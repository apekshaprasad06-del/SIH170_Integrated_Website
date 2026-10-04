const $=s=>document.querySelector(s);
let current=null, selected=null;

const fileInput=$("#fileInput"), dropzone=$("#dropzone"), fileLabel=$("#fileLabel"), runBtn=$("#runBtn"), runNote=$("#runNote");

function setFile(file){
  if(!file) return;
  fileInput.files = (()=>{const d=new DataTransfer();d.items.add(file);return d.files})();
  fileLabel.textContent=file.name;
  runBtn.disabled=false;
  runNote.textContent=`Ready · ${(file.size/1024).toFixed(0)} KB`;
}
fileInput.addEventListener("change",e=>setFile(e.target.files[0]));
["dragenter","dragover"].forEach(ev=>dropzone.addEventListener(ev,e=>{e.preventDefault();dropzone.style.borderColor="#6d756d"}));
["dragleave","drop"].forEach(ev=>dropzone.addEventListener(ev,e=>{e.preventDefault();dropzone.style.borderColor=""}));
dropzone.addEventListener("drop",e=>setFile(e.dataTransfer.files[0]));

async function health(){
  try{
    const r=await fetch("/api/health"), d=await r.json();
    if(d.module_b_ready){$("#statusDot").style.background="#637465";$("#statusText").textContent="Models ready"}
    else {$("#statusDot").style.background="#aa8757";$("#statusText").textContent="Module B starting…"}
  }catch(e){$("#statusDot").style.background="#a45b4d";$("#statusText").textContent="Server unavailable"}
}
health(); setInterval(health,5000);

runBtn.addEventListener("click",async()=>{
  const f=fileInput.files[0]; if(!f)return;
  runBtn.disabled=true; runBtn.textContent="Running…"; runNote.textContent="Module A screening, then Module B forecasting.";
  const fd=new FormData();fd.append("file",f);
  try{
    const r=await fetch("/api/screen",{method:"POST",body:fd});
    const d=await r.json();
    if(!r.ok)throw new Error(d.detail||"Screening failed");
    current=d; renderResults(d);
    $("#uploadCard").classList.add("hidden");$("#results").classList.remove("hidden");
  }catch(e){alert(e.message);runBtn.disabled=false;runBtn.textContent="Run integrated screening";runNote.textContent="Please check the CSV and try again."}
  finally{if(runBtn.textContent==="Running…"){runBtn.textContent="Run integrated screening";}}
});

$("#newRunBtn").addEventListener("click",()=>{current=null;$("#results").classList.add("hidden");$("#detail").classList.add("hidden");$("#uploadCard").classList.remove("hidden");fileInput.value="";fileLabel.textContent="Choose a CSV file";runBtn.disabled=true;runNote.textContent="Select a CSV to begin."});
$("#backBtn").addEventListener("click",()=>{$("#detail").classList.add("hidden");$("#results").classList.remove("hidden")});

function badge(v){
  const s=String(v||"").toLowerCase();
  const c=s==="safe"?"safe":s==="review"?"review":s==="reject"?"reject":"flag";
  return `<span class="badge ${c}">${String(v||"—").replaceAll("_"," ")}</span>`;
}
function renderResults(d){
  $("#resultTitle").textContent=d.filename;
  $("#resultMeta").textContent=`${d.rows.toLocaleString()} chips · ${d.lots} lots · Module A threshold ${Number(d.module_a.threshold).toFixed(2)}`;
  $("#nRows").textContent=d.rows.toLocaleString();
  $("#nLots").textContent=`${d.lots} lots`;
  $("#aFlagged").textContent=d.module_a.flagged.toLocaleString();
  $("#aRate").textContent=`${d.module_a.rejection_rate.toFixed(2)}% flagged`;
  const bc=d.module_b.decisions||{};
  const concern=(bc.REVIEW||0)+(bc.REJECT||0);
  $("#bConcern").textContent=concern.toLocaleString();
  renderBars(d);
  renderTable(d.records);
}
function renderBars(d){
  const total=d.rows;
  const a=d.module_a.flagged;
  const b=(d.module_b.decisions.REVIEW||0)+(d.module_b.decisions.REJECT||0);
  $("#bars").innerHTML=[
    ["Module A findings",a,"a"],
    ["Module B concerns",b,"b"],
  ].map(x=>`<div class="bar-row"><span>${x[0]}</span><div class="bar"><div class="fill ${x[2]==="b"?"b":""}" style="width:${Math.min(100,100*x[1]/Math.max(total,1))}%"></div></div><b>${x[1]}</b></div>`).join("");
}
function renderTable(rows){
  const q=($("#search").value||"").toLowerCase();
  const rr=rows.filter(r=>`${r.component_id} ${r.lot_id}`.toLowerCase().includes(q));
  $("#tableBody").innerHTML=rr.slice(0,300).map(r=>`<tr data-id="${r.component_id}">
    <td><b>${r.component_id}</b></td><td>${r.lot_id}</td>
    <td>${r.module_a_flagged?badge("FLAGGED"):badge("CLEAR")}</td>
    <td>${badge(r.module_b_overall)}</td>
    <td class="joint">${r.joint_status}</td>
    <td>${r.module_a_driver||"—"}</td>
  </tr>`).join("");
  $("#tableBody").querySelectorAll("tr").forEach(tr=>tr.addEventListener("click",()=>showDetail(tr.dataset.id)));
}
$("#search").addEventListener("input",()=>current&&renderTable(current.records));

function fmt(x,d=3){return x==null||!Number.isFinite(Number(x))?"—":Number(x).toFixed(d)}
function showDetail(id){
  selected=current.records.find(x=>x.component_id===id); if(!selected)return;
  $("#results").classList.add("hidden");$("#detail").classList.remove("hidden");
  $("#detailTitle").textContent=selected.component_id;
  $("#detailSub").textContent=`Lot ${selected.lot_id} · ${selected.joint_status}`;
  $("#aBadge").innerHTML=selected.module_a_flagged?badge("FLAGGED"):badge("CLEAR");
  const p=selected.module_a_parameters;
  $("#aDetail").innerHTML=`<div class="measure-grid">${Object.entries(p).map(([name,x])=>`
    <div class="measure"><label>${name} · 0h</label><b>${fmt(x.v0)}</b></div>
    <div class="measure"><label>${name} · 24h</label><b>${fmt(x.v24)}</b></div>
    <div class="measure"><label>drift</label><b>${fmt(x.drift_pct,1)}%</b></div>
  `).join("")}</div>
  <div class="reason"><b>Root cause:</b> ${selected.module_a_root_cause||"—"}<br>
  <b>Risk:</b> ${selected.module_a_risk||"—"} · <b>Confidence:</b> ${fmt(selected.module_a_confidence,2)}
  <br><b>Strongest feature:</b> ${selected.module_a_driver||"—"} · <b>max |z|:</b> ${fmt(selected.module_a_max_abs_z,2)}</div>`;
  $("#bBadge").innerHTML=badge(selected.module_b_overall);
  const bp=selected.module_b_parameters||{};
  $("#bDetail").innerHTML=Object.entries(bp).map(([name,x])=>{
    const lo=Number(x.interval_low), hi=Number(x.interval_high), pr=Number(x.prediction);
    const span=Math.max(hi-lo,1e-9), pos=Math.max(0,Math.min(100,100*(pr-lo)/span));
    const reasons=(x.reasons||[]).map(y=>`<div>• ${y}</div>`).join("");
    const contrib=(x.contributions||[]).slice(0,3).map(c=>`<div><span>${c.feature}</span><b>${fmt(c.contribution,3)}</b></div>`).join("");
    return `<div class="forecast-row">
      <div class="forecast-top"><b>${name}</b>${badge(x.decision)}</div>
      <div class="forecast-meta">168 h estimate · ${x.model_used} · lot z @24h ${fmt(x.lot_z_24h,2)}</div>
      <div class="range"><div class="center" style="left:${pos-2}%;width:4%"></div></div>
      <div class="range-label"><span>${fmt(lo)}</span><b>${fmt(pr)}</b><span>${fmt(hi)}</span></div>
      ${reasons?`<div class="reason">${reasons}</div>`:""}
    </div>
    ${contrib?`<div class="contrib">${contrib}</div>`:""}`;
  }).join("");
}
