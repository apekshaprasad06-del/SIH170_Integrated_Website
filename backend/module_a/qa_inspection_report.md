# QA Inspection Report - Module A Dynamic Outlier Detection

_Generated 2026-09-30 07:16 UTC | attribution method: fallback_

## Executive Summary

- Chips screened: **1978** across **8** lots
- Chips rejected: **222** (11.22%)
- Static-limit breaches: **0**
- Root causes: SINGLE_PARAMETER_PEER_OUTLIER: 121, MULTIVARIATE_LATENT_DRIFT: 101
- Risk levels: CRITICAL: 139, ELEVATED: 50, HIGH: 33

### Detection Metrics (ground truth available)

| Scope | Recall | Precision | F2 | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|
| Full population | 0.993 | 0.640 | 0.894 | 1755 | 80 | 1 | 142 |
| Calibration split | 1.000 | 0.632 | 0.896 | 875 | 42 | 0 | 72 |
| Held-out split | 0.986 | 0.648 | 0.893 | 880 | 38 | 1 | 70 |
| Static-limit screening (baseline) | 0.000 | 0.000 | 0.000 | 1835 | 0 | 143 | 0 |
| Isolation Forest only | 0.916 | 0.814 | 0.894 | 1805 | 30 | 12 | 131 |
| DPAT rule only | 0.993 | 0.676 | 0.908 | 1767 | 68 | 1 | 142 |

## Rejected Serial Numbers

| Serial | Lot | Root cause | Risk | Confidence |
|---|---|---|---|---|
| SN05-0175 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN03-0228 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN04-0074 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0163 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0107 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN07-0071 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN04-0022 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0170 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0032 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0217 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN04-0051 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN03-0265 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0187 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN08-0028 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN08-0226 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN08-0231 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN08-0164 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN08-0139 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN05-0044 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0018 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN04-0052 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN05-0119 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN05-0051 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN07-0172 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0057 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0072 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN03-0100 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN02-0012 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN08-0219 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN08-0098 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0105 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN03-0086 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN06-0037 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN07-0146 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN01-0225 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN02-0019 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN08-0041 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN03-0077 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN03-0071 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 1.000 |
| SN05-0090 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN08-0016 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN05-0112 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 1.000 |
| SN03-0218 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN04-0249 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.999 |
| SN02-0195 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN06-0166 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN02-0140 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN07-0188 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.999 |
| SN03-0045 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.999 |
| SN03-0154 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN02-0044 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN01-0243 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.999 |
| SN02-0134 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.999 |
| SN02-0254 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.999 |
| SN08-0181 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN01-0177 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.998 |
| SN05-0103 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN01-0251 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN04-0231 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN05-0082 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN07-0098 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN08-0171 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.998 |
| SN03-0224 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.998 |
| SN03-0167 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.997 |
| SN02-0071 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.997 |
| SN04-0087 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.997 |
| SN02-0183 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.997 |
| SN02-0232 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.997 |
| SN03-0050 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.996 |
| SN03-0016 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.996 |
| SN02-0124 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.996 |
| SN07-0141 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.996 |
| SN06-0136 | LOT-F | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.996 |
| SN07-0205 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.995 |
| SN02-0017 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.995 |
| SN02-0088 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.993 |
| SN02-0206 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.993 |
| SN03-0133 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.993 |
| SN03-0212 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.993 |
| SN08-0151 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.993 |
| SN07-0029 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.991 |
| SN01-0004 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.991 |
| SN03-0140 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.991 |
| SN08-0034 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.991 |
| SN02-0152 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.990 |
| SN06-0117 | LOT-F | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.990 |
| SN04-0270 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.989 |
| SN03-0259 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.989 |
| SN01-0159 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.989 |
| SN08-0029 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.989 |
| SN08-0073 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.987 |
| SN05-0100 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.986 |
| SN01-0007 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.984 |
| SN06-0107 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.984 |
| SN05-0053 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.984 |
| SN08-0015 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.984 |
| SN03-0248 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.977 |
| SN06-0051 | LOT-F | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.977 |
| SN08-0170 | LOT-H | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.975 |
| SN04-0064 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.974 |
| SN05-0007 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.974 |
| SN03-0168 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.972 |
| SN08-0221 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.971 |
| SN06-0125 | LOT-F | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.971 |
| SN02-0028 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.970 |
| SN05-0017 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.969 |
| SN02-0243 | LOT-B | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.966 |
| SN07-0120 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.960 |
| SN02-0016 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.958 |
| SN07-0156 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.954 |
| SN02-0274 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.953 |
| SN01-0194 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.951 |
| SN08-0048 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.950 |
| SN04-0225 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.933 |
| SN01-0193 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.928 |
| SN07-0102 | LOT-G | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.926 |
| SN01-0035 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.924 |
| SN06-0024 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.924 |
| SN02-0218 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.922 |
| SN05-0179 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.919 |
| SN01-0203 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.914 |
| SN03-0172 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.912 |
| SN01-0160 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.912 |
| SN08-0007 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.910 |
| SN04-0063 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.909 |
| SN04-0120 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.906 |
| SN01-0058 | LOT-A | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.892 |
| SN03-0081 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.876 |
| SN08-0232 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.875 |
| SN03-0247 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.869 |
| SN03-0201 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.862 |
| SN04-0065 | LOT-D | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.849 |
| SN03-0138 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.824 |
| SN07-0103 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.816 |
| SN08-0097 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.814 |
| SN04-0050 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.812 |
| SN03-0126 | LOT-C | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.810 |
| SN08-0207 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.795 |
| SN02-0237 | LOT-B | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.794 |
| SN05-0101 | LOT-E | MULTIVARIATE_LATENT_DRIFT | CRITICAL | 0.782 |
| SN08-0115 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.782 |
| SN03-0040 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | CRITICAL | 0.782 |
| SN05-0019 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.779 |
| SN08-0077 | LOT-H | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.778 |
| SN01-0218 | LOT-A | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.777 |
| SN04-0023 | LOT-D | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.762 |
| SN02-0094 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.757 |
| SN03-0260 | LOT-C | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.757 |
| SN05-0061 | LOT-E | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.752 |
| SN05-0172 | LOT-E | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.743 |
| SN08-0137 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.742 |
| SN01-0106 | LOT-A | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.740 |
| SN02-0214 | LOT-B | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.740 |
| SN04-0036 | LOT-D | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.737 |
| SN08-0184 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.732 |
| SN07-0184 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.729 |
| SN05-0201 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.722 |
| SN03-0002 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.718 |
| SN06-0090 | LOT-F | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.709 |
| SN01-0146 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.706 |
| SN07-0173 | LOT-G | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.701 |
| SN02-0202 | LOT-B | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.697 |
| SN05-0035 | LOT-E | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.690 |
| SN03-0095 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.690 |
| SN08-0058 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.680 |
| SN02-0076 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.679 |
| SN06-0027 | LOT-F | MULTIVARIATE_LATENT_DRIFT | HIGH | 0.675 |
| SN02-0104 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.674 |
| SN01-0219 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.662 |
| SN03-0060 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.659 |
| SN08-0092 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.651 |
| SN01-0158 | LOT-A | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.643 |
| SN02-0027 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | HIGH | 0.643 |
| SN04-0007 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.636 |
| SN04-0157 | LOT-D | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.635 |
| SN07-0013 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.626 |
| SN01-0221 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.625 |
| SN03-0084 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.622 |
| SN02-0224 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.622 |
| SN03-0051 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.613 |
| SN03-0075 | LOT-C | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.611 |
| SN08-0023 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.610 |
| SN08-0174 | LOT-H | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.605 |
| SN02-0255 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.601 |
| SN07-0034 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.597 |
| SN04-0208 | LOT-D | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.594 |
| SN04-0073 | LOT-D | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.594 |
| SN05-0013 | LOT-E | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.589 |
| SN08-0159 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.583 |
| SN04-0123 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.579 |
| SN02-0031 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.579 |
| SN04-0244 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.574 |
| SN03-0254 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.569 |
| SN03-0101 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.568 |
| SN01-0052 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.564 |
| SN03-0022 | LOT-C | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.561 |
| SN04-0040 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.556 |
| SN08-0149 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.556 |
| SN07-0031 | LOT-G | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.555 |
| SN02-0072 | LOT-B | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.551 |
| SN08-0102 | LOT-H | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.548 |
| SN06-0077 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.547 |
| SN01-0215 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.541 |
| SN06-0139 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.534 |
| SN07-0101 | LOT-G | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.533 |
| SN04-0207 | LOT-D | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.531 |
| SN02-0125 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.529 |
| SN02-0057 | LOT-B | MULTIVARIATE_LATENT_DRIFT | ELEVATED | 0.525 |
| SN01-0191 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.524 |
| SN06-0004 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.524 |
| SN02-0248 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.521 |
| SN03-0160 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.520 |
| SN03-0150 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.519 |
| SN06-0124 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.517 |
| SN06-0135 | LOT-F | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.517 |
| SN03-0005 | LOT-C | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.517 |
| SN01-0206 | LOT-A | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.517 |
| SN02-0193 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.516 |
| SN04-0273 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.515 |
| SN02-0167 | LOT-B | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.509 |
| SN04-0241 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.508 |
| SN04-0061 | LOT-D | SINGLE_PARAMETER_PEER_OUTLIER | ELEVATED | 0.501 |

## Inspection Certificates

### Certificate 001 - SN05-0175 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 36.20 µA | 56.58 µA | 21.74 µA | 2.60x | 14.5 | 57% |
| Leakage Current (Ileak) | 13.94 µA | 24.69 µA | 5.71 µA | 4.33x | 19.5 | 49% |
| Propagation Delay (tpd) | 9.79 ns | 10.48 ns | 8.87 ns | 1.18x | 9.1 | 70% |

**Parameter contribution:** Standby Current (Iddq) 32%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 20%

**Top attribution features:** leakage drift z-score (+19.488); Iddq drift z-score (+14.466); leakage z-score @24h (+9.740)

**Evidence:** Leakage Current (Ileak) reads 24.69 µA at 24h against a lot median of 5.71 µA (4.33x lot median) and uses 49% of the 50 µA datasheet limit. Drift is +77.1% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN05-0175](plots/waterfall_SN05-0175.png)

### Certificate 002 - SN03-0228 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.29 µA | 41.60 µA | 14.53 µA | 2.86x | 8.5 | 42% |
| Leakage Current (Ileak) | 23.50 µA | 44.73 µA | 8.19 µA | 5.46x | 39.1 | 89% |
| Propagation Delay (tpd) | 8.36 ns | 8.83 ns | 8.33 ns | 1.06x | 6.8 | 59% |

**Parameter contribution:** Standby Current (Iddq) 22%, Leakage Current (Ileak) 68%, Propagation Delay (tpd) 10%

**Top attribution features:** leakage drift z-score (+39.136); leakage z-score @24h (+10.502); Iddq drift z-score (+8.547)

**Evidence:** Leakage Current (Ileak) reads 44.73 µA at 24h against a lot median of 8.19 µA (5.46x lot median) and uses 89% of the 50 µA datasheet limit. Drift is +90.4% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN03-0228](plots/waterfall_SN03-0228.png)

### Certificate 003 - SN04-0074 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 52.40 µA | 71.06 µA | 17.67 µA | 4.02x | 12.0 | 71% |
| Leakage Current (Ileak) | 24.63 µA | 33.31 µA | 6.43 µA | 5.18x | 9.5 | 67% |
| Propagation Delay (tpd) | 10.25 ns | 10.57 ns | 10.33 ns | 1.02x | 2.2 | 70% |

**Parameter contribution:** Standby Current (Iddq) 49%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq drift z-score (+12.036); leakage z-score @24h (+9.522); Iddq z-score @24h (+8.635)

**Evidence:** Standby Current (Iddq) reads 71.06 µA at 24h against a lot median of 17.67 µA (4.02x lot median) and uses 71% of the 100 µA datasheet limit. Drift is +35.6% versus a lot-median drift of +4.5%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

![Waterfall for SN04-0074](plots/waterfall_SN04-0074.png)

### Certificate 004 - SN02-0163 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.63 µA | 52.66 µA | 18.95 µA | 2.78x | 15.3 | 53% |
| Leakage Current (Ileak) | 10.38 µA | 17.47 µA | 6.95 µA | 2.51x | 24.6 | 35% |
| Propagation Delay (tpd) | 9.79 ns | 10.62 ns | 9.82 ns | 1.08x | 8.1 | 71% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 15%

**Top attribution features:** leakage drift z-score (+24.556); Iddq drift z-score (+15.300); delay drift z-score (+8.135)

**Evidence:** Leakage Current (Ileak) reads 17.47 µA at 24h against a lot median of 6.95 µA (2.51x lot median) and uses 35% of the 50 µA datasheet limit. Drift is +68.4% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN02-0163](plots/waterfall_SN02-0163.png)

### Certificate 005 - SN01-0107 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 61.49 µA | 84.53 µA | 24.51 µA | 3.45x | 15.6 | 85% |
| Leakage Current (Ileak) | 18.30 µA | 29.98 µA | 9.64 µA | 3.11x | 20.3 | 60% |
| Propagation Delay (tpd) | 8.61 ns | 9.02 ns | 8.46 ns | 1.07x | 5.5 | 60% |

**Parameter contribution:** Standby Current (Iddq) 42%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage drift z-score (+20.277); Iddq drift z-score (+15.574); Iddq z-score @24h (+5.946)

**Evidence:** Leakage Current (Ileak) reads 29.98 µA at 24h against a lot median of 9.64 µA (3.11x lot median) and uses 60% of the 50 µA datasheet limit. Drift is +63.9% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN01-0107](plots/waterfall_SN01-0107.png)

### Certificate 006 - SN07-0071 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 30.39 µA | 46.59 µA | 17.12 µA | 2.72x | 15.3 | 47% |
| Leakage Current (Ileak) | 15.20 µA | 24.84 µA | 10.67 µA | 2.33x | 23.5 | 50% |
| Propagation Delay (tpd) | 9.68 ns | 10.20 ns | 8.96 ns | 1.14x | 5.1 | 68% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+23.526); Iddq drift z-score (+15.292); Iddq z-score @24h (+5.809)

**Evidence:** Leakage Current (Ileak) reads 24.84 µA at 24h against a lot median of 10.67 µA (2.33x lot median) and uses 50% of the 50 µA datasheet limit. Drift is +63.5% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN07-0071](plots/waterfall_SN07-0071.png)

### Certificate 007 - SN04-0022 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 28.18 µA | 51.47 µA | 17.67 µA | 2.91x | 30.2 | 51% |
| Leakage Current (Ileak) | 17.34 µA | 27.01 µA | 6.43 µA | 4.20x | 13.6 | 54% |
| Propagation Delay (tpd) | 10.76 ns | 11.46 ns | 10.33 ns | 1.11x | 6.1 | 76% |

**Parameter contribution:** Standby Current (Iddq) 53%, Leakage Current (Ileak) 35%, Propagation Delay (tpd) 12%

**Top attribution features:** Iddq drift z-score (+30.202); leakage drift z-score (+13.560); leakage z-score @24h (+7.290)

**Evidence:** Standby Current (Iddq) reads 51.47 µA at 24h against a lot median of 17.67 µA (2.91x lot median) and uses 51% of the 100 µA datasheet limit. Drift is +82.6% versus a lot-median drift of +4.5%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

![Waterfall for SN04-0022](plots/waterfall_SN04-0022.png)

### Certificate 008 - SN02-0170 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 30.78 µA | 51.49 µA | 18.95 µA | 2.72x | 16.9 | 51% |
| Leakage Current (Ileak) | 10.01 µA | 15.69 µA | 6.95 µA | 2.26x | 20.1 | 31% |
| Propagation Delay (tpd) | 10.71 ns | 11.34 ns | 9.82 ns | 1.15x | 5.1 | 76% |

**Parameter contribution:** Standby Current (Iddq) 43%, Leakage Current (Ileak) 41%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+20.090); Iddq drift z-score (+16.934); Iddq z-score @24h (+6.110)

**Evidence:** Standby Current (Iddq) reads 51.49 µA at 24h against a lot median of 18.95 µA (2.72x lot median) and uses 51% of the 100 µA datasheet limit. Drift is +67.3% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

![Waterfall for SN02-0170](plots/waterfall_SN02-0170.png)

### Certificate 009 - SN02-0032 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.04 µA | 49.33 µA | 18.95 µA | 2.60x | 13.2 | 49% |
| Leakage Current (Ileak) | 11.30 µA | 20.91 µA | 6.95 µA | 3.01x | 31.0 | 42% |
| Propagation Delay (tpd) | 9.76 ns | 10.57 ns | 9.82 ns | 1.08x | 8.1 | 70% |

**Parameter contribution:** Standby Current (Iddq) 32%, Leakage Current (Ileak) 55%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage drift z-score (+30.974); Iddq drift z-score (+13.243); delay drift z-score (+8.086)

**Evidence:** Leakage Current (Ileak) reads 20.91 µA at 24h against a lot median of 6.95 µA (3.01x lot median) and uses 42% of the 50 µA datasheet limit. Drift is +85.0% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

![Waterfall for SN02-0032](plots/waterfall_SN02-0032.png)

### Certificate 010 - SN02-0217 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.96 µA | 49.05 µA | 18.95 µA | 2.59x | 19.2 | 49% |
| Leakage Current (Ileak) | 10.59 µA | 16.91 µA | 6.95 µA | 2.43x | 21.2 | 34% |
| Propagation Delay (tpd) | 10.38 ns | 10.97 ns | 9.82 ns | 1.12x | 5.0 | 73% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 43%, Propagation Delay (tpd) 13%

**Top attribution features:** leakage drift z-score (+21.242); Iddq drift z-score (+19.187); Iddq z-score @24h (+5.651)

**Evidence:** Standby Current (Iddq) reads 49.05 µA at 24h against a lot median of 18.95 µA (2.59x lot median) and uses 49% of the 100 µA datasheet limit. Drift is +75.4% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

![Waterfall for SN02-0217](plots/waterfall_SN02-0217.png)

### Certificate 011 - SN04-0051 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 33.14 µA | 48.11 µA | 17.67 µA | 2.72x | 15.7 | 48% |
| Leakage Current (Ileak) | 16.72 µA | 27.07 µA | 6.43 µA | 4.21x | 15.2 | 54% |
| Propagation Delay (tpd) | 10.85 ns | 11.47 ns | 10.33 ns | 1.11x | 5.3 | 76% |

**Parameter contribution:** Standby Current (Iddq) 40%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq drift z-score (+15.719); leakage drift z-score (+15.244); leakage z-score @24h (+7.313)

**Evidence:** Leakage Current (Ileak) reads 27.07 µA at 24h against a lot median of 6.43 µA (4.21x lot median) and uses 54% of the 50 µA datasheet limit. Drift is +61.9% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 012 - SN03-0265 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.55 µA | 43.74 µA | 14.53 µA | 3.01x | 7.7 | 44% |
| Leakage Current (Ileak) | 39.78 µA | 46.80 µA | 8.19 µA | 5.72x | 11.1 | 94% |
| Propagation Delay (tpd) | 8.44 ns | 8.96 ns | 8.33 ns | 1.08x | 7.4 | 60% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 50%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage z-score @24h (+11.097); leakage z-score @0h (+9.633); Iddq drift z-score (+7.713)

**Evidence:** Leakage Current (Ileak) reads 46.80 µA at 24h against a lot median of 8.19 µA (5.72x lot median) and uses 94% of the 50 µA datasheet limit. Drift is +17.6% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 013 - SN01-0187 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 59.26 µA | 85.24 µA | 24.51 µA | 3.48x | 18.5 | 85% |
| Leakage Current (Ileak) | 16.07 µA | 24.07 µA | 9.64 µA | 2.50x | 15.4 | 48% |
| Propagation Delay (tpd) | 8.38 ns | 8.85 ns | 8.46 ns | 1.05x | 6.9 | 59% |

**Parameter contribution:** Standby Current (Iddq) 50%, Leakage Current (Ileak) 37%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq drift z-score (+18.532); leakage drift z-score (+15.443); delay drift z-score (+6.865)

**Evidence:** Standby Current (Iddq) reads 85.24 µA at 24h against a lot median of 24.51 µA (3.48x lot median) and uses 85% of the 100 µA datasheet limit. Drift is +43.8% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 014 - SN08-0028 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.09 µA | 37.57 µA | 12.78 µA | 2.94x | 16.2 | 38% |
| Leakage Current (Ileak) | 12.89 µA | 18.59 µA | 5.03 µA | 3.70x | 20.5 | 37% |
| Propagation Delay (tpd) | 8.41 ns | 8.67 ns | 8.48 ns | 1.02x | 2.1 | 58% |

**Parameter contribution:** Standby Current (Iddq) 40%, Leakage Current (Ileak) 55%, Propagation Delay (tpd) 5%

**Top attribution features:** leakage drift z-score (+20.479); Iddq drift z-score (+16.170); leakage z-score @24h (+6.705)

**Evidence:** Leakage Current (Ileak) reads 18.59 µA at 24h against a lot median of 5.03 µA (3.70x lot median) and uses 37% of the 50 µA datasheet limit. Drift is +44.2% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 015 - SN08-0226 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.39 µA | 21.46 µA | 12.78 µA | 1.68x | 1.6 | 21% |
| Leakage Current (Ileak) | 4.65 µA | 4.69 µA | 5.03 µA | 0.93x | 1.2 | 9% |
| Propagation Delay (tpd) | 11.80 ns | 12.90 ns | 8.48 ns | 1.52x | 11.8 | 86% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 87%

**Top attribution features:** delay z-score @24h (+11.828); delay z-score @0h (+10.405); delay drift z-score (+9.706)

**Evidence:** Propagation Delay (tpd) reads 12.90 ns at 24h against a lot median of 8.48 ns (1.52x lot median) and uses 86% of the 15 ns datasheet limit. Drift is +9.3% versus a lot-median drift of +1.3%.

### Certificate 016 - SN08-0231 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.62 µA | 17.29 µA | 12.78 µA | 1.35x | 0.9 | 17% |
| Leakage Current (Ileak) | 9.55 µA | 9.66 µA | 5.03 µA | 1.92x | 2.3 | 19% |
| Propagation Delay (tpd) | 10.67 ns | 11.82 ns | 8.48 ns | 1.39x | 11.4 | 79% |

**Parameter contribution:** Standby Current (Iddq) 6%, Leakage Current (Ileak) 16%, Propagation Delay (tpd) 78%

**Top attribution features:** delay drift z-score (+11.439); delay z-score @24h (+8.935); delay z-score @0h (+7.008)

**Evidence:** Propagation Delay (tpd) reads 11.82 ns at 24h against a lot median of 8.48 ns (1.39x lot median) and uses 79% of the 15 ns datasheet limit. Drift is +10.7% versus a lot-median drift of +1.3%.

### Certificate 017 - SN08-0164 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.84 µA | 12.01 µA | 12.78 µA | 0.94x | 1.3 | 12% |
| Leakage Current (Ileak) | 5.19 µA | 5.38 µA | 5.03 µA | 1.07x | 0.2 | 11% |
| Propagation Delay (tpd) | 11.51 ns | 13.29 ns | 8.48 ns | 1.57x | 17.2 | 89% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 1%, Propagation Delay (tpd) 95%

**Top attribution features:** delay drift z-score (+17.176); delay z-score @24h (+12.868); delay z-score @0h (+9.523)

**Evidence:** Propagation Delay (tpd) reads 13.29 ns at 24h against a lot median of 8.48 ns (1.57x lot median) and uses 89% of the 15 ns datasheet limit. Drift is +15.5% versus a lot-median drift of +1.3%.

### Certificate 018 - SN08-0139 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 19.69 µA | 27.71 µA | 12.78 µA | 2.17x | 12.9 | 28% |
| Leakage Current (Ileak) | 7.72 µA | 12.27 µA | 5.03 µA | 2.44x | 27.9 | 25% |
| Propagation Delay (tpd) | 8.39 ns | 8.98 ns | 8.48 ns | 1.06x | 6.9 | 60% |

**Parameter contribution:** Standby Current (Iddq) 29%, Leakage Current (Ileak) 56%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage drift z-score (+27.902); Iddq drift z-score (+12.889); delay drift z-score (+6.922)

**Evidence:** Leakage Current (Ileak) reads 12.27 µA at 24h against a lot median of 5.03 µA (2.44x lot median) and uses 25% of the 50 µA datasheet limit. Drift is +59.0% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 019 - SN05-0044 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 43.61 µA | 46.59 µA | 21.74 µA | 2.14x | 4.1 | 47% |
| Leakage Current (Ileak) | 27.59 µA | 30.61 µA | 5.71 µA | 5.36x | 12.8 | 61% |
| Propagation Delay (tpd) | 7.60 ns | 7.66 ns | 8.87 ns | 0.86x | 2.2 | 51% |

**Parameter contribution:** Standby Current (Iddq) 21%, Leakage Current (Ileak) 67%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage z-score @24h (+12.776); leakage z-score @0h (+12.702); Iddq z-score @24h (+4.149)

**Evidence:** Leakage Current (Ileak) reads 30.61 µA at 24h against a lot median of 5.71 µA (5.36x lot median) and uses 61% of the 50 µA datasheet limit. Drift is +11.0% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 020 - SN01-0018 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 39.31 µA | 61.03 µA | 24.51 µA | 2.49x | 23.8 | 61% |
| Leakage Current (Ileak) | 14.77 µA | 22.22 µA | 9.64 µA | 2.31x | 15.7 | 44% |
| Propagation Delay (tpd) | 8.90 ns | 9.23 ns | 8.46 ns | 1.09x | 4.0 | 62% |

**Parameter contribution:** Standby Current (Iddq) 52%, Leakage Current (Ileak) 36%, Propagation Delay (tpd) 12%

**Top attribution features:** Iddq drift z-score (+23.815); leakage drift z-score (+15.653); delay drift z-score (+4.001)

**Evidence:** Standby Current (Iddq) reads 61.03 µA at 24h against a lot median of 24.51 µA (2.49x lot median) and uses 61% of the 100 µA datasheet limit. Drift is +55.2% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 021 - SN04-0052 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.24 µA | 39.49 µA | 17.67 µA | 2.24x | 11.8 | 39% |
| Leakage Current (Ileak) | 8.81 µA | 14.22 µA | 6.43 µA | 2.21x | 15.1 | 28% |
| Propagation Delay (tpd) | 11.69 ns | 12.38 ns | 10.33 ns | 1.20x | 5.4 | 83% |

**Parameter contribution:** Standby Current (Iddq) 37%, Leakage Current (Ileak) 40%, Propagation Delay (tpd) 23%

**Top attribution features:** leakage drift z-score (+15.107); Iddq drift z-score (+11.821); delay drift z-score (+5.369)

**Evidence:** Leakage Current (Ileak) reads 14.22 µA at 24h against a lot median of 6.43 µA (2.21x lot median) and uses 28% of the 50 µA datasheet limit. Drift is +61.4% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 022 - SN05-0119 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.60 µA | 23.26 µA | 21.74 µA | 1.07x | 2.0 | 23% |
| Leakage Current (Ileak) | 5.41 µA | 5.79 µA | 5.71 µA | 1.01x | 0.1 | 12% |
| Propagation Delay (tpd) | 12.73 ns | 14.08 ns | 8.87 ns | 1.59x | 14.4 | 94% |

**Parameter contribution:** Standby Current (Iddq) 7%, Leakage Current (Ileak) 1%, Propagation Delay (tpd) 93%

**Top attribution features:** delay drift z-score (+14.387); delay z-score @24h (+9.393); delay z-score @0h (+7.249)

**Evidence:** Propagation Delay (tpd) reads 14.08 ns at 24h against a lot median of 8.87 ns (1.59x lot median) and uses 94% of the 15 ns datasheet limit. Drift is +10.6% versus a lot-median drift of +1.1%.

### Certificate 023 - SN05-0051 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.98 µA | 45.04 µA | 21.74 µA | 2.07x | 10.0 | 45% |
| Leakage Current (Ileak) | 9.37 µA | 14.23 µA | 5.71 µA | 2.49x | 12.5 | 28% |
| Propagation Delay (tpd) | 8.88 ns | 9.60 ns | 8.87 ns | 1.08x | 10.7 | 64% |

**Parameter contribution:** Standby Current (Iddq) 34%, Leakage Current (Ileak) 41%, Propagation Delay (tpd) 26%

**Top attribution features:** leakage drift z-score (+12.498); delay drift z-score (+10.698); Iddq drift z-score (+10.042)

**Evidence:** Leakage Current (Ileak) reads 14.23 µA at 24h against a lot median of 5.71 µA (2.49x lot median) and uses 28% of the 50 µA datasheet limit. Drift is +51.9% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 024 - SN07-0172 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.04 µA | 36.56 µA | 17.12 µA | 2.14x | 13.0 | 37% |
| Leakage Current (Ileak) | 15.83 µA | 25.32 µA | 10.67 µA | 2.37x | 22.1 | 51% |
| Propagation Delay (tpd) | 9.13 ns | 9.55 ns | 8.96 ns | 1.07x | 4.1 | 64% |

**Parameter contribution:** Standby Current (Iddq) 36%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage drift z-score (+22.092); Iddq drift z-score (+12.989); delay drift z-score (+4.086)

**Evidence:** Leakage Current (Ileak) reads 25.32 µA at 24h against a lot median of 10.67 µA (2.37x lot median) and uses 51% of the 50 µA datasheet limit. Drift is +59.9% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 025 - SN01-0057 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.60 µA | 24.21 µA | 24.51 µA | 0.99x | 0.6 | 24% |
| Leakage Current (Ileak) | 9.03 µA | 10.78 µA | 9.64 µA | 1.12x | 4.9 | 22% |
| Propagation Delay (tpd) | 11.26 ns | 12.52 ns | 8.46 ns | 1.48x | 15.2 | 83% |

**Parameter contribution:** Standby Current (Iddq) 2%, Leakage Current (Ileak) 15%, Propagation Delay (tpd) 84%

**Top attribution features:** delay drift z-score (+15.239); delay z-score @24h (+8.162); delay z-score @0h (+6.270)

**Evidence:** Propagation Delay (tpd) reads 12.52 ns at 24h against a lot median of 8.46 ns (1.48x lot median) and uses 83% of the 15 ns datasheet limit. Drift is +11.2% versus a lot-median drift of +1.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 026 - SN01-0072 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 37.88 µA | 51.70 µA | 24.51 µA | 2.11x | 15.1 | 52% |
| Leakage Current (Ileak) | 14.48 µA | 23.48 µA | 9.64 µA | 2.44x | 19.7 | 47% |
| Propagation Delay (tpd) | 8.79 ns | 9.08 ns | 8.46 ns | 1.07x | 3.5 | 61% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 49%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage drift z-score (+19.700); Iddq drift z-score (+15.127); delay drift z-score (+3.476)

**Evidence:** Leakage Current (Ileak) reads 23.48 µA at 24h against a lot median of 9.64 µA (2.44x lot median) and uses 47% of the 50 µA datasheet limit. Drift is +62.2% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 027 - SN03-0100 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 13.03 µA | 14.53 µA | 0.90x | 0.3 | 13% |
| Leakage Current (Ileak) | 7.53 µA | 7.76 µA | 8.19 µA | 0.95x | 0.7 | 16% |
| Propagation Delay (tpd) | 13.15 ns | 14.06 ns | 8.33 ns | 1.69x | 11.3 | 94% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 3%, Propagation Delay (tpd) 95%

**Top attribution features:** delay z-score @24h (+11.256); delay z-score @0h (+10.401); delay drift z-score (+8.513)

**Evidence:** Propagation Delay (tpd) reads 14.06 ns at 24h against a lot median of 8.33 ns (1.69x lot median) and uses 94% of the 15 ns datasheet limit. Drift is +6.9% versus a lot-median drift of +1.1%.

### Certificate 028 - SN02-0012 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.03 µA | 37.80 µA | 18.95 µA | 1.99x | 9.3 | 38% |
| Leakage Current (Ileak) | 12.12 µA | 18.60 µA | 6.95 µA | 2.68x | 18.8 | 37% |
| Propagation Delay (tpd) | 9.78 ns | 10.44 ns | 9.82 ns | 1.06x | 6.2 | 70% |

**Parameter contribution:** Standby Current (Iddq) 32%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 15%

**Top attribution features:** leakage drift z-score (+18.832); Iddq drift z-score (+9.339); delay drift z-score (+6.190)

**Evidence:** Leakage Current (Ileak) reads 18.60 µA at 24h against a lot median of 6.95 µA (2.68x lot median) and uses 37% of the 50 µA datasheet limit. Drift is +53.5% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 029 - SN08-0219 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.12 µA | 31.34 µA | 12.78 µA | 2.45x | 11.0 | 31% |
| Leakage Current (Ileak) | 7.96 µA | 11.69 µA | 5.03 µA | 2.33x | 21.8 | 23% |
| Propagation Delay (tpd) | 8.49 ns | 8.92 ns | 8.48 ns | 1.05x | 4.5 | 59% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 54%, Propagation Delay (tpd) 13%

**Top attribution features:** leakage drift z-score (+21.808); Iddq drift z-score (+11.024); delay drift z-score (+4.543)

**Evidence:** Leakage Current (Ileak) reads 11.69 µA at 24h against a lot median of 5.03 µA (2.33x lot median) and uses 23% of the 50 µA datasheet limit. Drift is +46.9% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 030 - SN08-0098 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.35 µA | 26.51 µA | 12.78 µA | 2.07x | 14.2 | 27% |
| Leakage Current (Ileak) | 8.22 µA | 10.66 µA | 5.03 µA | 2.12x | 13.1 | 21% |
| Propagation Delay (tpd) | 9.28 ns | 9.50 ns | 8.48 ns | 1.12x | 2.8 | 63% |

**Parameter contribution:** Standby Current (Iddq) 42%, Leakage Current (Ileak) 42%, Propagation Delay (tpd) 16%

**Top attribution features:** Iddq drift z-score (+14.238); leakage drift z-score (+13.144); delay z-score @0h (+2.824)

**Evidence:** Standby Current (Iddq) reads 26.51 µA at 24h against a lot median of 12.78 µA (2.07x lot median) and uses 27% of the 100 µA datasheet limit. Drift is +44.4% versus a lot-median drift of +5.2%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 031 - SN02-0105 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.62 µA | 30.15 µA | 18.95 µA | 1.59x | 2.3 | 30% |
| Leakage Current (Ileak) | 39.99 µA | 46.12 µA | 6.95 µA | 6.64x | 14.4 | 92% |
| Propagation Delay (tpd) | 9.55 ns | 9.63 ns | 9.82 ns | 0.98x | 0.7 | 64% |

**Parameter contribution:** Standby Current (Iddq) 14%, Leakage Current (Ileak) 83%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage z-score @24h (+14.361); leakage z-score @0h (+12.734); leakage drift z-score (+4.121)

**Evidence:** Leakage Current (Ileak) reads 46.12 µA at 24h against a lot median of 6.95 µA (6.64x lot median) and uses 92% of the 50 µA datasheet limit. Drift is +15.3% versus a lot-median drift of +4.6%.

### Certificate 032 - SN03-0086 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.18 µA | 30.99 µA | 14.53 µA | 2.13x | 8.0 | 31% |
| Leakage Current (Ileak) | 23.08 µA | 33.30 µA | 8.19 µA | 4.07x | 18.2 | 67% |
| Propagation Delay (tpd) | 8.20 ns | 8.48 ns | 8.33 ns | 1.02x | 3.3 | 57% |

**Parameter contribution:** Standby Current (Iddq) 28%, Leakage Current (Ileak) 64%, Propagation Delay (tpd) 8%

**Top attribution features:** leakage drift z-score (+18.159); Iddq drift z-score (+7.967); leakage z-score @24h (+7.218)

**Evidence:** Leakage Current (Ileak) reads 33.30 µA at 24h against a lot median of 8.19 µA (4.07x lot median) and uses 67% of the 50 µA datasheet limit. Drift is +44.3% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 033 - SN06-0037 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.36 µA | 21.00 µA | 21.75 µA | 0.97x | 0.7 | 21% |
| Leakage Current (Ileak) | 7.56 µA | 7.76 µA | 7.94 µA | 0.98x | 0.7 | 16% |
| Propagation Delay (tpd) | 13.56 ns | 14.30 ns | 9.80 ns | 1.46x | 8.9 | 95% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 3%, Propagation Delay (tpd) 94%

**Top attribution features:** delay drift z-score (+8.930); delay z-score @24h (+8.909); delay z-score @0h (+7.800)

**Evidence:** Propagation Delay (tpd) reads 14.30 ns at 24h against a lot median of 9.80 ns (1.46x lot median) and uses 95% of the 15 ns datasheet limit. Drift is +5.5% versus a lot-median drift of +0.8%.

### Certificate 034 - SN07-0146 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.90 µA | 30.12 µA | 17.12 µA | 1.76x | 8.4 | 30% |
| Leakage Current (Ileak) | 20.54 µA | 28.92 µA | 10.67 µA | 2.71x | 14.4 | 58% |
| Propagation Delay (tpd) | 9.15 ns | 9.63 ns | 8.96 ns | 1.07x | 5.0 | 64% |

**Parameter contribution:** Standby Current (Iddq) 30%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+14.409); Iddq drift z-score (+8.379); delay drift z-score (+4.958)

**Evidence:** Leakage Current (Ileak) reads 28.92 µA at 24h against a lot median of 10.67 µA (2.71x lot median) and uses 58% of the 50 µA datasheet limit. Drift is +40.8% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 035 - SN01-0225 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 64.84 µA | 83.64 µA | 24.51 µA | 3.41x | 11.7 | 84% |
| Leakage Current (Ileak) | 13.45 µA | 18.69 µA | 9.64 µA | 1.94x | 11.7 | 37% |
| Propagation Delay (tpd) | 8.37 ns | 8.62 ns | 8.46 ns | 1.02x | 3.0 | 57% |

**Parameter contribution:** Standby Current (Iddq) 54%, Leakage Current (Ileak) 37%, Propagation Delay (tpd) 8%

**Top attribution features:** leakage drift z-score (+11.686); Iddq drift z-score (+11.652); Iddq z-score @24h (+5.858)

**Evidence:** Standby Current (Iddq) reads 83.64 µA at 24h against a lot median of 24.51 µA (3.41x lot median) and uses 84% of the 100 µA datasheet limit. Drift is +29.0% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 036 - SN02-0019 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.12 µA | 24.16 µA | 18.95 µA | 1.27x | 1.2 | 24% |
| Leakage Current (Ileak) | 46.24 µA | 46.42 µA | 6.95 µA | 6.68x | 15.1 | 93% |
| Propagation Delay (tpd) | 9.55 ns | 9.78 ns | 9.82 ns | 1.00x | 1.1 | 65% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 89%, Propagation Delay (tpd) 4%

**Top attribution features:** leakage z-score @0h (+15.109); leakage z-score @24h (+14.471); leakage drift z-score (+1.631)

**Evidence:** Leakage Current (Ileak) reads 46.42 µA at 24h against a lot median of 6.95 µA (6.68x lot median) and uses 93% of the 50 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +4.6%.

### Certificate 037 - SN08-0041 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.84 µA | 13.02 µA | 12.78 µA | 1.02x | 1.7 | 13% |
| Leakage Current (Ileak) | 27.06 µA | 31.37 µA | 5.03 µA | 6.24x | 13.0 | 63% |
| Propagation Delay (tpd) | 8.51 ns | 8.62 ns | 8.48 ns | 1.02x | 0.5 | 57% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 92%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage z-score @24h (+13.027); leakage z-score @0h (+10.946); leakage drift z-score (+6.274)

**Evidence:** Leakage Current (Ileak) reads 31.37 µA at 24h against a lot median of 5.03 µA (6.24x lot median) and uses 63% of the 50 µA datasheet limit. Drift is +16.0% versus a lot-median drift of +3.5%.

### Certificate 038 - SN03-0077 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 40.97 µA | 53.41 µA | 14.53 µA | 3.68x | 7.7 | 53% |
| Leakage Current (Ileak) | 11.78 µA | 15.33 µA | 8.19 µA | 1.87x | 11.7 | 31% |
| Propagation Delay (tpd) | 8.62 ns | 8.83 ns | 8.33 ns | 1.06x | 2.0 | 59% |

**Parameter contribution:** Standby Current (Iddq) 51%, Leakage Current (Ileak) 39%, Propagation Delay (tpd) 10%

**Top attribution features:** leakage drift z-score (+11.698); Iddq z-score @24h (+7.733); Iddq z-score @0h (+5.936)

**Evidence:** Standby Current (Iddq) reads 53.41 µA at 24h against a lot median of 14.53 µA (3.68x lot median) and uses 53% of the 100 µA datasheet limit. Drift is +30.4% versus a lot-median drift of +7.1%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 039 - SN03-0071 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.91 µA | 27.55 µA | 14.53 µA | 1.90x | 4.6 | 28% |
| Leakage Current (Ileak) | 14.34 µA | 21.16 µA | 8.19 µA | 2.58x | 19.7 | 42% |
| Propagation Delay (tpd) | 9.50 ns | 9.75 ns | 8.33 ns | 1.17x | 2.8 | 65% |

**Parameter contribution:** Standby Current (Iddq) 21%, Leakage Current (Ileak) 60%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage drift z-score (+19.654); Iddq drift z-score (+4.553); leakage z-score @24h (+3.727)

**Evidence:** Leakage Current (Ileak) reads 21.16 µA at 24h against a lot median of 8.19 µA (2.58x lot median) and uses 42% of the 50 µA datasheet limit. Drift is +47.6% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 040 - SN05-0090 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.60 µA | 21.18 µA | 21.74 µA | 0.97x | 0.9 | 21% |
| Leakage Current (Ileak) | 32.17 µA | 36.24 µA | 5.71 µA | 6.35x | 15.7 | 72% |
| Propagation Delay (tpd) | 9.06 ns | 9.13 ns | 8.87 ns | 1.03x | 0.6 | 61% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 93%, Propagation Delay (tpd) 4%

**Top attribution features:** leakage z-score @24h (+15.661); leakage z-score @0h (+15.317); leakage drift z-score (+1.653)

**Evidence:** Leakage Current (Ileak) reads 36.24 µA at 24h against a lot median of 5.71 µA (6.35x lot median) and uses 72% of the 50 µA datasheet limit. Drift is +12.7% versus a lot-median drift of +6.7%.

### Certificate 041 - SN08-0016 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 19.35 µA | 19.64 µA | 12.78 µA | 1.54x | 1.4 | 20% |
| Leakage Current (Ileak) | 32.38 µA | 35.72 µA | 5.03 µA | 7.11x | 15.2 | 71% |
| Propagation Delay (tpd) | 8.25 ns | 8.37 ns | 8.48 ns | 0.99x | 0.3 | 56% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 87%, Propagation Delay (tpd) 2%

**Top attribution features:** leakage z-score @24h (+15.174); leakage z-score @0h (+13.570); leakage drift z-score (+3.438)

**Evidence:** Leakage Current (Ileak) reads 35.72 µA at 24h against a lot median of 5.03 µA (7.11x lot median) and uses 71% of the 50 µA datasheet limit. Drift is +10.3% versus a lot-median drift of +3.5%.

### Certificate 042 - SN05-0112 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 1.000

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.60 µA | 23.08 µA | 21.74 µA | 1.06x | 1.8 | 23% |
| Leakage Current (Ileak) | 32.63 µA | 35.33 µA | 5.71 µA | 6.19x | 15.6 | 71% |
| Propagation Delay (tpd) | 9.14 ns | 9.27 ns | 8.87 ns | 1.04x | 0.7 | 62% |

**Parameter contribution:** Standby Current (Iddq) 6%, Leakage Current (Ileak) 89%, Propagation Delay (tpd) 5%

**Top attribution features:** leakage z-score @0h (+15.582); leakage z-score @24h (+15.199); Iddq drift z-score (+1.768)

**Evidence:** Leakage Current (Ileak) reads 35.33 µA at 24h against a lot median of 5.71 µA (6.19x lot median) and uses 71% of the 50 µA datasheet limit. Drift is +8.3% versus a lot-median drift of +6.7%.

### Certificate 043 - SN03-0218 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.97 µA | 14.53 µA | 14.53 µA | 1.00x | 1.2 | 15% |
| Leakage Current (Ileak) | 7.53 µA | 7.82 µA | 8.19 µA | 0.96x | 0.3 | 16% |
| Propagation Delay (tpd) | 10.91 ns | 11.91 ns | 8.33 ns | 1.43x | 11.9 | 79% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 2%, Propagation Delay (tpd) 93%

**Top attribution features:** delay drift z-score (+11.878); delay z-score @24h (+7.043); delay z-score @0h (+5.669)

**Evidence:** Propagation Delay (tpd) reads 11.91 ns at 24h against a lot median of 8.33 ns (1.43x lot median) and uses 79% of the 15 ns datasheet limit. Drift is +9.2% versus a lot-median drift of +1.1%.

### Certificate 044 - SN04-0249 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.60 µA | 42.20 µA | 17.67 µA | 2.39x | 9.6 | 42% |
| Leakage Current (Ileak) | 10.25 µA | 15.37 µA | 6.43 µA | 2.39x | 12.0 | 31% |
| Propagation Delay (tpd) | 10.07 ns | 10.68 ns | 10.33 ns | 1.03x | 5.6 | 71% |

**Parameter contribution:** Standby Current (Iddq) 41%, Leakage Current (Ileak) 43%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+11.970); Iddq drift z-score (+9.644); delay drift z-score (+5.552)

**Evidence:** Leakage Current (Ileak) reads 15.37 µA at 24h against a lot median of 6.43 µA (2.39x lot median) and uses 31% of the 50 µA datasheet limit. Drift is +50.0% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 045 - SN02-0195 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 94.54 µA | 94.92 µA | 18.95 µA | 5.01x | 17.3 | 95% |
| Leakage Current (Ileak) | 6.14 µA | 6.43 µA | 6.95 µA | 0.92x | 0.2 | 13% |
| Propagation Delay (tpd) | 9.55 ns | 9.70 ns | 9.82 ns | 0.99x | 0.2 | 65% |

**Parameter contribution:** Standby Current (Iddq) 98%, Leakage Current (Ileak) 1%, Propagation Delay (tpd) 1%

**Top attribution features:** Iddq z-score @0h (+17.341); Iddq z-score @24h (+14.263); Iddq drift z-score (+1.585)

**Evidence:** Standby Current (Iddq) reads 94.92 µA at 24h against a lot median of 18.95 µA (5.01x lot median) and uses 95% of the 100 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +6.1%.

### Certificate 046 - SN06-0166 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.36 µA | 21.75 µA | 21.75 µA | 1.00x | 0.5 | 22% |
| Leakage Current (Ileak) | 9.89 µA | 10.26 µA | 7.94 µA | 1.29x | 0.8 | 21% |
| Propagation Delay (tpd) | 12.92 ns | 13.40 ns | 9.80 ns | 1.37x | 7.1 | 89% |

**Parameter contribution:** Standby Current (Iddq) 2%, Leakage Current (Ileak) 9%, Propagation Delay (tpd) 89%

**Top attribution features:** delay z-score @24h (+7.121); delay z-score @0h (+6.506); delay drift z-score (+5.512)

**Evidence:** Propagation Delay (tpd) reads 13.40 ns at 24h against a lot median of 9.80 ns (1.37x lot median) and uses 89% of the 15 ns datasheet limit. Drift is +3.7% versus a lot-median drift of +0.8%.

### Certificate 047 - SN02-0140 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.14 µA | 25.59 µA | 18.95 µA | 1.35x | 1.2 | 26% |
| Leakage Current (Ileak) | 42.31 µA | 46.98 µA | 6.95 µA | 6.76x | 14.7 | 94% |
| Propagation Delay (tpd) | 9.70 ns | 9.87 ns | 9.82 ns | 1.00x | 0.3 | 66% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 88%, Propagation Delay (tpd) 1%

**Top attribution features:** leakage z-score @24h (+14.674); leakage z-score @0h (+13.613); leakage drift z-score (+2.469)

**Evidence:** Leakage Current (Ileak) reads 46.98 µA at 24h against a lot median of 6.95 µA (6.76x lot median) and uses 94% of the 50 µA datasheet limit. Drift is +11.0% versus a lot-median drift of +4.6%.

### Certificate 048 - SN07-0188 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.07 µA | 37.45 µA | 17.12 µA | 2.19x | 12.2 | 37% |
| Leakage Current (Ileak) | 24.38 µA | 31.95 µA | 10.67 µA | 3.00x | 10.5 | 64% |
| Propagation Delay (tpd) | 8.78 ns | 8.98 ns | 8.96 ns | 1.00x | 1.2 | 60% |

**Parameter contribution:** Standby Current (Iddq) 46%, Leakage Current (Ileak) 50%, Propagation Delay (tpd) 3%

**Top attribution features:** Iddq drift z-score (+12.244); leakage drift z-score (+10.492); leakage z-score @24h (+5.575)

**Evidence:** Leakage Current (Ileak) reads 31.95 µA at 24h against a lot median of 10.67 µA (3.00x lot median) and uses 64% of the 50 µA datasheet limit. Drift is +31.1% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 049 - SN03-0045 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.31 µA | 32.79 µA | 14.53 µA | 2.26x | 9.7 | 33% |
| Leakage Current (Ileak) | 12.96 µA | 18.26 µA | 8.19 µA | 2.23x | 16.7 | 37% |
| Propagation Delay (tpd) | 8.26 ns | 8.63 ns | 8.33 ns | 1.04x | 4.9 | 58% |

**Parameter contribution:** Standby Current (Iddq) 36%, Leakage Current (Ileak) 50%, Propagation Delay (tpd) 13%

**Top attribution features:** leakage drift z-score (+16.651); Iddq drift z-score (+9.749); delay drift z-score (+4.899)

**Evidence:** Leakage Current (Ileak) reads 18.26 µA at 24h against a lot median of 8.19 µA (2.23x lot median) and uses 37% of the 50 µA datasheet limit. Drift is +41.0% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 050 - SN03-0154 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 92.10 µA | 92.47 µA | 14.53 µA | 6.37x | 17.0 | 92% |
| Leakage Current (Ileak) | 7.53 µA | 7.71 µA | 8.19 µA | 0.94x | 0.9 | 15% |
| Propagation Delay (tpd) | 8.15 ns | 8.25 ns | 8.33 ns | 0.99x | 0.2 | 55% |

**Parameter contribution:** Standby Current (Iddq) 96%, Leakage Current (Ileak) 3%, Propagation Delay (tpd) 1%

**Top attribution features:** Iddq z-score @0h (+16.990); Iddq z-score @24h (+15.500); Iddq drift z-score (+1.646)

**Evidence:** Standby Current (Iddq) reads 92.47 µA at 24h against a lot median of 14.53 µA (6.37x lot median) and uses 92% of the 100 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +7.1%.

### Certificate 051 - SN02-0044 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 76.07 µA | 87.29 µA | 18.95 µA | 4.61x | 13.2 | 87% |
| Leakage Current (Ileak) | 5.98 µA | 6.72 µA | 6.95 µA | 0.97x | 3.0 | 13% |
| Propagation Delay (tpd) | 9.58 ns | 9.66 ns | 9.82 ns | 0.98x | 0.7 | 64% |

**Parameter contribution:** Standby Current (Iddq) 87%, Leakage Current (Ileak) 10%, Propagation Delay (tpd) 3%

**Top attribution features:** Iddq z-score @0h (+13.178); Iddq z-score @24h (+12.831); leakage drift z-score (+2.975)

**Evidence:** Standby Current (Iddq) reads 87.29 µA at 24h against a lot median of 18.95 µA (4.61x lot median) and uses 87% of the 100 µA datasheet limit. Drift is +14.7% versus a lot-median drift of +6.1%.

### Certificate 052 - SN01-0243 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 56.01 µA | 61.47 µA | 24.51 µA | 2.51x | 3.7 | 61% |
| Leakage Current (Ileak) | 47.52 µA | 47.71 µA | 9.64 µA | 4.95x | 10.2 | 95% |
| Propagation Delay (tpd) | 8.26 ns | 8.35 ns | 8.46 ns | 0.99x | 0.2 | 56% |

**Parameter contribution:** Standby Current (Iddq) 31%, Leakage Current (Ileak) 68%, Propagation Delay (tpd) 1%

**Top attribution features:** leakage z-score @0h (+10.214); leakage z-score @24h (+9.238); Iddq z-score @24h (+3.662)

**Evidence:** Leakage Current (Ileak) reads 47.71 µA at 24h against a lot median of 9.64 µA (4.95x lot median) and uses 95% of the 50 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 053 - SN02-0134 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 55.96 µA | 64.67 µA | 18.95 µA | 3.41x | 8.6 | 65% |
| Leakage Current (Ileak) | 5.98 µA | 6.91 µA | 6.95 µA | 0.99x | 4.2 | 14% |
| Propagation Delay (tpd) | 10.79 ns | 11.00 ns | 9.82 ns | 1.12x | 2.0 | 73% |

**Parameter contribution:** Standby Current (Iddq) 69%, Leakage Current (Ileak) 15%, Propagation Delay (tpd) 16%

**Top attribution features:** Iddq z-score @0h (+8.645); Iddq z-score @24h (+8.585); leakage drift z-score (+4.227)

**Evidence:** Standby Current (Iddq) reads 64.67 µA at 24h against a lot median of 18.95 µA (3.41x lot median) and uses 65% of the 100 µA datasheet limit. Drift is +15.6% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 054 - SN02-0254 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.999

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 16.92 µA | 18.95 µA | 0.89x | 1.0 | 17% |
| Leakage Current (Ileak) | 6.26 µA | 6.48 µA | 6.95 µA | 0.93x | 0.5 | 13% |
| Propagation Delay (tpd) | 13.43 ns | 14.31 ns | 9.82 ns | 1.46x | 7.0 | 95% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 3%, Propagation Delay (tpd) 89%

**Top attribution features:** delay z-score @24h (+7.013); delay z-score @0h (+6.675); delay drift z-score (+5.952)

**Evidence:** Propagation Delay (tpd) reads 14.31 ns at 24h against a lot median of 9.82 ns (1.46x lot median) and uses 95% of the 15 ns datasheet limit. Drift is +6.5% versus a lot-median drift of +1.4%.

### Certificate 055 - SN08-0181 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.65 µA | 23.07 µA | 12.78 µA | 1.81x | 9.3 | 23% |
| Leakage Current (Ileak) | 6.67 µA | 9.01 µA | 5.03 µA | 1.79x | 15.9 | 18% |
| Propagation Delay (tpd) | 9.01 ns | 9.36 ns | 8.48 ns | 1.10x | 3.2 | 62% |

**Parameter contribution:** Standby Current (Iddq) 31%, Leakage Current (Ileak) 49%, Propagation Delay (tpd) 20%

**Top attribution features:** leakage drift z-score (+15.895); Iddq drift z-score (+9.279); delay drift z-score (+3.248)

**Evidence:** Leakage Current (Ileak) reads 9.01 µA at 24h against a lot median of 5.03 µA (1.79x lot median) and uses 18% of the 50 µA datasheet limit. Drift is +35.1% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 056 - SN01-0177 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.60 µA | 24.01 µA | 24.51 µA | 0.98x | 1.0 | 24% |
| Leakage Current (Ileak) | 47.51 µA | 47.70 µA | 9.64 µA | 4.95x | 10.2 | 95% |
| Propagation Delay (tpd) | 9.35 ns | 9.40 ns | 8.46 ns | 1.11x | 2.2 | 63% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 78%, Propagation Delay (tpd) 18%

**Top attribution features:** leakage z-score @0h (+10.210); leakage z-score @24h (+9.235); delay z-score @0h (+2.164)

**Evidence:** Leakage Current (Ileak) reads 47.70 µA at 24h against a lot median of 9.64 µA (4.95x lot median) and uses 95% of the 50 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +5.1%.

### Certificate 057 - SN05-0103 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 33.02 µA | 45.22 µA | 21.74 µA | 2.08x | 8.9 | 45% |
| Leakage Current (Ileak) | 8.16 µA | 11.52 µA | 5.71 µA | 2.02x | 9.6 | 23% |
| Propagation Delay (tpd) | 9.43 ns | 9.86 ns | 8.87 ns | 1.11x | 5.3 | 66% |

**Parameter contribution:** Standby Current (Iddq) 40%, Leakage Current (Ileak) 38%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage drift z-score (+9.563); Iddq drift z-score (+8.915); delay drift z-score (+5.298)

**Evidence:** Standby Current (Iddq) reads 45.22 µA at 24h against a lot median of 21.74 µA (2.08x lot median) and uses 45% of the 100 µA datasheet limit. Drift is +36.9% versus a lot-median drift of +5.9%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 058 - SN01-0251 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 36.55 µA | 47.45 µA | 24.51 µA | 1.94x | 12.0 | 47% |
| Leakage Current (Ileak) | 14.04 µA | 17.69 µA | 9.64 µA | 1.84x | 7.2 | 35% |
| Propagation Delay (tpd) | 9.67 ns | 9.87 ns | 8.46 ns | 1.17x | 2.9 | 66% |

**Parameter contribution:** Standby Current (Iddq) 47%, Leakage Current (Ileak) 31%, Propagation Delay (tpd) 22%

**Top attribution features:** Iddq drift z-score (+12.045); leakage drift z-score (+7.225); delay z-score @0h (+2.853)

**Evidence:** Standby Current (Iddq) reads 47.45 µA at 24h against a lot median of 24.51 µA (1.94x lot median) and uses 47% of the 100 µA datasheet limit. Drift is +29.8% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 059 - SN04-0231 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 30.87 µA | 38.53 µA | 17.67 µA | 2.18x | 7.9 | 39% |
| Leakage Current (Ileak) | 10.16 µA | 15.06 µA | 6.43 µA | 2.34x | 11.5 | 30% |
| Propagation Delay (tpd) | 10.02 ns | 10.58 ns | 10.33 ns | 1.02x | 5.1 | 71% |

**Parameter contribution:** Standby Current (Iddq) 38%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+11.489); Iddq drift z-score (+7.859); delay drift z-score (+5.063)

**Evidence:** Leakage Current (Ileak) reads 15.06 µA at 24h against a lot median of 6.43 µA (2.34x lot median) and uses 30% of the 50 µA datasheet limit. Drift is +48.2% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 060 - SN05-0082 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 24.07 µA | 25.10 µA | 21.74 µA | 1.15x | 0.6 | 25% |
| Leakage Current (Ileak) | 11.48 µA | 12.35 µA | 5.71 µA | 2.16x | 3.5 | 25% |
| Propagation Delay (tpd) | 11.52 ns | 11.86 ns | 8.87 ns | 1.34x | 5.4 | 79% |

**Parameter contribution:** Standby Current (Iddq) 7%, Leakage Current (Ileak) 32%, Propagation Delay (tpd) 60%

**Top attribution features:** delay z-score @24h (+5.391); delay z-score @0h (+5.055); leakage z-score @0h (+3.499)

**Evidence:** Propagation Delay (tpd) reads 11.86 ns at 24h against a lot median of 8.87 ns (1.34x lot median) and uses 79% of the 15 ns datasheet limit. Drift is +2.9% versus a lot-median drift of +1.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 061 - SN07-0098 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 73.47 µA | 77.48 µA | 17.12 µA | 4.53x | 12.0 | 77% |
| Leakage Current (Ileak) | 10.70 µA | 12.14 µA | 10.67 µA | 1.14x | 3.4 | 24% |
| Propagation Delay (tpd) | 8.86 ns | 9.04 ns | 8.96 ns | 1.01x | 0.9 | 60% |

**Parameter contribution:** Standby Current (Iddq) 83%, Leakage Current (Ileak) 14%, Propagation Delay (tpd) 4%

**Top attribution features:** Iddq z-score @0h (+12.028); Iddq z-score @24h (+11.899); leakage drift z-score (+3.402)

**Evidence:** Standby Current (Iddq) reads 77.48 µA at 24h against a lot median of 17.12 µA (4.53x lot median) and uses 77% of the 100 µA datasheet limit. Drift is +5.5% versus a lot-median drift of +5.2%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 062 - SN08-0171 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 89.69 µA | 92.23 µA | 12.78 µA | 7.22x | 14.6 | 92% |
| Leakage Current (Ileak) | 4.75 µA | 4.89 µA | 5.03 µA | 0.97x | 0.3 | 10% |
| Propagation Delay (tpd) | 8.25 ns | 8.39 ns | 8.48 ns | 0.99x | 0.5 | 56% |

**Parameter contribution:** Standby Current (Iddq) 95%, Leakage Current (Ileak) 1%, Propagation Delay (tpd) 3%

**Top attribution features:** Iddq z-score @0h (+14.619); Iddq z-score @24h (+13.711); Iddq drift z-score (+0.850)

**Evidence:** Standby Current (Iddq) reads 92.23 µA at 24h against a lot median of 12.78 µA (7.22x lot median) and uses 92% of the 100 µA datasheet limit. Drift is +2.8% versus a lot-median drift of +5.2%.

### Certificate 063 - SN03-0224 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.998

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 19.65 µA | 25.67 µA | 14.53 µA | 1.77x | 5.7 | 26% |
| Leakage Current (Ileak) | 14.43 µA | 20.02 µA | 8.19 µA | 2.45x | 15.6 | 40% |
| Propagation Delay (tpd) | 8.29 ns | 8.65 ns | 8.33 ns | 1.04x | 4.9 | 58% |

**Parameter contribution:** Standby Current (Iddq) 26%, Leakage Current (Ileak) 58%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+15.648); Iddq drift z-score (+5.749); delay drift z-score (+4.913)

**Evidence:** Leakage Current (Ileak) reads 20.02 µA at 24h against a lot median of 8.19 µA (2.45x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +38.8% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 064 - SN03-0167 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.997

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 19.76 µA | 20.62 µA | 14.53 µA | 1.42x | 1.4 | 21% |
| Leakage Current (Ileak) | 9.90 µA | 10.18 µA | 8.19 µA | 1.24x | 0.7 | 20% |
| Propagation Delay (tpd) | 10.48 ns | 11.09 ns | 8.33 ns | 1.33x | 6.9 | 74% |

**Parameter contribution:** Standby Current (Iddq) 15%, Leakage Current (Ileak) 9%, Propagation Delay (tpd) 77%

**Top attribution features:** delay drift z-score (+6.933); delay z-score @24h (+5.430); delay z-score @0h (+4.768)

**Evidence:** Propagation Delay (tpd) reads 11.09 ns at 24h against a lot median of 8.33 ns (1.33x lot median) and uses 74% of the 15 ns datasheet limit. Drift is +5.8% versus a lot-median drift of +1.1%.

### Certificate 065 - SN02-0071 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.997

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 17.92 µA | 18.95 µA | 0.95x | 0.6 | 18% |
| Leakage Current (Ileak) | 5.98 µA | 6.30 µA | 6.95 µA | 0.91x | 0.3 | 13% |
| Propagation Delay (tpd) | 12.77 ns | 13.86 ns | 9.82 ns | 1.41x | 8.3 | 92% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 3%, Propagation Delay (tpd) 92%

**Top attribution features:** delay drift z-score (+8.294); delay z-score @24h (+6.318); delay z-score @0h (+5.509)

**Evidence:** Propagation Delay (tpd) reads 13.86 ns at 24h against a lot median of 9.82 ns (1.41x lot median) and uses 92% of the 15 ns datasheet limit. Drift is +8.5% versus a lot-median drift of +1.4%.

### Certificate 066 - SN04-0087 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.997

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.37 µA | 38.17 µA | 17.67 µA | 2.16x | 9.8 | 38% |
| Leakage Current (Ileak) | 15.08 µA | 21.41 µA | 6.43 µA | 3.33x | 9.8 | 43% |
| Propagation Delay (tpd) | 10.07 ns | 10.44 ns | 10.33 ns | 1.01x | 2.7 | 70% |

**Parameter contribution:** Standby Current (Iddq) 41%, Leakage Current (Ileak) 50%, Propagation Delay (tpd) 8%

**Top attribution features:** Iddq drift z-score (+9.847); leakage drift z-score (+9.758); leakage z-score @24h (+5.306)

**Evidence:** Leakage Current (Ileak) reads 21.41 µA at 24h against a lot median of 6.43 µA (3.33x lot median) and uses 43% of the 50 µA datasheet limit. Drift is +41.9% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 067 - SN02-0183 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.997

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.13 µA | 36.49 µA | 18.95 µA | 1.93x | 10.8 | 36% |
| Leakage Current (Ileak) | 9.13 µA | 13.40 µA | 6.95 µA | 1.93x | 16.2 | 27% |
| Propagation Delay (tpd) | 9.69 ns | 9.94 ns | 9.82 ns | 1.01x | 1.4 | 66% |

**Parameter contribution:** Standby Current (Iddq) 43%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 4%

**Top attribution features:** leakage drift z-score (+16.217); Iddq drift z-score (+10.807); Iddq z-score @24h (+3.292)

**Evidence:** Leakage Current (Ileak) reads 13.40 µA at 24h against a lot median of 6.95 µA (1.93x lot median) and uses 27% of the 50 µA datasheet limit. Drift is +46.7% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 068 - SN02-0232 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.997

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 24.50 µA | 26.26 µA | 18.95 µA | 1.39x | 1.6 | 26% |
| Leakage Current (Ileak) | 10.92 µA | 11.59 µA | 6.95 µA | 1.67x | 1.7 | 23% |
| Propagation Delay (tpd) | 13.79 ns | 13.84 ns | 9.82 ns | 1.41x | 7.3 | 92% |

**Parameter contribution:** Standby Current (Iddq) 15%, Leakage Current (Ileak) 18%, Propagation Delay (tpd) 67%

**Top attribution features:** delay z-score @0h (+7.310); delay z-score @24h (+6.288); leakage z-score @24h (+1.702)

**Evidence:** Propagation Delay (tpd) reads 13.84 ns at 24h against a lot median of 9.82 ns (1.41x lot median) and uses 92% of the 15 ns datasheet limit. Drift is +0.4% versus a lot-median drift of +1.4%.

### Certificate 069 - SN03-0050 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.996

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.90 µA | 26.42 µA | 14.53 µA | 1.82x | 8.0 | 26% |
| Leakage Current (Ileak) | 13.49 µA | 17.49 µA | 8.19 µA | 2.14x | 11.5 | 35% |
| Propagation Delay (tpd) | 9.39 ns | 9.63 ns | 8.33 ns | 1.16x | 2.6 | 64% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 21%

**Top attribution features:** leakage drift z-score (+11.507); Iddq drift z-score (+7.985); leakage z-score @24h (+2.674)

**Evidence:** Leakage Current (Ileak) reads 17.49 µA at 24h against a lot median of 8.19 µA (2.14x lot median) and uses 35% of the 50 µA datasheet limit. Drift is +29.7% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 070 - SN03-0016 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.996

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 55.10 µA | 70.02 µA | 14.53 µA | 4.82x | 11.0 | 70% |
| Leakage Current (Ileak) | 10.92 µA | 11.32 µA | 8.19 µA | 1.38x | 0.9 | 23% |
| Propagation Delay (tpd) | 8.12 ns | 8.16 ns | 8.33 ns | 0.98x | 0.9 | 54% |

**Parameter contribution:** Standby Current (Iddq) 87%, Leakage Current (Ileak) 7%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq z-score @24h (+11.036); Iddq z-score @0h (+8.991); Iddq drift z-score (+4.882)

**Evidence:** Standby Current (Iddq) reads 70.02 µA at 24h against a lot median of 14.53 µA (4.82x lot median) and uses 70% of the 100 µA datasheet limit. Drift is +27.1% versus a lot-median drift of +7.1%.

### Certificate 071 - SN02-0124 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.996

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.59 µA | 36.31 µA | 18.95 µA | 1.92x | 9.9 | 36% |
| Leakage Current (Ileak) | 8.24 µA | 11.71 µA | 6.95 µA | 1.69x | 14.4 | 23% |
| Propagation Delay (tpd) | 10.16 ns | 10.57 ns | 9.82 ns | 1.08x | 3.1 | 70% |

**Parameter contribution:** Standby Current (Iddq) 41%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage drift z-score (+14.442); Iddq drift z-score (+9.903); Iddq z-score @24h (+3.260)

**Evidence:** Leakage Current (Ileak) reads 11.71 µA at 24h against a lot median of 6.95 µA (1.69x lot median) and uses 23% of the 50 µA datasheet limit. Drift is +42.1% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 072 - SN07-0141 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.996

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 15.94 µA | 17.25 µA | 17.12 µA | 1.01x | 1.0 | 17% |
| Leakage Current (Ileak) | 10.05 µA | 10.92 µA | 10.67 µA | 1.02x | 1.5 | 22% |
| Propagation Delay (tpd) | 11.87 ns | 12.38 ns | 8.96 ns | 1.38x | 7.4 | 83% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 8%, Propagation Delay (tpd) 88%

**Top attribution features:** delay z-score @24h (+7.372); delay z-score @0h (+6.987); delay drift z-score (+3.735)

**Evidence:** Propagation Delay (tpd) reads 12.38 ns at 24h against a lot median of 8.96 ns (1.38x lot median) and uses 83% of the 15 ns datasheet limit. Drift is +4.3% versus a lot-median drift of +1.4%.

### Certificate 073 - SN06-0136 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.996

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 34.84 µA | 44.55 µA | 21.75 µA | 2.05x | 7.2 | 45% |
| Leakage Current (Ileak) | 13.26 µA | 17.35 µA | 7.94 µA | 2.18x | 10.2 | 35% |
| Propagation Delay (tpd) | 9.73 ns | 10.09 ns | 9.80 ns | 1.03x | 5.5 | 67% |

**Parameter contribution:** Standby Current (Iddq) 35%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 18%

**Top attribution features:** leakage drift z-score (+10.247); Iddq drift z-score (+7.210); delay drift z-score (+5.519)

**Evidence:** Leakage Current (Ileak) reads 17.35 µA at 24h against a lot median of 7.94 µA (2.18x lot median) and uses 35% of the 50 µA datasheet limit. Drift is +30.8% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 074 - SN07-0205 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.995

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 28.93 µA | 38.79 µA | 17.12 µA | 2.27x | 9.2 | 39% |
| Leakage Current (Ileak) | 15.65 µA | 21.36 µA | 10.67 µA | 2.00x | 12.7 | 43% |
| Propagation Delay (tpd) | 8.88 ns | 9.19 ns | 8.96 ns | 1.02x | 2.6 | 61% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 47%, Propagation Delay (tpd) 9%

**Top attribution features:** leakage drift z-score (+12.692); Iddq drift z-score (+9.190); Iddq z-score @24h (+4.271)

**Evidence:** Leakage Current (Ileak) reads 21.36 µA at 24h against a lot median of 10.67 µA (2.00x lot median) and uses 43% of the 50 µA datasheet limit. Drift is +36.5% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 075 - SN02-0017 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.995

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.81 µA | 24.27 µA | 18.95 µA | 1.28x | 1.4 | 24% |
| Leakage Current (Ileak) | 36.17 µA | 40.16 µA | 6.95 µA | 5.78x | 12.2 | 80% |
| Propagation Delay (tpd) | 9.55 ns | 9.66 ns | 9.82 ns | 0.98x | 0.3 | 64% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 86%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage z-score @24h (+12.175); leakage z-score @0h (+11.280); leakage drift z-score (+2.468)

**Evidence:** Leakage Current (Ileak) reads 40.16 µA at 24h against a lot median of 6.95 µA (5.78x lot median) and uses 80% of the 50 µA datasheet limit. Drift is +11.0% versus a lot-median drift of +4.6%.

### Certificate 076 - SN02-0088 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.993

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 63.16 µA | 70.15 µA | 18.95 µA | 3.70x | 10.3 | 70% |
| Leakage Current (Ileak) | 6.30 µA | 6.99 µA | 6.95 µA | 1.01x | 2.5 | 14% |
| Propagation Delay (tpd) | 9.55 ns | 9.88 ns | 9.82 ns | 1.01x | 2.3 | 66% |

**Parameter contribution:** Standby Current (Iddq) 80%, Leakage Current (Ileak) 10%, Propagation Delay (tpd) 10%

**Top attribution features:** Iddq z-score @0h (+10.269); Iddq z-score @24h (+9.612); leakage drift z-score (+2.462)

**Evidence:** Standby Current (Iddq) reads 70.15 µA at 24h against a lot median of 18.95 µA (3.70x lot median) and uses 70% of the 100 µA datasheet limit. Drift is +11.1% versus a lot-median drift of +6.1%.

### Certificate 077 - SN02-0206 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.993

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 64.50 µA | 70.27 µA | 18.95 µA | 3.71x | 10.6 | 70% |
| Leakage Current (Ileak) | 5.98 µA | 6.13 µA | 6.95 µA | 0.88x | 0.8 | 12% |
| Propagation Delay (tpd) | 10.78 ns | 10.86 ns | 9.82 ns | 1.11x | 2.0 | 72% |

**Parameter contribution:** Standby Current (Iddq) 79%, Leakage Current (Ileak) 5%, Propagation Delay (tpd) 17%

**Top attribution features:** Iddq z-score @0h (+10.570); Iddq z-score @24h (+9.635); delay z-score @0h (+1.983)

**Evidence:** Standby Current (Iddq) reads 70.27 µA at 24h against a lot median of 18.95 µA (3.71x lot median) and uses 70% of the 100 µA datasheet limit. Drift is +8.9% versus a lot-median drift of +6.1%.

### Certificate 078 - SN03-0133 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.993

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 14.34 µA | 15.61 µA | 14.53 µA | 1.07x | 0.4 | 16% |
| Leakage Current (Ileak) | 37.19 µA | 43.80 µA | 8.19 µA | 5.35x | 10.2 | 88% |
| Propagation Delay (tpd) | 8.12 ns | 8.17 ns | 8.33 ns | 0.98x | 0.7 | 54% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 92%, Propagation Delay (tpd) 5%

**Top attribution features:** leakage z-score @24h (+10.235); leakage z-score @0h (+8.853); leakage drift z-score (+6.089)

**Evidence:** Leakage Current (Ileak) reads 43.80 µA at 24h against a lot median of 8.19 µA (5.35x lot median) and uses 88% of the 50 µA datasheet limit. Drift is +17.8% versus a lot-median drift of +4.4%.

### Certificate 079 - SN03-0212 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.993

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.54 µA | 24.44 µA | 14.53 µA | 1.68x | 7.9 | 24% |
| Leakage Current (Ileak) | 11.07 µA | 14.28 µA | 8.19 µA | 1.74x | 11.2 | 29% |
| Propagation Delay (tpd) | 9.22 ns | 9.47 ns | 8.33 ns | 1.14x | 2.4 | 63% |

**Parameter contribution:** Standby Current (Iddq) 34%, Leakage Current (Ileak) 44%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage drift z-score (+11.197); Iddq drift z-score (+7.889); delay drift z-score (+2.446)

**Evidence:** Leakage Current (Ileak) reads 14.28 µA at 24h against a lot median of 8.19 µA (1.74x lot median) and uses 29% of the 50 µA datasheet limit. Drift is +29.0% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 080 - SN08-0151 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.993

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 56.79 µA | 67.72 µA | 12.78 µA | 5.30x | 9.5 | 68% |
| Leakage Current (Ileak) | 6.29 µA | 6.56 µA | 5.03 µA | 1.31x | 0.8 | 13% |
| Propagation Delay (tpd) | 8.25 ns | 8.30 ns | 8.48 ns | 0.98x | 0.9 | 55% |

**Parameter contribution:** Standby Current (Iddq) 87%, Leakage Current (Ileak) 7%, Propagation Delay (tpd) 6%

**Top attribution features:** Iddq z-score @24h (+9.481); Iddq z-score @0h (+8.430); Iddq drift z-score (+5.099)

**Evidence:** Standby Current (Iddq) reads 67.72 µA at 24h against a lot median of 12.78 µA (5.30x lot median) and uses 68% of the 100 µA datasheet limit. Drift is +19.2% versus a lot-median drift of +5.2%.

### Certificate 081 - SN07-0029 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.991

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.97 µA | 27.22 µA | 17.12 µA | 1.59x | 5.9 | 27% |
| Leakage Current (Ileak) | 15.05 µA | 20.03 µA | 10.67 µA | 1.88x | 11.3 | 40% |
| Propagation Delay (tpd) | 9.40 ns | 9.85 ns | 8.96 ns | 1.10x | 4.3 | 66% |

**Parameter contribution:** Standby Current (Iddq) 29%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 24%

**Top attribution features:** leakage drift z-score (+11.293); Iddq drift z-score (+5.937); delay drift z-score (+4.251)

**Evidence:** Leakage Current (Ileak) reads 20.03 µA at 24h against a lot median of 10.67 µA (1.88x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +33.0% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 082 - SN01-0004 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.991

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 62.05 µA | 79.06 µA | 24.51 µA | 3.23x | 10.9 | 79% |
| Leakage Current (Ileak) | 17.01 µA | 19.98 µA | 9.64 µA | 2.07x | 4.3 | 40% |
| Propagation Delay (tpd) | 8.37 ns | 8.53 ns | 8.46 ns | 1.01x | 1.2 | 57% |

**Parameter contribution:** Standby Current (Iddq) 66%, Leakage Current (Ileak) 29%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq drift z-score (+10.923); Iddq z-score @24h (+5.405); leakage drift z-score (+4.275)

**Evidence:** Standby Current (Iddq) reads 79.06 µA at 24h against a lot median of 24.51 µA (3.23x lot median) and uses 79% of the 100 µA datasheet limit. Drift is +27.4% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 083 - SN03-0140 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.991

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 56.49 µA | 67.49 µA | 14.53 µA | 4.65x | 10.5 | 67% |
| Leakage Current (Ileak) | 7.53 µA | 7.72 µA | 8.19 µA | 0.94x | 0.9 | 15% |
| Propagation Delay (tpd) | 8.12 ns | 8.17 ns | 8.33 ns | 0.98x | 0.8 | 54% |

**Parameter contribution:** Standby Current (Iddq) 91%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq z-score @24h (+10.532); Iddq z-score @0h (+9.290); Iddq drift z-score (+3.022)

**Evidence:** Standby Current (Iddq) reads 67.49 µA at 24h against a lot median of 14.53 µA (4.65x lot median) and uses 67% of the 100 µA datasheet limit. Drift is +19.5% versus a lot-median drift of +7.1%.

### Certificate 084 - SN08-0034 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.991

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.90 µA | 13.85 µA | 12.78 µA | 1.08x | 0.8 | 14% |
| Leakage Current (Ileak) | 16.22 µA | 19.36 µA | 5.03 µA | 3.85x | 8.0 | 39% |
| Propagation Delay (tpd) | 8.25 ns | 8.66 ns | 8.48 ns | 1.02x | 4.4 | 58% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 77%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage drift z-score (+7.982); leakage z-score @24h (+7.087); leakage z-score @0h (+5.602)

**Evidence:** Leakage Current (Ileak) reads 19.36 µA at 24h against a lot median of 5.03 µA (3.85x lot median) and uses 39% of the 50 µA datasheet limit. Drift is +19.4% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Propagation Delay (tpd).

### Certificate 085 - SN02-0152 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.990

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 33.88 µA | 41.47 µA | 18.95 µA | 2.19x | 4.5 | 41% |
| Leakage Current (Ileak) | 13.94 µA | 14.79 µA | 6.95 µA | 2.13x | 2.9 | 30% |
| Propagation Delay (tpd) | 8.37 ns | 8.40 ns | 9.82 ns | 0.86x | 2.3 | 56% |

**Parameter contribution:** Standby Current (Iddq) 51%, Leakage Current (Ileak) 26%, Propagation Delay (tpd) 23%

**Top attribution features:** Iddq drift z-score (+4.508); Iddq z-score @24h (+4.228); Iddq z-score @0h (+3.668)

**Evidence:** Standby Current (Iddq) reads 41.47 µA at 24h against a lot median of 18.95 µA (2.19x lot median) and uses 41% of the 100 µA datasheet limit. Drift is +22.4% versus a lot-median drift of +6.1%.

### Certificate 086 - SN06-0117 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.990

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 45.56 µA | 53.23 µA | 21.75 µA | 2.45x | 3.8 | 53% |
| Leakage Current (Ileak) | 20.91 µA | 21.83 µA | 7.94 µA | 2.75x | 4.7 | 44% |
| Propagation Delay (tpd) | 8.75 ns | 8.79 ns | 9.80 ns | 0.90x | 2.0 | 59% |

**Parameter contribution:** Standby Current (Iddq) 43%, Leakage Current (Ileak) 38%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage z-score @24h (+4.672); leakage z-score @0h (+4.668); Iddq z-score @24h (+3.775)

**Evidence:** Standby Current (Iddq) reads 53.23 µA at 24h against a lot median of 21.75 µA (2.45x lot median) and uses 53% of the 100 µA datasheet limit. Drift is +16.8% versus a lot-median drift of +5.3%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 087 - SN04-0270 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.989

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.38 µA | 18.98 µA | 17.67 µA | 1.07x | 0.5 | 19% |
| Leakage Current (Ileak) | 26.81 µA | 34.04 µA | 6.43 µA | 5.30x | 9.8 | 68% |
| Propagation Delay (tpd) | 10.69 ns | 10.93 ns | 10.33 ns | 1.06x | 1.0 | 73% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 87%, Propagation Delay (tpd) 10%

**Top attribution features:** leakage z-score @24h (+9.782); leakage z-score @0h (+8.113); leakage drift z-score (+5.643)

**Evidence:** Leakage Current (Ileak) reads 34.04 µA at 24h against a lot median of 6.43 µA (5.30x lot median) and uses 68% of the 50 µA datasheet limit. Drift is +27.0% versus a lot-median drift of +6.5%.

### Certificate 088 - SN03-0259 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.989

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.33 µA | 23.82 µA | 14.53 µA | 1.64x | 7.4 | 24% |
| Leakage Current (Ileak) | 13.53 µA | 18.78 µA | 8.19 µA | 2.29x | 15.7 | 38% |
| Propagation Delay (tpd) | 8.31 ns | 8.54 ns | 8.33 ns | 1.03x | 2.5 | 57% |

**Parameter contribution:** Standby Current (Iddq) 30%, Leakage Current (Ileak) 61%, Propagation Delay (tpd) 9%

**Top attribution features:** leakage drift z-score (+15.691); Iddq drift z-score (+7.408); leakage z-score @24h (+3.045)

**Evidence:** Leakage Current (Ileak) reads 18.78 µA at 24h against a lot median of 8.19 µA (2.29x lot median) and uses 38% of the 50 µA datasheet limit. Drift is +38.8% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 089 - SN01-0159 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.989

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 40.69 µA | 49.39 µA | 24.51 µA | 2.02x | 8.1 | 49% |
| Leakage Current (Ileak) | 23.79 µA | 31.53 µA | 9.64 µA | 3.27x | 9.5 | 63% |
| Propagation Delay (tpd) | 8.36 ns | 8.58 ns | 8.46 ns | 1.01x | 2.3 | 57% |

**Parameter contribution:** Standby Current (Iddq) 37%, Leakage Current (Ileak) 56%, Propagation Delay (tpd) 8%

**Top attribution features:** leakage drift z-score (+9.465); Iddq drift z-score (+8.135); leakage z-score @24h (+5.312)

**Evidence:** Leakage Current (Ileak) reads 31.53 µA at 24h against a lot median of 9.64 µA (3.27x lot median) and uses 63% of the 50 µA datasheet limit. Drift is +32.5% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 090 - SN08-0029 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.989

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 58.42 µA | 65.26 µA | 12.78 µA | 5.11x | 9.1 | 65% |
| Leakage Current (Ileak) | 4.65 µA | 4.89 µA | 5.03 µA | 0.97x | 0.8 | 10% |
| Propagation Delay (tpd) | 8.77 ns | 8.86 ns | 8.48 ns | 1.05x | 1.3 | 59% |

**Parameter contribution:** Standby Current (Iddq) 84%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 11%

**Top attribution features:** Iddq z-score @24h (+9.056); Iddq z-score @0h (+8.736); Iddq drift z-score (+2.371)

**Evidence:** Standby Current (Iddq) reads 65.26 µA at 24h against a lot median of 12.78 µA (5.11x lot median) and uses 65% of the 100 µA datasheet limit. Drift is +11.7% versus a lot-median drift of +5.2%.

### Certificate 091 - SN08-0073 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.987

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.27 µA | 18.24 µA | 12.78 µA | 1.43x | 2.5 | 18% |
| Leakage Current (Ileak) | 21.45 µA | 23.81 µA | 5.03 µA | 4.74x | 9.3 | 48% |
| Propagation Delay (tpd) | 8.32 ns | 8.40 ns | 8.48 ns | 0.99x | 0.3 | 56% |

**Parameter contribution:** Standby Current (Iddq) 16%, Leakage Current (Ileak) 82%, Propagation Delay (tpd) 2%

**Top attribution features:** leakage z-score @24h (+9.289); leakage z-score @0h (+8.183); leakage drift z-score (+3.779)

**Evidence:** Leakage Current (Ileak) reads 23.81 µA at 24h against a lot median of 5.03 µA (4.74x lot median) and uses 48% of the 50 µA datasheet limit. Drift is +11.0% versus a lot-median drift of +3.5%.

### Certificate 092 - SN05-0100 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.986

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.61 µA | 23.30 µA | 21.74 µA | 1.07x | 0.8 | 23% |
| Leakage Current (Ileak) | 24.39 µA | 27.05 µA | 5.71 µA | 4.74x | 11.0 | 54% |
| Propagation Delay (tpd) | 8.73 ns | 8.82 ns | 8.87 ns | 0.99x | 0.1 | 59% |

**Parameter contribution:** Standby Current (Iddq) 6%, Leakage Current (Ileak) 94%, Propagation Delay (tpd) 1%

**Top attribution features:** leakage z-score @24h (+10.950); leakage z-score @0h (+10.873); leakage drift z-score (+1.176)

**Evidence:** Leakage Current (Ileak) reads 27.05 µA at 24h against a lot median of 5.71 µA (4.74x lot median) and uses 54% of the 50 µA datasheet limit. Drift is +10.9% versus a lot-median drift of +6.7%.

### Certificate 093 - SN01-0007 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.984

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.60 µA | 24.02 µA | 24.51 µA | 0.98x | 0.9 | 24% |
| Leakage Current (Ileak) | 46.58 µA | 46.77 µA | 9.64 µA | 4.85x | 10.0 | 94% |
| Propagation Delay (tpd) | 8.26 ns | 8.38 ns | 8.46 ns | 0.99x | 0.4 | 56% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 92%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage z-score @0h (+9.965); leakage z-score @24h (+9.009); leakage drift z-score (+1.613)

**Evidence:** Leakage Current (Ileak) reads 46.77 µA at 24h against a lot median of 9.64 µA (4.85x lot median) and uses 94% of the 50 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +5.1%.

### Certificate 094 - SN06-0107 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.984

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.72 µA | 28.65 µA | 21.75 µA | 1.32x | 0.8 | 29% |
| Leakage Current (Ileak) | 34.12 µA | 37.79 µA | 7.94 µA | 4.76x | 10.0 | 76% |
| Propagation Delay (tpd) | 9.58 ns | 9.75 ns | 9.80 ns | 0.99x | 1.9 | 65% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 83%, Propagation Delay (tpd) 9%

**Top attribution features:** leakage z-score @24h (+10.043); leakage z-score @0h (+9.314); leakage drift z-score (+2.444)

**Evidence:** Leakage Current (Ileak) reads 37.79 µA at 24h against a lot median of 7.94 µA (4.76x lot median) and uses 76% of the 50 µA datasheet limit. Drift is +10.7% versus a lot-median drift of +4.4%.

### Certificate 095 - SN05-0053 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.984

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.43 µA | 35.73 µA | 21.74 µA | 1.64x | 2.3 | 36% |
| Leakage Current (Ileak) | 14.79 µA | 15.86 µA | 5.71 µA | 2.78x | 5.4 | 32% |
| Propagation Delay (tpd) | 7.32 ns | 7.46 ns | 8.87 ns | 0.84x | 2.6 | 50% |

**Parameter contribution:** Standby Current (Iddq) 25%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 28%

**Top attribution features:** leakage z-score @0h (+5.388); leakage z-score @24h (+5.209); delay z-score @0h (+2.568)

**Evidence:** Leakage Current (Ileak) reads 15.86 µA at 24h against a lot median of 5.71 µA (2.78x lot median) and uses 32% of the 50 µA datasheet limit. Drift is +7.3% versus a lot-median drift of +6.7%.

### Certificate 096 - SN08-0015 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.984

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 28.73 µA | 38.01 µA | 12.78 µA | 2.98x | 9.8 | 38% |
| Leakage Current (Ileak) | 7.26 µA | 9.01 µA | 5.03 µA | 1.79x | 10.4 | 18% |
| Propagation Delay (tpd) | 8.34 ns | 8.45 ns | 8.48 ns | 1.00x | 0.1 | 56% |

**Parameter contribution:** Standby Current (Iddq) 56%, Leakage Current (Ileak) 44%, Propagation Delay (tpd) 0%

**Top attribution features:** leakage drift z-score (+10.377); Iddq drift z-score (+9.836); Iddq z-score @24h (+4.354)

**Evidence:** Standby Current (Iddq) reads 38.01 µA at 24h against a lot median of 12.78 µA (2.98x lot median) and uses 38% of the 100 µA datasheet limit. Drift is +32.3% versus a lot-median drift of +5.2%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 097 - SN03-0248 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.977

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 12.58 µA | 14.53 µA | 0.87x | 1.2 | 13% |
| Leakage Current (Ileak) | 39.75 µA | 41.16 µA | 8.19 µA | 5.03x | 9.6 | 82% |
| Propagation Delay (tpd) | 8.26 ns | 8.37 ns | 8.33 ns | 1.01x | 0.4 | 56% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 89%, Propagation Delay (tpd) 2%

**Top attribution features:** leakage z-score @0h (+9.625); leakage z-score @24h (+9.478); Iddq drift z-score (+1.196)

**Evidence:** Leakage Current (Ileak) reads 41.16 µA at 24h against a lot median of 8.19 µA (5.03x lot median) and uses 82% of the 50 µA datasheet limit. Drift is +3.6% versus a lot-median drift of +4.4%.

### Certificate 098 - SN06-0051 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.977

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 48.67 µA | 50.49 µA | 21.75 µA | 2.32x | 3.7 | 50% |
| Leakage Current (Ileak) | 26.45 µA | 27.18 µA | 7.94 µA | 3.42x | 6.6 | 54% |
| Propagation Delay (tpd) | 9.29 ns | 9.33 ns | 9.80 ns | 0.95x | 0.9 | 62% |

**Parameter contribution:** Standby Current (Iddq) 32%, Leakage Current (Ileak) 58%, Propagation Delay (tpd) 11%

**Top attribution features:** leakage z-score @0h (+6.615); leakage z-score @24h (+6.472); Iddq z-score @0h (+3.651)

**Evidence:** Leakage Current (Ileak) reads 27.18 µA at 24h against a lot median of 7.94 µA (3.42x lot median) and uses 54% of the 50 µA datasheet limit. Drift is +2.8% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 099 - SN08-0170 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.975

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.27 µA | 26.43 µA | 12.78 µA | 2.07x | 9.1 | 26% |
| Leakage Current (Ileak) | 6.76 µA | 8.46 µA | 5.03 µA | 1.68x | 10.9 | 17% |
| Propagation Delay (tpd) | 8.68 ns | 9.00 ns | 8.48 ns | 1.06x | 2.8 | 60% |

**Parameter contribution:** Standby Current (Iddq) 41%, Leakage Current (Ileak) 42%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+10.875); Iddq drift z-score (+9.140); delay drift z-score (+2.830)

**Evidence:** Leakage Current (Ileak) reads 8.46 µA at 24h against a lot median of 5.03 µA (1.68x lot median) and uses 17% of the 50 µA datasheet limit. Drift is +25.1% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 100 - SN04-0064 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.974

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.37 µA | 27.21 µA | 17.67 µA | 1.54x | 4.6 | 27% |
| Leakage Current (Ileak) | 5.97 µA | 6.45 µA | 6.43 µA | 1.00x | 0.4 | 13% |
| Propagation Delay (tpd) | 13.41 ns | 13.71 ns | 10.33 ns | 1.33x | 5.2 | 91% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 2%, Propagation Delay (tpd) 59%

**Top attribution features:** delay z-score @0h (+5.166); delay z-score @24h (+4.918); Iddq drift z-score (+4.623)

**Evidence:** Propagation Delay (tpd) reads 13.71 ns at 24h against a lot median of 10.33 ns (1.33x lot median) and uses 91% of the 15 ns datasheet limit. Drift is +2.2% versus a lot-median drift of +1.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 101 - SN05-0007 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.974

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.71 µA | 36.24 µA | 21.74 µA | 1.67x | 7.1 | 36% |
| Leakage Current (Ileak) | 11.28 µA | 14.55 µA | 5.71 µA | 2.55x | 6.2 | 29% |
| Propagation Delay (tpd) | 8.81 ns | 9.11 ns | 8.87 ns | 1.03x | 3.5 | 61% |

**Parameter contribution:** Standby Current (Iddq) 37%, Leakage Current (Ileak) 49%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq drift z-score (+7.150); leakage drift z-score (+6.160); leakage z-score @24h (+4.534)

**Evidence:** Leakage Current (Ileak) reads 14.55 µA at 24h against a lot median of 5.71 µA (2.55x lot median) and uses 29% of the 50 µA datasheet limit. Drift is +28.9% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 102 - SN03-0168 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.972

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 13.25 µA | 14.53 µA | 0.91x | 0.3 | 13% |
| Leakage Current (Ileak) | 33.11 µA | 35.41 µA | 8.19 µA | 4.32x | 7.8 | 71% |
| Propagation Delay (tpd) | 9.18 ns | 9.21 ns | 8.33 ns | 1.11x | 2.0 | 61% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 76%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage z-score @24h (+7.823); leakage z-score @0h (+7.620); delay z-score @0h (+2.018)

**Evidence:** Leakage Current (Ileak) reads 35.41 µA at 24h against a lot median of 8.19 µA (4.32x lot median) and uses 71% of the 50 µA datasheet limit. Drift is +6.9% versus a lot-median drift of +4.4%.

### Certificate 103 - SN08-0221 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.971

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 51.44 µA | 58.32 µA | 12.78 µA | 4.56x | 7.9 | 58% |
| Leakage Current (Ileak) | 4.65 µA | 4.81 µA | 5.03 µA | 0.96x | 0.1 | 10% |
| Propagation Delay (tpd) | 8.69 ns | 8.88 ns | 8.48 ns | 1.05x | 1.2 | 59% |

**Parameter contribution:** Standby Current (Iddq) 84%, Leakage Current (Ileak) 1%, Propagation Delay (tpd) 15%

**Top attribution features:** Iddq z-score @24h (+7.859); Iddq z-score @0h (+7.423); Iddq drift z-score (+2.975)

**Evidence:** Standby Current (Iddq) reads 58.32 µA at 24h against a lot median of 12.78 µA (4.56x lot median) and uses 58% of the 100 µA datasheet limit. Drift is +13.4% versus a lot-median drift of +5.2%.

### Certificate 104 - SN06-0125 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.971

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.44 µA | 37.26 µA | 21.75 µA | 1.71x | 6.8 | 37% |
| Leakage Current (Ileak) | 15.70 µA | 20.08 µA | 7.94 µA | 2.53x | 9.1 | 40% |
| Propagation Delay (tpd) | 10.18 ns | 10.38 ns | 9.80 ns | 1.06x | 2.2 | 69% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage drift z-score (+9.126); Iddq drift z-score (+6.791); leakage z-score @24h (+4.085)

**Evidence:** Leakage Current (Ileak) reads 20.08 µA at 24h against a lot median of 7.94 µA (2.53x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +27.9% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 105 - SN02-0028 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.970

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 37.15 µA | 38.23 µA | 18.95 µA | 2.02x | 4.4 | 38% |
| Leakage Current (Ileak) | 19.39 µA | 19.95 µA | 6.95 µA | 2.87x | 4.9 | 40% |
| Propagation Delay (tpd) | 8.72 ns | 8.79 ns | 9.82 ns | 0.89x | 1.7 | 59% |

**Parameter contribution:** Standby Current (Iddq) 38%, Leakage Current (Ileak) 44%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage z-score @0h (+4.903); leakage z-score @24h (+4.765); Iddq z-score @0h (+4.406)

**Evidence:** Leakage Current (Ileak) reads 19.95 µA at 24h against a lot median of 6.95 µA (2.87x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +2.9% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 106 - SN05-0017 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.969

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 30.08 µA | 31.16 µA | 21.74 µA | 1.43x | 1.6 | 31% |
| Leakage Current (Ileak) | 16.50 µA | 19.27 µA | 5.71 µA | 3.38x | 7.0 | 39% |
| Propagation Delay (tpd) | 7.81 ns | 7.93 ns | 8.87 ns | 0.89x | 1.7 | 53% |

**Parameter contribution:** Standby Current (Iddq) 16%, Leakage Current (Ileak) 67%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage z-score @24h (+6.956); leakage z-score @0h (+6.367); leakage drift z-score (+2.794)

**Evidence:** Leakage Current (Ileak) reads 19.27 µA at 24h against a lot median of 5.71 µA (3.38x lot median) and uses 39% of the 50 µA datasheet limit. Drift is +16.8% versus a lot-median drift of +6.7%.

### Certificate 107 - SN02-0243 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.966

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.84 µA | 33.36 µA | 18.95 µA | 1.76x | 11.1 | 33% |
| Leakage Current (Ileak) | 9.51 µA | 11.91 µA | 6.95 µA | 1.71x | 7.9 | 24% |
| Propagation Delay (tpd) | 10.31 ns | 10.56 ns | 9.82 ns | 1.08x | 1.2 | 70% |

**Parameter contribution:** Standby Current (Iddq) 51%, Leakage Current (Ileak) 37%, Propagation Delay (tpd) 12%

**Top attribution features:** Iddq drift z-score (+11.065); leakage drift z-score (+7.916); Iddq z-score @24h (+2.706)

**Evidence:** Standby Current (Iddq) reads 33.36 µA at 24h against a lot median of 18.95 µA (1.76x lot median) and uses 33% of the 100 µA datasheet limit. Drift is +46.1% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 108 - SN07-0120 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.960

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.37 µA | 31.62 µA | 17.12 µA | 1.85x | 6.2 | 32% |
| Leakage Current (Ileak) | 12.75 µA | 16.26 µA | 10.67 µA | 1.52x | 9.1 | 33% |
| Propagation Delay (tpd) | 9.51 ns | 9.80 ns | 8.96 ns | 1.09x | 2.2 | 65% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 41%, Propagation Delay (tpd) 20%

**Top attribution features:** leakage drift z-score (+9.081); Iddq drift z-score (+6.187); Iddq z-score @24h (+2.858)

**Evidence:** Leakage Current (Ileak) reads 16.26 µA at 24h against a lot median of 10.67 µA (1.52x lot median) and uses 33% of the 50 µA datasheet limit. Drift is +27.6% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 109 - SN02-0016 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.958

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 17.18 µA | 18.95 µA | 0.91x | 0.6 | 17% |
| Leakage Current (Ileak) | 23.87 µA | 25.99 µA | 6.95 µA | 3.74x | 7.0 | 52% |
| Propagation Delay (tpd) | 10.87 ns | 10.93 ns | 9.82 ns | 1.11x | 2.1 | 73% |

**Parameter contribution:** Standby Current (Iddq) 6%, Leakage Current (Ileak) 72%, Propagation Delay (tpd) 23%

**Top attribution features:** leakage z-score @24h (+6.980); leakage z-score @0h (+6.604); delay z-score @0h (+2.139)

**Evidence:** Leakage Current (Ileak) reads 25.99 µA at 24h against a lot median of 6.95 µA (3.74x lot median) and uses 52% of the 50 µA datasheet limit. Drift is +8.9% versus a lot-median drift of +4.6%.

### Certificate 110 - SN07-0156 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.954

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.94 µA | 28.54 µA | 17.12 µA | 1.67x | 9.9 | 29% |
| Leakage Current (Ileak) | 17.85 µA | 22.70 µA | 10.67 µA | 2.13x | 8.9 | 45% |
| Propagation Delay (tpd) | 8.77 ns | 8.89 ns | 8.96 ns | 0.99x | 0.2 | 59% |

**Parameter contribution:** Standby Current (Iddq) 47%, Leakage Current (Ileak) 51%, Propagation Delay (tpd) 1%

**Top attribution features:** Iddq drift z-score (+9.885); leakage drift z-score (+8.925); leakage z-score @24h (+3.152)

**Evidence:** Leakage Current (Ileak) reads 22.70 µA at 24h against a lot median of 10.67 µA (2.13x lot median) and uses 45% of the 50 µA datasheet limit. Drift is +27.2% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 111 - SN02-0274 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.953

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 17.05 µA | 18.95 µA | 0.90x | 0.8 | 17% |
| Leakage Current (Ileak) | 6.95 µA | 7.33 µA | 6.95 µA | 1.05x | 0.3 | 15% |
| Propagation Delay (tpd) | 13.76 ns | 13.81 ns | 9.82 ns | 1.41x | 7.3 | 92% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 88%

**Top attribution features:** delay z-score @0h (+7.256); delay z-score @24h (+6.241); delay drift z-score (+1.194)

**Evidence:** Propagation Delay (tpd) reads 13.81 ns at 24h against a lot median of 9.82 ns (1.41x lot median) and uses 92% of the 15 ns datasheet limit. Drift is +0.4% versus a lot-median drift of +1.4%.

### Certificate 112 - SN01-0194 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.951

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 95.26 µA | 95.64 µA | 24.51 µA | 3.90x | 7.4 | 96% |
| Leakage Current (Ileak) | 9.03 µA | 9.32 µA | 9.64 µA | 0.97x | 0.7 | 19% |
| Propagation Delay (tpd) | 8.26 ns | 8.32 ns | 8.46 ns | 0.98x | 0.7 | 55% |

**Parameter contribution:** Standby Current (Iddq) 89%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 7%

**Top attribution features:** Iddq z-score @0h (+7.432); Iddq z-score @24h (+7.048); Iddq drift z-score (+1.590)

**Evidence:** Standby Current (Iddq) reads 95.64 µA at 24h against a lot median of 24.51 µA (3.90x lot median) and uses 96% of the 100 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +3.8%.

### Certificate 113 - SN08-0048 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.950

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.84 µA | 12.48 µA | 12.78 µA | 0.98x | 0.1 | 12% |
| Leakage Current (Ileak) | 18.20 µA | 18.50 µA | 5.03 µA | 3.68x | 6.7 | 37% |
| Propagation Delay (tpd) | 9.16 ns | 9.32 ns | 8.48 ns | 1.10x | 2.5 | 62% |

**Parameter contribution:** Standby Current (Iddq) 1%, Leakage Current (Ileak) 72%, Propagation Delay (tpd) 27%

**Top attribution features:** leakage z-score @24h (+6.663); leakage z-score @0h (+6.579); delay z-score @0h (+2.472)

**Evidence:** Leakage Current (Ileak) reads 18.50 µA at 24h against a lot median of 5.03 µA (3.68x lot median) and uses 37% of the 50 µA datasheet limit. Drift is +1.6% versus a lot-median drift of +3.5%.

### Certificate 114 - SN04-0225 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.933

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.35 µA | 32.06 µA | 17.67 µA | 1.81x | 2.5 | 32% |
| Leakage Current (Ileak) | 17.38 µA | 17.88 µA | 6.43 µA | 2.78x | 4.4 | 36% |
| Propagation Delay (tpd) | 8.55 ns | 8.77 ns | 10.33 ns | 0.85x | 2.6 | 58% |

**Parameter contribution:** Standby Current (Iddq) 26%, Leakage Current (Ileak) 44%, Propagation Delay (tpd) 29%

**Top attribution features:** leakage z-score @0h (+4.439); leakage z-score @24h (+4.056); delay z-score @0h (+2.571)

**Evidence:** Leakage Current (Ileak) reads 17.88 µA at 24h against a lot median of 6.43 µA (2.78x lot median) and uses 36% of the 50 µA datasheet limit. Drift is +2.9% versus a lot-median drift of +6.5%.

### Certificate 115 - SN01-0193 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.928

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.81 µA | 38.97 µA | 24.51 µA | 1.59x | 8.7 | 39% |
| Leakage Current (Ileak) | 11.80 µA | 16.70 µA | 9.64 µA | 1.73x | 12.6 | 33% |
| Propagation Delay (tpd) | 8.59 ns | 8.77 ns | 8.46 ns | 1.04x | 1.5 | 58% |

**Parameter contribution:** Standby Current (Iddq) 38%, Leakage Current (Ileak) 52%, Propagation Delay (tpd) 9%

**Top attribution features:** leakage drift z-score (+12.588); Iddq drift z-score (+8.656); leakage z-score @24h (+1.714)

**Evidence:** Leakage Current (Ileak) reads 16.70 µA at 24h against a lot median of 9.64 µA (1.73x lot median) and uses 33% of the 50 µA datasheet limit. Drift is +41.6% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 116 - SN07-0102 (LOT-G)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.926

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 45.61 µA | 47.03 µA | 17.12 µA | 2.75x | 6.2 | 47% |
| Leakage Current (Ileak) | 22.47 µA | 23.25 µA | 10.67 µA | 2.18x | 3.5 | 47% |
| Propagation Delay (tpd) | 8.66 ns | 8.83 ns | 8.96 ns | 0.99x | 0.7 | 59% |

**Parameter contribution:** Standby Current (Iddq) 59%, Leakage Current (Ileak) 34%, Propagation Delay (tpd) 6%

**Top attribution features:** Iddq z-score @0h (+6.181); Iddq z-score @24h (+5.896); leakage z-score @0h (+3.479)

**Evidence:** Standby Current (Iddq) reads 47.03 µA at 24h against a lot median of 17.12 µA (2.75x lot median) and uses 47% of the 100 µA datasheet limit. Drift is +3.1% versus a lot-median drift of +5.2%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 117 - SN01-0035 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.924

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.60 µA | 24.42 µA | 24.51 µA | 1.00x | 0.2 | 24% |
| Leakage Current (Ileak) | 37.31 µA | 43.38 µA | 9.64 µA | 4.50x | 8.2 | 87% |
| Propagation Delay (tpd) | 8.26 ns | 8.39 ns | 8.46 ns | 0.99x | 0.7 | 56% |

**Parameter contribution:** Standby Current (Iddq) 1%, Leakage Current (Ileak) 94%, Propagation Delay (tpd) 5%

**Top attribution features:** leakage z-score @24h (+8.188); leakage z-score @0h (+7.505); leakage drift z-score (+3.861)

**Evidence:** Leakage Current (Ileak) reads 43.38 µA at 24h against a lot median of 9.64 µA (4.50x lot median) and uses 87% of the 50 µA datasheet limit. Drift is +16.3% versus a lot-median drift of +5.1%.

### Certificate 118 - SN06-0024 (LOT-F)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.924

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 88.58 µA | 94.80 µA | 21.75 µA | 4.36x | 8.8 | 95% |
| Leakage Current (Ileak) | 9.75 µA | 10.34 µA | 7.94 µA | 1.30x | 0.8 | 21% |
| Propagation Delay (tpd) | 9.97 ns | 10.04 ns | 9.80 ns | 1.02x | 0.5 | 67% |

**Parameter contribution:** Standby Current (Iddq) 85%, Leakage Current (Ileak) 10%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq z-score @0h (+8.802); Iddq z-score @24h (+8.763); leakage z-score @24h (+0.808)

**Evidence:** Standby Current (Iddq) reads 94.80 µA at 24h against a lot median of 21.75 µA (4.36x lot median) and uses 95% of the 100 µA datasheet limit. Drift is +7.0% versus a lot-median drift of +5.3%.

### Certificate 119 - SN02-0218 (LOT-B)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.922

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 17.11 µA | 18.95 µA | 0.90x | 0.7 | 17% |
| Leakage Current (Ileak) | 7.20 µA | 7.48 µA | 6.95 µA | 1.08x | 0.3 | 15% |
| Propagation Delay (tpd) | 13.51 ns | 13.80 ns | 9.82 ns | 1.41x | 6.8 | 92% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 5%, Propagation Delay (tpd) 87%

**Top attribution features:** delay z-score @0h (+6.810); delay z-score @24h (+6.222); delay drift z-score (+0.882)

**Evidence:** Propagation Delay (tpd) reads 13.80 ns at 24h against a lot median of 9.82 ns (1.41x lot median) and uses 92% of the 15 ns datasheet limit. Drift is +2.2% versus a lot-median drift of +1.4%.

### Certificate 120 - SN05-0179 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.919

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.81 µA | 33.26 µA | 21.74 µA | 1.53x | 1.9 | 33% |
| Leakage Current (Ileak) | 14.85 µA | 15.62 µA | 5.71 µA | 2.74x | 5.4 | 31% |
| Propagation Delay (tpd) | 7.51 ns | 7.59 ns | 8.87 ns | 0.86x | 2.3 | 51% |

**Parameter contribution:** Standby Current (Iddq) 21%, Leakage Current (Ileak) 55%, Propagation Delay (tpd) 23%

**Top attribution features:** leakage z-score @0h (+5.425); leakage z-score @24h (+5.082); delay z-score @24h (+2.309)

**Evidence:** Leakage Current (Ileak) reads 15.62 µA at 24h against a lot median of 5.71 µA (2.74x lot median) and uses 31% of the 50 µA datasheet limit. Drift is +5.1% versus a lot-median drift of +6.7%.

### Certificate 121 - SN01-0203 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.914

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 71.73 µA | 74.97 µA | 24.51 µA | 3.06x | 5.0 | 75% |
| Leakage Current (Ileak) | 16.83 µA | 18.33 µA | 9.64 µA | 1.90x | 2.1 | 37% |
| Propagation Delay (tpd) | 7.39 ns | 7.48 ns | 8.46 ns | 0.88x | 2.0 | 50% |

**Parameter contribution:** Standby Current (Iddq) 52%, Leakage Current (Ileak) 28%, Propagation Delay (tpd) 20%

**Top attribution features:** Iddq z-score @24h (+4.999); Iddq z-score @0h (+4.992); leakage z-score @24h (+2.108)

**Evidence:** Standby Current (Iddq) reads 74.97 µA at 24h against a lot median of 24.51 µA (3.06x lot median) and uses 75% of the 100 µA datasheet limit. Drift is +4.5% versus a lot-median drift of +3.8%.

### Certificate 122 - SN03-0172 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.912

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.55 µA | 23.82 µA | 14.53 µA | 1.64x | 5.2 | 24% |
| Leakage Current (Ileak) | 10.29 µA | 13.52 µA | 8.19 µA | 1.65x | 12.3 | 27% |
| Propagation Delay (tpd) | 8.49 ns | 8.78 ns | 8.33 ns | 1.05x | 3.3 | 59% |

**Parameter contribution:** Standby Current (Iddq) 30%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+12.318); Iddq drift z-score (+5.218); delay drift z-score (+3.321)

**Evidence:** Leakage Current (Ileak) reads 13.52 µA at 24h against a lot median of 8.19 µA (1.65x lot median) and uses 27% of the 50 µA datasheet limit. Drift is +31.4% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 123 - SN01-0160 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.912

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 95.00 µA | 95.38 µA | 24.51 µA | 3.89x | 7.4 | 95% |
| Leakage Current (Ileak) | 13.01 µA | 13.32 µA | 9.64 µA | 1.38x | 1.1 | 27% |
| Propagation Delay (tpd) | 8.26 ns | 8.38 ns | 8.46 ns | 0.99x | 0.4 | 56% |

**Parameter contribution:** Standby Current (Iddq) 82%, Leakage Current (Ileak) 15%, Propagation Delay (tpd) 4%

**Top attribution features:** Iddq z-score @0h (+7.405); Iddq z-score @24h (+7.022); Iddq drift z-score (+1.590)

**Evidence:** Standby Current (Iddq) reads 95.38 µA at 24h against a lot median of 24.51 µA (3.89x lot median) and uses 95% of the 100 µA datasheet limit. Drift is +0.4% versus a lot-median drift of +3.8%.

### Certificate 124 - SN08-0007 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.910

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 55.75 µA | 58.46 µA | 12.78 µA | 4.58x | 8.2 | 58% |
| Leakage Current (Ileak) | 4.65 µA | 4.97 µA | 5.03 µA | 0.99x | 1.8 | 10% |
| Propagation Delay (tpd) | 8.44 ns | 8.54 ns | 8.48 ns | 1.01x | 0.3 | 57% |

**Parameter contribution:** Standby Current (Iddq) 86%, Leakage Current (Ileak) 10%, Propagation Delay (tpd) 4%

**Top attribution features:** Iddq z-score @0h (+8.235); Iddq z-score @24h (+7.883); leakage drift z-score (+1.753)

**Evidence:** Standby Current (Iddq) reads 58.46 µA at 24h against a lot median of 12.78 µA (4.58x lot median) and uses 58% of the 100 µA datasheet limit. Drift is +4.9% versus a lot-median drift of +5.2%.

### Certificate 125 - SN04-0063 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.909

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.09 µA | 17.50 µA | 17.67 µA | 0.99x | 0.8 | 18% |
| Leakage Current (Ileak) | 24.28 µA | 28.51 µA | 6.43 µA | 4.43x | 7.8 | 57% |
| Propagation Delay (tpd) | 9.88 ns | 9.93 ns | 10.33 ns | 0.96x | 0.9 | 66% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 86%, Propagation Delay (tpd) 10%

**Top attribution features:** leakage z-score @24h (+7.821); leakage z-score @0h (+7.126); leakage drift z-score (+3.016)

**Evidence:** Leakage Current (Ileak) reads 28.51 µA at 24h against a lot median of 6.43 µA (4.43x lot median) and uses 57% of the 50 µA datasheet limit. Drift is +17.4% versus a lot-median drift of +6.5%.

### Certificate 126 - SN04-0120 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.906

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 40.92 µA | 44.77 µA | 17.67 µA | 2.53x | 4.4 | 45% |
| Leakage Current (Ileak) | 11.17 µA | 14.59 µA | 6.43 µA | 2.27x | 6.6 | 29% |
| Propagation Delay (tpd) | 9.78 ns | 9.89 ns | 10.33 ns | 0.96x | 0.7 | 66% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 49%, Propagation Delay (tpd) 7%

**Top attribution features:** leakage drift z-score (+6.634); Iddq z-score @24h (+4.383); Iddq z-score @0h (+4.106)

**Evidence:** Leakage Current (Ileak) reads 14.59 µA at 24h against a lot median of 6.43 µA (2.27x lot median) and uses 29% of the 50 µA datasheet limit. Drift is +30.6% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 127 - SN01-0058 (LOT-A)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.892

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 34.24 µA | 41.82 µA | 24.51 µA | 1.71x | 8.5 | 42% |
| Leakage Current (Ileak) | 12.85 µA | 16.42 µA | 9.64 µA | 1.70x | 7.8 | 33% |
| Propagation Delay (tpd) | 8.87 ns | 9.11 ns | 8.46 ns | 1.08x | 2.4 | 61% |

**Parameter contribution:** Standby Current (Iddq) 42%, Leakage Current (Ileak) 39%, Propagation Delay (tpd) 18%

**Top attribution features:** Iddq drift z-score (+8.480); leakage drift z-score (+7.842); delay drift z-score (+2.418)

**Evidence:** Standby Current (Iddq) reads 41.82 µA at 24h against a lot median of 24.51 µA (1.71x lot median) and uses 42% of the 100 µA datasheet limit. Drift is +22.1% versus a lot-median drift of +3.8%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 128 - SN03-0081 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.876

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.88 µA | 20.76 µA | 14.53 µA | 1.43x | 3.9 | 21% |
| Leakage Current (Ileak) | 12.49 µA | 15.98 µA | 8.19 µA | 1.95x | 10.8 | 32% |
| Propagation Delay (tpd) | 8.20 ns | 8.38 ns | 8.33 ns | 1.01x | 1.7 | 56% |

**Parameter contribution:** Standby Current (Iddq) 26%, Leakage Current (Ileak) 65%, Propagation Delay (tpd) 9%

**Top attribution features:** leakage drift z-score (+10.761); Iddq drift z-score (+3.881); leakage z-score @24h (+2.241)

**Evidence:** Leakage Current (Ileak) reads 15.98 µA at 24h against a lot median of 8.19 µA (1.95x lot median) and uses 32% of the 50 µA datasheet limit. Drift is +28.0% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 129 - SN08-0232 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.875

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.84 µA | 12.29 µA | 12.78 µA | 0.96x | 0.5 | 12% |
| Leakage Current (Ileak) | 17.37 µA | 20.07 µA | 5.03 µA | 3.99x | 7.4 | 40% |
| Propagation Delay (tpd) | 8.43 ns | 8.50 ns | 8.48 ns | 1.00x | 0.5 | 57% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 93%, Propagation Delay (tpd) 4%

**Top attribution features:** leakage z-score @24h (+7.439); leakage z-score @0h (+6.167); leakage drift z-score (+6.078)

**Evidence:** Leakage Current (Ileak) reads 20.07 µA at 24h against a lot median of 5.03 µA (3.99x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +15.6% versus a lot-median drift of +3.5%.

### Certificate 130 - SN03-0247 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.869

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 13.60 µA | 14.53 µA | 0.94x | 0.8 | 14% |
| Leakage Current (Ileak) | 29.58 µA | 32.01 µA | 8.19 µA | 3.91x | 6.8 | 64% |
| Propagation Delay (tpd) | 8.72 ns | 8.76 ns | 8.33 ns | 1.05x | 1.1 | 58% |

**Parameter contribution:** Standby Current (Iddq) 7%, Leakage Current (Ileak) 78%, Propagation Delay (tpd) 15%

**Top attribution features:** leakage z-score @24h (+6.848); leakage z-score @0h (+6.556); leakage drift z-score (+1.743)

**Evidence:** Leakage Current (Ileak) reads 32.01 µA at 24h against a lot median of 8.19 µA (3.91x lot median) and uses 64% of the 50 µA datasheet limit. Drift is +8.2% versus a lot-median drift of +4.4%.

### Certificate 131 - SN03-0201 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.862

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.14 µA | 20.91 µA | 14.53 µA | 1.44x | 5.5 | 21% |
| Leakage Current (Ileak) | 18.95 µA | 22.78 µA | 8.19 µA | 2.78x | 7.2 | 46% |
| Propagation Delay (tpd) | 8.59 ns | 8.79 ns | 8.33 ns | 1.06x | 1.9 | 59% |

**Parameter contribution:** Standby Current (Iddq) 29%, Leakage Current (Ileak) 58%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage drift z-score (+7.229); Iddq drift z-score (+5.491); leakage z-score @24h (+4.195)

**Evidence:** Leakage Current (Ileak) reads 22.78 µA at 24h against a lot median of 8.19 µA (2.78x lot median) and uses 46% of the 50 µA datasheet limit. Drift is +20.3% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 132 - SN04-0065 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.849

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.78 µA | 33.52 µA | 17.67 µA | 1.90x | 9.9 | 34% |
| Leakage Current (Ileak) | 8.40 µA | 10.86 µA | 6.43 µA | 1.69x | 6.3 | 22% |
| Propagation Delay (tpd) | 10.78 ns | 11.04 ns | 10.33 ns | 1.07x | 1.3 | 74% |

**Parameter contribution:** Standby Current (Iddq) 54%, Leakage Current (Ileak) 34%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq drift z-score (+9.889); leakage drift z-score (+6.272); Iddq z-score @24h (+2.564)

**Evidence:** Standby Current (Iddq) reads 33.52 µA at 24h against a lot median of 17.67 µA (1.90x lot median) and uses 34% of the 100 µA datasheet limit. Drift is +30.1% versus a lot-median drift of +4.5%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 133 - SN03-0138 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.824

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 5.96 µA | 6.42 µA | 14.53 µA | 0.44x | 1.6 | 6% |
| Leakage Current (Ileak) | 5.76 µA | 7.17 µA | 8.19 µA | 0.88x | 9.2 | 14% |
| Propagation Delay (tpd) | 8.89 ns | 9.04 ns | 8.33 ns | 1.09x | 1.4 | 60% |

**Parameter contribution:** Standby Current (Iddq) 20%, Leakage Current (Ileak) 59%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage drift z-score (+9.202); Iddq z-score @0h (+1.633); Iddq z-score @24h (+1.612)

**Evidence:** Leakage Current (Ileak) reads 7.17 µA at 24h against a lot median of 8.19 µA (0.88x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +24.6% versus a lot-median drift of +4.4%.

### Certificate 134 - SN07-0103 (LOT-G)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.816

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.55 µA | 21.06 µA | 17.12 µA | 1.23x | 0.9 | 21% |
| Leakage Current (Ileak) | 22.29 µA | 24.30 µA | 10.67 µA | 2.28x | 3.6 | 49% |
| Propagation Delay (tpd) | 7.64 ns | 7.67 ns | 8.96 ns | 0.86x | 2.8 | 51% |

**Parameter contribution:** Standby Current (Iddq) 14%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 38%

**Top attribution features:** leakage z-score @24h (+3.571); leakage z-score @0h (+3.429); delay z-score @24h (+2.797)

**Evidence:** Leakage Current (Ileak) reads 24.30 µA at 24h against a lot median of 10.67 µA (2.28x lot median) and uses 49% of the 50 µA datasheet limit. Drift is +9.0% versus a lot-median drift of +5.0%.

### Certificate 135 - SN08-0097 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.814

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 45.89 µA | 51.97 µA | 12.78 µA | 4.07x | 6.8 | 52% |
| Leakage Current (Ileak) | 7.58 µA | 7.79 µA | 5.03 µA | 1.55x | 1.4 | 16% |
| Propagation Delay (tpd) | 8.25 ns | 8.40 ns | 8.48 ns | 0.99x | 0.6 | 56% |

**Parameter contribution:** Standby Current (Iddq) 80%, Leakage Current (Ileak) 15%, Propagation Delay (tpd) 5%

**Top attribution features:** Iddq z-score @24h (+6.764); Iddq z-score @0h (+6.380); Iddq drift z-score (+2.926)

**Evidence:** Standby Current (Iddq) reads 51.97 µA at 24h against a lot median of 12.78 µA (4.07x lot median) and uses 52% of the 100 µA datasheet limit. Drift is +13.2% versus a lot-median drift of +5.2%.

### Certificate 136 - SN04-0050 (LOT-D)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.812

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 14.03 µA | 14.61 µA | 17.67 µA | 0.83x | 0.5 | 15% |
| Leakage Current (Ileak) | 4.99 µA | 6.92 µA | 6.43 µA | 1.08x | 8.9 | 14% |
| Propagation Delay (tpd) | 10.41 ns | 10.68 ns | 10.33 ns | 1.03x | 1.4 | 71% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 73%, Propagation Delay (tpd) 18%

**Top attribution features:** leakage drift z-score (+8.908); delay drift z-score (+1.426); delay z-score @24h (+0.499)

**Evidence:** Leakage Current (Ileak) reads 6.92 µA at 24h against a lot median of 6.43 µA (1.08x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +38.8% versus a lot-median drift of +6.5%.

### Certificate 137 - SN03-0126 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.810

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.38 µA | 20.84 µA | 14.53 µA | 1.43x | 3.1 | 21% |
| Leakage Current (Ileak) | 10.80 µA | 13.37 µA | 8.19 µA | 1.63x | 8.9 | 27% |
| Propagation Delay (tpd) | 8.77 ns | 8.96 ns | 8.33 ns | 1.08x | 1.6 | 60% |

**Parameter contribution:** Standby Current (Iddq) 26%, Leakage Current (Ileak) 55%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage drift z-score (+8.854); Iddq drift z-score (+3.131); delay drift z-score (+1.572)

**Evidence:** Leakage Current (Ileak) reads 13.37 µA at 24h against a lot median of 8.19 µA (1.63x lot median) and uses 27% of the 50 µA datasheet limit. Drift is +23.8% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 138 - SN08-0207 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.795

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.13 µA | 12.36 µA | 12.78 µA | 0.97x | 1.2 | 12% |
| Leakage Current (Ileak) | 4.19 µA | 5.04 µA | 5.03 µA | 1.00x | 8.5 | 10% |
| Propagation Delay (tpd) | 7.98 ns | 8.08 ns | 8.48 ns | 0.95x | 1.1 | 54% |

**Parameter contribution:** Standby Current (Iddq) 10%, Leakage Current (Ileak) 72%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+8.518); Iddq drift z-score (+1.186); delay z-score @0h (+1.091)

**Evidence:** Leakage Current (Ileak) reads 5.04 µA at 24h against a lot median of 5.03 µA (1.00x lot median) and uses 10% of the 50 µA datasheet limit. Drift is +20.4% versus a lot-median drift of +3.5%.

### Certificate 139 - SN02-0237 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.794

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 25.26 µA | 31.49 µA | 18.95 µA | 1.66x | 5.1 | 31% |
| Leakage Current (Ileak) | 10.86 µA | 13.08 µA | 6.95 µA | 1.88x | 6.1 | 26% |
| Propagation Delay (tpd) | 10.68 ns | 10.92 ns | 9.82 ns | 1.11x | 1.8 | 73% |

**Parameter contribution:** Standby Current (Iddq) 39%, Leakage Current (Ileak) 42%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage drift z-score (+6.072); Iddq drift z-score (+5.125); Iddq z-score @24h (+2.354)

**Evidence:** Leakage Current (Ileak) reads 13.08 µA at 24h against a lot median of 6.95 µA (1.88x lot median) and uses 26% of the 50 µA datasheet limit. Drift is +20.4% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 140 - SN05-0101 (LOT-E)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.782

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.14 µA | 35.17 µA | 21.74 µA | 1.62x | 8.2 | 35% |
| Leakage Current (Ileak) | 7.90 µA | 9.43 µA | 5.71 µA | 1.65x | 3.5 | 19% |
| Propagation Delay (tpd) | 9.01 ns | 9.13 ns | 8.87 ns | 1.03x | 0.5 | 61% |

**Parameter contribution:** Standby Current (Iddq) 58%, Leakage Current (Ileak) 35%, Propagation Delay (tpd) 7%

**Top attribution features:** Iddq drift z-score (+8.243); leakage drift z-score (+3.527); Iddq z-score @24h (+2.243)

**Evidence:** Standby Current (Iddq) reads 35.17 µA at 24h against a lot median of 21.74 µA (1.62x lot median) and uses 35% of the 100 µA datasheet limit. Drift is +34.6% versus a lot-median drift of +5.9%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 141 - SN08-0115 (LOT-H)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.782

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.01 µA | 11.58 µA | 12.78 µA | 0.91x | 0.2 | 12% |
| Leakage Current (Ileak) | 6.71 µA | 8.05 µA | 5.03 µA | 1.60x | 8.2 | 16% |
| Propagation Delay (tpd) | 8.10 ns | 8.15 ns | 8.48 ns | 0.96x | 0.9 | 54% |

**Parameter contribution:** Standby Current (Iddq) 3%, Leakage Current (Ileak) 79%, Propagation Delay (tpd) 18%

**Top attribution features:** leakage drift z-score (+8.243); leakage z-score @24h (+1.494); leakage z-score @0h (+0.912)

**Evidence:** Leakage Current (Ileak) reads 8.05 µA at 24h against a lot median of 5.03 µA (1.60x lot median) and uses 16% of the 50 µA datasheet limit. Drift is +19.9% versus a lot-median drift of +3.5%.

### Certificate 142 - SN03-0040 (LOT-C)

**Verdict:** REJECT | **Risk:** CRITICAL | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.782

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.33 µA | 19.37 µA | 14.53 µA | 1.33x | 1.0 | 19% |
| Leakage Current (Ileak) | 8.69 µA | 10.65 µA | 8.19 µA | 1.30x | 8.2 | 21% |
| Propagation Delay (tpd) | 7.66 ns | 7.76 ns | 8.33 ns | 0.93x | 1.2 | 52% |

**Parameter contribution:** Standby Current (Iddq) 17%, Leakage Current (Ileak) 65%, Propagation Delay (tpd) 19%

**Top attribution features:** leakage drift z-score (+8.234); delay z-score @0h (+1.182); delay z-score @24h (+1.107)

**Evidence:** Leakage Current (Ileak) reads 10.65 µA at 24h against a lot median of 8.19 µA (1.30x lot median) and uses 21% of the 50 µA datasheet limit. Drift is +22.5% versus a lot-median drift of +4.4%.

### Certificate 143 - SN05-0019 (LOT-E)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.779

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.12 µA | 20.70 µA | 21.74 µA | 0.95x | 0.8 | 21% |
| Leakage Current (Ileak) | 18.13 µA | 19.24 µA | 5.71 µA | 3.37x | 7.3 | 38% |
| Propagation Delay (tpd) | 8.92 ns | 9.10 ns | 8.87 ns | 1.03x | 1.4 | 61% |

**Parameter contribution:** Standby Current (Iddq) 6%, Leakage Current (Ileak) 82%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage z-score @0h (+7.300); leakage z-score @24h (+6.941); delay drift z-score (+1.390)

**Evidence:** Leakage Current (Ileak) reads 19.24 µA at 24h against a lot median of 5.71 µA (3.37x lot median) and uses 38% of the 50 µA datasheet limit. Drift is +6.1% versus a lot-median drift of +6.7%.

### Certificate 144 - SN08-0077 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.778

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 34.09 µA | 36.27 µA | 12.78 µA | 2.84x | 4.2 | 36% |
| Leakage Current (Ileak) | 11.31 µA | 11.76 µA | 5.03 µA | 2.34x | 3.3 | 24% |
| Propagation Delay (tpd) | 7.72 ns | 7.84 ns | 8.48 ns | 0.93x | 1.9 | 52% |

**Parameter contribution:** Standby Current (Iddq) 45%, Leakage Current (Ileak) 35%, Propagation Delay (tpd) 20%

**Top attribution features:** Iddq z-score @0h (+4.161); Iddq z-score @24h (+4.054); leakage z-score @24h (+3.328)

**Evidence:** Standby Current (Iddq) reads 36.27 µA at 24h against a lot median of 12.78 µA (2.84x lot median) and uses 36% of the 100 µA datasheet limit. Drift is +6.4% versus a lot-median drift of +5.2%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 145 - SN01-0218 (LOT-A)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.777

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.85 µA | 38.68 µA | 24.51 µA | 1.58x | 6.5 | 39% |
| Leakage Current (Ileak) | 11.91 µA | 15.19 µA | 9.64 µA | 1.58x | 7.8 | 30% |
| Propagation Delay (tpd) | 9.08 ns | 9.28 ns | 8.46 ns | 1.10x | 1.7 | 62% |

**Parameter contribution:** Standby Current (Iddq) 37%, Leakage Current (Ileak) 42%, Propagation Delay (tpd) 21%

**Top attribution features:** leakage drift z-score (+7.752); Iddq drift z-score (+6.454); delay z-score @24h (+1.665)

**Evidence:** Leakage Current (Ileak) reads 15.19 µA at 24h against a lot median of 9.64 µA (1.58x lot median) and uses 30% of the 50 µA datasheet limit. Drift is +27.5% versus a lot-median drift of +5.1%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 146 - SN04-0023 (LOT-D)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.762

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.61 µA | 24.08 µA | 17.67 µA | 1.36x | 4.8 | 24% |
| Leakage Current (Ileak) | 5.12 µA | 6.91 µA | 6.43 µA | 1.07x | 7.8 | 14% |
| Propagation Delay (tpd) | 10.12 ns | 10.30 ns | 10.33 ns | 1.00x | 0.5 | 69% |

**Parameter contribution:** Standby Current (Iddq) 42%, Leakage Current (Ileak) 54%, Propagation Delay (tpd) 4%

**Top attribution features:** leakage drift z-score (+7.846); Iddq drift z-score (+4.782); Iddq z-score @24h (+1.037)

**Evidence:** Leakage Current (Ileak) reads 6.91 µA at 24h against a lot median of 6.43 µA (1.07x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +35.0% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 147 - SN02-0094 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.757

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.83 µA | 24.45 µA | 18.95 µA | 1.29x | 1.6 | 24% |
| Leakage Current (Ileak) | 3.44 µA | 3.76 µA | 6.95 µA | 0.54x | 1.8 | 8% |
| Propagation Delay (tpd) | 11.69 ns | 11.75 ns | 9.82 ns | 1.20x | 3.6 | 78% |

**Parameter contribution:** Standby Current (Iddq) 24%, Leakage Current (Ileak) 27%, Propagation Delay (tpd) 50%

**Top attribution features:** delay z-score @0h (+3.586); delay z-score @24h (+3.017); leakage drift z-score (+1.755)

**Evidence:** Propagation Delay (tpd) reads 11.75 ns at 24h against a lot median of 9.82 ns (1.20x lot median) and uses 78% of the 15 ns datasheet limit. Drift is +0.6% versus a lot-median drift of +1.4%.

### Certificate 148 - SN03-0260 (LOT-C)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.757

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.06 µA | 23.09 µA | 14.53 µA | 1.59x | 6.9 | 23% |
| Leakage Current (Ileak) | 12.55 µA | 15.23 µA | 8.19 µA | 1.86x | 7.7 | 30% |
| Propagation Delay (tpd) | 8.24 ns | 8.40 ns | 8.33 ns | 1.01x | 1.2 | 56% |

**Parameter contribution:** Standby Current (Iddq) 43%, Leakage Current (Ileak) 51%, Propagation Delay (tpd) 6%

**Top attribution features:** leakage drift z-score (+7.740); Iddq drift z-score (+6.903); leakage z-score @24h (+2.025)

**Evidence:** Leakage Current (Ileak) reads 15.23 µA at 24h against a lot median of 8.19 µA (1.86x lot median) and uses 30% of the 50 µA datasheet limit. Drift is +21.4% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 149 - SN05-0061 (LOT-E)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.752

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.07 µA | 28.35 µA | 21.74 µA | 1.30x | 1.1 | 28% |
| Leakage Current (Ileak) | 12.47 µA | 14.68 µA | 5.71 µA | 2.57x | 4.6 | 29% |
| Propagation Delay (tpd) | 9.03 ns | 9.40 ns | 8.87 ns | 1.06x | 4.5 | 63% |

**Parameter contribution:** Standby Current (Iddq) 14%, Leakage Current (Ileak) 57%, Propagation Delay (tpd) 29%

**Top attribution features:** leakage z-score @24h (+4.602); delay drift z-score (+4.515); leakage z-score @0h (+4.065)

**Evidence:** Leakage Current (Ileak) reads 14.68 µA at 24h against a lot median of 5.71 µA (2.57x lot median) and uses 29% of the 50 µA datasheet limit. Drift is +17.7% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Propagation Delay (tpd).

### Certificate 150 - SN05-0172 (LOT-E)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.743

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.73 µA | 36.60 µA | 21.74 µA | 1.68x | 7.5 | 37% |
| Leakage Current (Ileak) | 7.02 µA | 8.11 µA | 5.71 µA | 1.42x | 2.5 | 16% |
| Propagation Delay (tpd) | 8.64 ns | 8.95 ns | 8.87 ns | 1.01x | 3.7 | 60% |

**Parameter contribution:** Standby Current (Iddq) 56%, Leakage Current (Ileak) 23%, Propagation Delay (tpd) 20%

**Top attribution features:** Iddq drift z-score (+7.490); delay drift z-score (+3.678); Iddq z-score @24h (+2.481)

**Evidence:** Standby Current (Iddq) reads 36.60 µA at 24h against a lot median of 21.74 µA (1.68x lot median) and uses 37% of the 100 µA datasheet limit. Drift is +32.0% versus a lot-median drift of +5.9%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 151 - SN08-0137 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.742

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.84 µA | 12.69 µA | 12.78 µA | 0.99x | 0.7 | 13% |
| Leakage Current (Ileak) | 18.52 µA | 19.38 µA | 5.03 µA | 3.86x | 7.1 | 39% |
| Propagation Delay (tpd) | 8.63 ns | 8.76 ns | 8.48 ns | 1.03x | 0.9 | 58% |

**Parameter contribution:** Standby Current (Iddq) 4%, Leakage Current (Ileak) 85%, Propagation Delay (tpd) 11%

**Top attribution features:** leakage z-score @24h (+7.098); leakage z-score @0h (+6.738); delay z-score @0h (+0.867)

**Evidence:** Leakage Current (Ileak) reads 19.38 µA at 24h against a lot median of 5.03 µA (3.86x lot median) and uses 39% of the 50 µA datasheet limit. Drift is +4.6% versus a lot-median drift of +3.5%.

### Certificate 152 - SN01-0106 (LOT-A)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.740

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 9.78 µA | 10.93 µA | 24.51 µA | 0.45x | 3.7 | 11% |
| Leakage Current (Ileak) | 8.01 µA | 8.38 µA | 9.64 µA | 0.87x | 0.3 | 17% |
| Propagation Delay (tpd) | 9.95 ns | 10.09 ns | 8.46 ns | 1.19x | 3.5 | 67% |

**Parameter contribution:** Standby Current (Iddq) 45%, Leakage Current (Ileak) 5%, Propagation Delay (tpd) 50%

**Top attribution features:** Iddq drift z-score (+3.686); delay z-score @0h (+3.467); delay z-score @24h (+3.278)

**Evidence:** Propagation Delay (tpd) reads 10.09 ns at 24h against a lot median of 8.46 ns (1.19x lot median) and uses 67% of the 15 ns datasheet limit. Drift is +1.3% versus a lot-median drift of +1.1%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 153 - SN02-0214 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.740

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 40.19 µA | 43.25 µA | 18.95 µA | 2.28x | 5.1 | 43% |
| Leakage Current (Ileak) | 15.60 µA | 16.25 µA | 6.95 µA | 2.34x | 3.5 | 32% |
| Propagation Delay (tpd) | 9.08 ns | 9.27 ns | 9.82 ns | 0.94x | 1.0 | 62% |

**Parameter contribution:** Standby Current (Iddq) 51%, Leakage Current (Ileak) 36%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq z-score @0h (+5.091); Iddq z-score @24h (+4.562); leakage z-score @0h (+3.462)

**Evidence:** Standby Current (Iddq) reads 43.25 µA at 24h against a lot median of 18.95 µA (2.28x lot median) and uses 43% of the 100 µA datasheet limit. Drift is +7.6% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 154 - SN04-0036 (LOT-D)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.737

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.40 µA | 31.54 µA | 17.67 µA | 1.78x | 5.8 | 32% |
| Leakage Current (Ileak) | 8.80 µA | 11.74 µA | 6.43 µA | 1.83x | 7.4 | 23% |
| Propagation Delay (tpd) | 10.01 ns | 10.26 ns | 10.33 ns | 0.99x | 1.3 | 68% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 8%

**Top attribution features:** leakage drift z-score (+7.399); Iddq drift z-score (+5.790); Iddq z-score @24h (+2.243)

**Evidence:** Leakage Current (Ileak) reads 11.74 µA at 24h against a lot median of 6.43 µA (1.83x lot median) and uses 23% of the 50 µA datasheet limit. Drift is +33.4% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 155 - SN08-0184 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.732

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 46.13 µA | 48.99 µA | 12.78 µA | 3.83x | 6.4 | 49% |
| Leakage Current (Ileak) | 4.65 µA | 4.90 µA | 5.03 µA | 0.97x | 0.9 | 10% |
| Propagation Delay (tpd) | 8.63 ns | 8.78 ns | 8.48 ns | 1.04x | 0.9 | 59% |

**Parameter contribution:** Standby Current (Iddq) 80%, Leakage Current (Ileak) 7%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq z-score @0h (+6.425); Iddq z-score @24h (+6.249); leakage drift z-score (+0.937)

**Evidence:** Standby Current (Iddq) reads 48.99 µA at 24h against a lot median of 12.78 µA (3.83x lot median) and uses 49% of the 100 µA datasheet limit. Drift is +6.2% versus a lot-median drift of +5.2%.

### Certificate 156 - SN07-0184 (LOT-G)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.729

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.19 µA | 12.06 µA | 17.12 µA | 0.70x | 1.0 | 12% |
| Leakage Current (Ileak) | 6.56 µA | 8.07 µA | 10.67 µA | 0.76x | 7.3 | 16% |
| Propagation Delay (tpd) | 9.74 ns | 9.88 ns | 8.96 ns | 1.10x | 2.1 | 66% |

**Parameter contribution:** Standby Current (Iddq) 18%, Leakage Current (Ileak) 56%, Propagation Delay (tpd) 26%

**Top attribution features:** leakage drift z-score (+7.257); delay z-score @0h (+2.082); delay z-score @24h (+1.973)

**Evidence:** Leakage Current (Ileak) reads 8.07 µA at 24h against a lot median of 10.67 µA (0.76x lot median) and uses 16% of the 50 µA datasheet limit. Drift is +23.0% versus a lot-median drift of +5.0%.

### Certificate 157 - SN05-0201 (LOT-E)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.722

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.92 µA | 31.28 µA | 21.74 µA | 1.44x | 7.1 | 31% |
| Leakage Current (Ileak) | 7.65 µA | 8.14 µA | 5.71 µA | 1.43x | 1.3 | 16% |
| Propagation Delay (tpd) | 8.97 ns | 9.11 ns | 8.87 ns | 1.03x | 0.8 | 61% |

**Parameter contribution:** Standby Current (Iddq) 68%, Leakage Current (Ileak) 19%, Propagation Delay (tpd) 12%

**Top attribution features:** Iddq drift z-score (+7.141); Iddq z-score @24h (+1.593); leakage z-score @0h (+1.309)

**Evidence:** Standby Current (Iddq) reads 31.28 µA at 24h against a lot median of 21.74 µA (1.44x lot median) and uses 31% of the 100 µA datasheet limit. Drift is +30.7% versus a lot-median drift of +5.9%.

### Certificate 158 - SN03-0002 (LOT-C)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.718

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.33 µA | 17.64 µA | 14.53 µA | 1.21x | 0.6 | 18% |
| Leakage Current (Ileak) | 7.83 µA | 9.40 µA | 8.19 µA | 1.15x | 7.1 | 19% |
| Propagation Delay (tpd) | 8.53 ns | 8.58 ns | 8.33 ns | 1.03x | 0.6 | 57% |

**Parameter contribution:** Standby Current (Iddq) 14%, Leakage Current (Ileak) 70%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+7.076); delay z-score @0h (+0.650); Iddq z-score @24h (+0.619)

**Evidence:** Leakage Current (Ileak) reads 9.40 µA at 24h against a lot median of 8.19 µA (1.15x lot median) and uses 19% of the 50 µA datasheet limit. Drift is +19.9% versus a lot-median drift of +4.4%.

### Certificate 159 - SN06-0090 (LOT-F)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.709

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 24.66 µA | 31.33 µA | 21.75 µA | 1.44x | 6.9 | 31% |
| Leakage Current (Ileak) | 10.21 µA | 11.75 µA | 7.94 µA | 1.48x | 4.1 | 23% |
| Propagation Delay (tpd) | 10.00 ns | 10.13 ns | 9.80 ns | 1.03x | 1.0 | 68% |

**Parameter contribution:** Standby Current (Iddq) 50%, Leakage Current (Ileak) 37%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq drift z-score (+6.943); leakage drift z-score (+4.104); leakage z-score @24h (+1.280)

**Evidence:** Standby Current (Iddq) reads 31.33 µA at 24h against a lot median of 21.75 µA (1.44x lot median) and uses 31% of the 100 µA datasheet limit. Drift is +27.0% versus a lot-median drift of +5.3%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 160 - SN01-0146 (LOT-A)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.706

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.06 µA | 23.74 µA | 24.51 µA | 0.97x | 1.7 | 24% |
| Leakage Current (Ileak) | 20.85 µA | 22.23 µA | 9.64 µA | 2.31x | 3.1 | 44% |
| Propagation Delay (tpd) | 6.97 ns | 7.04 ns | 8.46 ns | 0.83x | 2.9 | 47% |

**Parameter contribution:** Standby Current (Iddq) 14%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 41%

**Top attribution features:** leakage z-score @0h (+3.134); leakage z-score @24h (+3.055); delay z-score @0h (+2.944)

**Evidence:** Leakage Current (Ileak) reads 22.23 µA at 24h against a lot median of 9.64 µA (2.31x lot median) and uses 44% of the 50 µA datasheet limit. Drift is +6.6% versus a lot-median drift of +5.1%.

### Certificate 161 - SN07-0173 (LOT-G)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.701

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 19.28 µA | 19.85 µA | 17.12 µA | 1.16x | 0.7 | 20% |
| Leakage Current (Ileak) | 13.42 µA | 16.36 µA | 10.67 µA | 1.53x | 6.8 | 33% |
| Propagation Delay (tpd) | 8.35 ns | 8.71 ns | 8.96 ns | 0.97x | 3.8 | 58% |

**Parameter contribution:** Standby Current (Iddq) 12%, Leakage Current (Ileak) 56%, Propagation Delay (tpd) 33%

**Top attribution features:** leakage drift z-score (+6.809); delay drift z-score (+3.762); leakage z-score @24h (+1.491)

**Evidence:** Leakage Current (Ileak) reads 16.36 µA at 24h against a lot median of 10.67 µA (1.53x lot median) and uses 33% of the 50 µA datasheet limit. Drift is +21.9% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Propagation Delay (tpd).

### Certificate 162 - SN02-0202 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.697

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.43 µA | 25.21 µA | 18.95 µA | 1.33x | 3.2 | 25% |
| Leakage Current (Ileak) | 8.83 µA | 10.79 µA | 6.95 µA | 1.55x | 6.8 | 22% |
| Propagation Delay (tpd) | 10.29 ns | 10.59 ns | 9.82 ns | 1.08x | 1.7 | 71% |

**Parameter contribution:** Standby Current (Iddq) 29%, Leakage Current (Ileak) 49%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage drift z-score (+6.761); Iddq drift z-score (+3.197); delay drift z-score (+1.726)

**Evidence:** Leakage Current (Ileak) reads 10.79 µA at 24h against a lot median of 6.95 µA (1.55x lot median) and uses 22% of the 50 µA datasheet limit. Drift is +22.2% versus a lot-median drift of +4.6%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 163 - SN05-0035 (LOT-E)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.690

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.20 µA | 19.45 µA | 21.74 µA | 0.89x | 0.4 | 19% |
| Leakage Current (Ileak) | 3.70 µA | 4.84 µA | 5.71 µA | 0.85x | 6.6 | 10% |
| Propagation Delay (tpd) | 8.61 ns | 8.88 ns | 8.87 ns | 1.00x | 3.2 | 59% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 64%, Propagation Delay (tpd) 27%

**Top attribution features:** leakage drift z-score (+6.648); delay drift z-score (+3.195); leakage z-score @0h (+0.944)

**Evidence:** Leakage Current (Ileak) reads 4.84 µA at 24h against a lot median of 5.71 µA (0.85x lot median) and uses 10% of the 50 µA datasheet limit. Drift is +30.7% versus a lot-median drift of +6.7%. Coordinated shifts also appear in Propagation Delay (tpd).

### Certificate 164 - SN03-0095 (LOT-C)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.690

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 12.83 µA | 14.53 µA | 0.88x | 0.7 | 13% |
| Leakage Current (Ileak) | 26.98 µA | 31.31 µA | 8.19 µA | 3.82x | 6.6 | 63% |
| Propagation Delay (tpd) | 8.12 ns | 8.20 ns | 8.33 ns | 0.98x | 0.2 | 55% |

**Parameter contribution:** Standby Current (Iddq) 7%, Leakage Current (Ileak) 90%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage z-score @24h (+6.646); leakage z-score @0h (+5.772); leakage drift z-score (+5.306)

**Evidence:** Leakage Current (Ileak) reads 31.31 µA at 24h against a lot median of 8.19 µA (3.82x lot median) and uses 63% of the 50 µA datasheet limit. Drift is +16.0% versus a lot-median drift of +4.4%.

### Certificate 165 - SN08-0058 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.680

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.20 µA | 13.79 µA | 12.78 µA | 1.08x | 6.5 | 14% |
| Leakage Current (Ileak) | 7.24 µA | 7.64 µA | 5.03 µA | 1.52x | 1.3 | 15% |
| Propagation Delay (tpd) | 8.24 ns | 8.37 ns | 8.48 ns | 0.99x | 0.4 | 56% |

**Parameter contribution:** Standby Current (Iddq) 61%, Leakage Current (Ileak) 31%, Propagation Delay (tpd) 9%

**Top attribution features:** Iddq drift z-score (+6.510); leakage z-score @24h (+1.290); leakage z-score @0h (+1.174)

**Evidence:** Standby Current (Iddq) reads 13.79 µA at 24h against a lot median of 12.78 µA (1.08x lot median) and uses 14% of the 100 µA datasheet limit. Drift is +23.1% versus a lot-median drift of +5.2%.

### Certificate 166 - SN02-0076 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.679

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.71 µA | 14.04 µA | 18.95 µA | 0.74x | 1.2 | 14% |
| Leakage Current (Ileak) | 4.64 µA | 4.82 µA | 6.95 µA | 0.69x | 0.8 | 10% |
| Propagation Delay (tpd) | 9.90 ns | 10.59 ns | 9.82 ns | 1.08x | 6.5 | 71% |

**Parameter contribution:** Standby Current (Iddq) 25%, Leakage Current (Ileak) 14%, Propagation Delay (tpd) 62%

**Top attribution features:** delay drift z-score (+6.498); Iddq drift z-score (+1.205); delay z-score @24h (+1.198)

**Evidence:** Propagation Delay (tpd) reads 10.59 ns at 24h against a lot median of 9.82 ns (1.08x lot median) and uses 71% of the 15 ns datasheet limit. Drift is +7.0% versus a lot-median drift of +1.4%.

### Certificate 167 - SN06-0027 (LOT-F)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.675

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.07 µA | 37.25 µA | 21.75 µA | 1.71x | 4.7 | 37% |
| Leakage Current (Ileak) | 11.13 µA | 13.46 µA | 7.94 µA | 1.69x | 6.4 | 27% |
| Propagation Delay (tpd) | 9.99 ns | 10.18 ns | 9.80 ns | 1.04x | 2.2 | 68% |

**Parameter contribution:** Standby Current (Iddq) 38%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+6.433); Iddq drift z-score (+4.655); delay drift z-score (+2.163)

**Evidence:** Leakage Current (Ileak) reads 13.46 µA at 24h against a lot median of 7.94 µA (1.69x lot median) and uses 27% of the 50 µA datasheet limit. Drift is +21.0% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq), Propagation Delay (tpd).

### Certificate 168 - SN02-0104 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.674

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 20.47 µA | 26.48 µA | 18.95 µA | 1.40x | 6.4 | 26% |
| Leakage Current (Ileak) | 9.38 µA | 9.92 µA | 6.95 µA | 1.43x | 1.1 | 20% |
| Propagation Delay (tpd) | 9.83 ns | 10.06 ns | 9.82 ns | 1.02x | 1.1 | 67% |

**Parameter contribution:** Standby Current (Iddq) 66%, Leakage Current (Ileak) 20%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq drift z-score (+6.427); Iddq z-score @24h (+1.413); delay drift z-score (+1.112)

**Evidence:** Standby Current (Iddq) reads 26.48 µA at 24h against a lot median of 18.95 µA (1.40x lot median) and uses 26% of the 100 µA datasheet limit. Drift is +29.3% versus a lot-median drift of +6.1%.

### Certificate 169 - SN01-0219 (LOT-A)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.662

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.60 µA | 25.42 µA | 24.51 µA | 1.04x | 1.8 | 25% |
| Leakage Current (Ileak) | 32.50 µA | 35.47 µA | 9.64 µA | 3.68x | 6.3 | 71% |
| Propagation Delay (tpd) | 8.45 ns | 8.51 ns | 8.46 ns | 1.01x | 0.5 | 57% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 83%, Propagation Delay (tpd) 5%

**Top attribution features:** leakage z-score @24h (+6.267); leakage z-score @0h (+6.227); Iddq drift z-score (+1.801)

**Evidence:** Leakage Current (Ileak) reads 35.47 µA at 24h against a lot median of 9.64 µA (3.68x lot median) and uses 71% of the 50 µA datasheet limit. Drift is +9.1% versus a lot-median drift of +5.1%.

### Certificate 170 - SN03-0060 (LOT-C)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.659

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 14.74 µA | 15.27 µA | 14.53 µA | 1.05x | 0.9 | 15% |
| Leakage Current (Ileak) | 4.91 µA | 5.80 µA | 8.19 µA | 0.71x | 6.2 | 12% |
| Propagation Delay (tpd) | 9.24 ns | 9.30 ns | 8.33 ns | 1.12x | 2.1 | 62% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 57%, Propagation Delay (tpd) 34%

**Top attribution features:** leakage drift z-score (+6.222); delay z-score @0h (+2.142); delay z-score @24h (+1.910)

**Evidence:** Leakage Current (Ileak) reads 5.80 µA at 24h against a lot median of 8.19 µA (0.71x lot median) and uses 12% of the 50 µA datasheet limit. Drift is +18.0% versus a lot-median drift of +4.4%.

### Certificate 171 - SN08-0092 (LOT-H)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.651

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 15.13 µA | 16.24 µA | 12.78 µA | 1.27x | 0.8 | 16% |
| Leakage Current (Ileak) | 15.85 µA | 16.48 µA | 5.03 µA | 3.28x | 5.7 | 33% |
| Propagation Delay (tpd) | 7.70 ns | 7.85 ns | 8.48 ns | 0.93x | 1.9 | 52% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 64%, Propagation Delay (tpd) 25%

**Top attribution features:** leakage z-score @24h (+5.663); leakage z-score @0h (+5.418); delay z-score @0h (+1.919)

**Evidence:** Leakage Current (Ileak) reads 16.48 µA at 24h against a lot median of 5.03 µA (3.28x lot median) and uses 33% of the 50 µA datasheet limit. Drift is +4.0% versus a lot-median drift of +3.5%.

### Certificate 172 - SN01-0158 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.643

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 10.14 µA | 10.74 µA | 24.51 µA | 0.44x | 1.4 | 11% |
| Leakage Current (Ileak) | 3.10 µA | 3.49 µA | 9.64 µA | 0.36x | 2.6 | 7% |
| Propagation Delay (tpd) | 9.48 ns | 9.70 ns | 8.46 ns | 1.15x | 2.5 | 65% |

**Parameter contribution:** Standby Current (Iddq) 23%, Leakage Current (Ileak) 35%, Propagation Delay (tpd) 42%

**Top attribution features:** leakage drift z-score (+2.640); delay z-score @24h (+2.504); delay z-score @0h (+2.452)

**Evidence:** Propagation Delay (tpd) reads 9.70 ns at 24h against a lot median of 8.46 ns (1.15x lot median) and uses 65% of the 15 ns datasheet limit. Drift is +2.3% versus a lot-median drift of +1.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 173 - SN02-0027 (LOT-B)

**Verdict:** REJECT | **Risk:** HIGH | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.643

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 19.29 µA | 18.95 µA | 1.02x | 2.9 | 19% |
| Leakage Current (Ileak) | 20.96 µA | 23.36 µA | 6.95 µA | 3.36x | 6.0 | 47% |
| Propagation Delay (tpd) | 9.55 ns | 9.78 ns | 9.82 ns | 1.00x | 1.1 | 65% |

**Parameter contribution:** Standby Current (Iddq) 17%, Leakage Current (Ileak) 75%, Propagation Delay (tpd) 7%

**Top attribution features:** leakage z-score @24h (+6.015); leakage z-score @0h (+5.500); Iddq drift z-score (+2.904)

**Evidence:** Leakage Current (Ileak) reads 23.36 µA at 24h against a lot median of 6.95 µA (3.36x lot median) and uses 47% of the 50 µA datasheet limit. Drift is +11.4% versus a lot-median drift of +4.6%.

### Certificate 174 - SN04-0007 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.636

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 51.58 µA | 53.28 µA | 17.67 µA | 3.02x | 5.9 | 53% |
| Leakage Current (Ileak) | 5.17 µA | 5.64 µA | 6.43 µA | 0.88x | 0.7 | 11% |
| Propagation Delay (tpd) | 10.01 ns | 10.18 ns | 10.33 ns | 0.99x | 0.4 | 68% |

**Parameter contribution:** Standby Current (Iddq) 85%, Leakage Current (Ileak) 9%, Propagation Delay (tpd) 6%

**Top attribution features:** Iddq z-score @0h (+5.925); Iddq z-score @24h (+5.759); leakage drift z-score (+0.721)

**Evidence:** Standby Current (Iddq) reads 53.28 µA at 24h against a lot median of 17.67 µA (3.02x lot median) and uses 53% of the 100 µA datasheet limit. Drift is +3.3% versus a lot-median drift of +4.5%.

### Certificate 175 - SN04-0157 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.635

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 33.99 µA | 36.36 µA | 17.67 µA | 2.06x | 3.0 | 36% |
| Leakage Current (Ileak) | 6.86 µA | 8.78 µA | 6.43 µA | 1.37x | 5.9 | 18% |
| Propagation Delay (tpd) | 10.61 ns | 10.78 ns | 10.33 ns | 1.04x | 0.7 | 72% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 45%, Propagation Delay (tpd) 11%

**Top attribution features:** leakage drift z-score (+5.920); Iddq z-score @24h (+3.023); Iddq z-score @0h (+2.923)

**Evidence:** Leakage Current (Ileak) reads 8.78 µA at 24h against a lot median of 6.43 µA (1.37x lot median) and uses 18% of the 50 µA datasheet limit. Drift is +28.0% versus a lot-median drift of +6.5%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 176 - SN07-0013 (LOT-G)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.626

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 14.46 µA | 17.85 µA | 17.12 µA | 1.04x | 5.8 | 18% |
| Leakage Current (Ileak) | 6.59 µA | 6.79 µA | 10.67 µA | 0.64x | 1.0 | 14% |
| Propagation Delay (tpd) | 8.98 ns | 9.15 ns | 8.96 ns | 1.02x | 0.6 | 61% |

**Parameter contribution:** Standby Current (Iddq) 60%, Leakage Current (Ileak) 27%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq drift z-score (+5.806); leakage z-score @24h (+1.016); leakage z-score @0h (+0.968)

**Evidence:** Standby Current (Iddq) reads 17.85 µA at 24h against a lot median of 17.12 µA (1.04x lot median) and uses 18% of the 100 µA datasheet limit. Drift is +23.4% versus a lot-median drift of +5.2%.

### Certificate 177 - SN01-0221 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.625

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.94 µA | 18.62 µA | 24.51 µA | 0.76x | 0.6 | 19% |
| Leakage Current (Ileak) | 9.01 µA | 9.72 µA | 9.64 µA | 1.01x | 1.0 | 19% |
| Propagation Delay (tpd) | 8.53 ns | 8.95 ns | 8.46 ns | 1.06x | 5.8 | 60% |

**Parameter contribution:** Standby Current (Iddq) 13%, Leakage Current (Ileak) 11%, Propagation Delay (tpd) 76%

**Top attribution features:** delay drift z-score (+5.789); delay z-score @24h (+0.992); leakage drift z-score (+0.989)

**Evidence:** Propagation Delay (tpd) reads 8.95 ns at 24h against a lot median of 8.46 ns (1.06x lot median) and uses 60% of the 15 ns datasheet limit. Drift is +4.9% versus a lot-median drift of +1.1%.

### Certificate 178 - SN03-0084 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.622

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 6.98 µA | 9.11 µA | 14.53 µA | 0.63x | 5.7 | 9% |
| Leakage Current (Ileak) | 5.11 µA | 5.42 µA | 8.19 µA | 0.66x | 0.8 | 11% |
| Propagation Delay (tpd) | 9.39 ns | 9.58 ns | 8.33 ns | 1.15x | 2.5 | 64% |

**Parameter contribution:** Standby Current (Iddq) 48%, Leakage Current (Ileak) 14%, Propagation Delay (tpd) 38%

**Top attribution features:** Iddq drift z-score (+5.724); delay z-score @24h (+2.469); delay z-score @0h (+2.458)

**Evidence:** Standby Current (Iddq) reads 9.11 µA at 24h against a lot median of 14.53 µA (0.63x lot median) and uses 9% of the 100 µA datasheet limit. Drift is +30.5% versus a lot-median drift of +7.1%.

### Certificate 179 - SN02-0224 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.622

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 10.94 µA | 11.29 µA | 18.95 µA | 0.60x | 1.5 | 11% |
| Leakage Current (Ileak) | 3.21 µA | 3.41 µA | 6.95 µA | 0.49x | 1.3 | 7% |
| Propagation Delay (tpd) | 11.42 ns | 11.74 ns | 9.82 ns | 1.20x | 3.1 | 78% |

**Parameter contribution:** Standby Current (Iddq) 26%, Leakage Current (Ileak) 22%, Propagation Delay (tpd) 53%

**Top attribution features:** delay z-score @0h (+3.111); delay z-score @24h (+3.001); delay drift z-score (+1.648)

**Evidence:** Propagation Delay (tpd) reads 11.74 ns at 24h against a lot median of 9.82 ns (1.20x lot median) and uses 78% of the 15 ns datasheet limit. Drift is +2.8% versus a lot-median drift of +1.4%.

### Certificate 180 - SN03-0051 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.613

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 26.56 µA | 27.21 µA | 14.53 µA | 1.87x | 2.8 | 27% |
| Leakage Current (Ileak) | 26.07 µA | 27.21 µA | 8.19 µA | 3.32x | 5.5 | 54% |
| Propagation Delay (tpd) | 8.36 ns | 8.40 ns | 8.33 ns | 1.01x | 0.8 | 56% |

**Parameter contribution:** Standby Current (Iddq) 35%, Leakage Current (Ileak) 59%, Propagation Delay (tpd) 7%

**Top attribution features:** leakage z-score @0h (+5.497); leakage z-score @24h (+5.469); Iddq z-score @0h (+2.821)

**Evidence:** Leakage Current (Ileak) reads 27.21 µA at 24h against a lot median of 8.19 µA (3.32x lot median) and uses 54% of the 50 µA datasheet limit. Drift is +4.4% versus a lot-median drift of +4.4%.

### Certificate 181 - SN03-0075 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.611

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 17.52 µA | 18.83 µA | 14.53 µA | 1.30x | 0.9 | 19% |
| Leakage Current (Ileak) | 18.87 µA | 19.67 µA | 8.19 µA | 2.40x | 3.3 | 39% |
| Propagation Delay (tpd) | 6.78 ns | 6.84 ns | 8.33 ns | 0.82x | 3.1 | 46% |

**Parameter contribution:** Standby Current (Iddq) 12%, Leakage Current (Ileak) 46%, Propagation Delay (tpd) 42%

**Top attribution features:** leakage z-score @0h (+3.324); leakage z-score @24h (+3.300); delay z-score @0h (+3.051)

**Evidence:** Leakage Current (Ileak) reads 19.67 µA at 24h against a lot median of 8.19 µA (2.40x lot median) and uses 39% of the 50 µA datasheet limit. Drift is +4.2% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Propagation Delay (tpd).

### Certificate 182 - SN08-0023 (LOT-H)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.610

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 41.81 µA | 44.99 µA | 12.78 µA | 3.52x | 5.6 | 45% |
| Leakage Current (Ileak) | 4.65 µA | 4.78 µA | 5.03 µA | 0.95x | 0.3 | 10% |
| Propagation Delay (tpd) | 8.47 ns | 8.64 ns | 8.48 ns | 1.02x | 0.9 | 58% |

**Parameter contribution:** Standby Current (Iddq) 84%, Leakage Current (Ileak) 4%, Propagation Delay (tpd) 12%

**Top attribution features:** Iddq z-score @0h (+5.613); Iddq z-score @24h (+5.558); delay drift z-score (+0.883)

**Evidence:** Standby Current (Iddq) reads 44.99 µA at 24h against a lot median of 12.78 µA (3.52x lot median) and uses 45% of the 100 µA datasheet limit. Drift is +7.6% versus a lot-median drift of +5.2%.

### Certificate 183 - SN08-0174 (LOT-H)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.605

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 33.54 µA | 35.63 µA | 12.78 µA | 2.79x | 4.1 | 36% |
| Leakage Current (Ileak) | 12.45 µA | 13.16 µA | 5.03 µA | 2.62x | 4.0 | 26% |
| Propagation Delay (tpd) | 7.95 ns | 8.07 ns | 8.48 ns | 0.95x | 1.2 | 54% |

**Parameter contribution:** Standby Current (Iddq) 42%, Leakage Current (Ileak) 45%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq z-score @0h (+4.058); leakage z-score @24h (+4.021); Iddq z-score @24h (+3.943)

**Evidence:** Leakage Current (Ileak) reads 13.16 µA at 24h against a lot median of 5.03 µA (2.62x lot median) and uses 26% of the 50 µA datasheet limit. Drift is +5.7% versus a lot-median drift of +3.5%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 184 - SN02-0255 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.601

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 14.89 µA | 16.29 µA | 18.95 µA | 0.86x | 0.9 | 16% |
| Leakage Current (Ileak) | 4.40 µA | 5.23 µA | 6.95 µA | 0.75x | 5.5 | 10% |
| Propagation Delay (tpd) | 10.43 ns | 10.49 ns | 9.82 ns | 1.07x | 1.4 | 70% |

**Parameter contribution:** Standby Current (Iddq) 16%, Leakage Current (Ileak) 56%, Propagation Delay (tpd) 27%

**Top attribution features:** leakage drift z-score (+5.513); delay z-score @0h (+1.363); delay z-score @24h (+1.050)

**Evidence:** Leakage Current (Ileak) reads 5.23 µA at 24h against a lot median of 6.95 µA (0.75x lot median) and uses 10% of the 50 µA datasheet limit. Drift is +18.9% versus a lot-median drift of +4.6%.

### Certificate 185 - SN07-0034 (LOT-G)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.597

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.45 µA | 26.54 µA | 17.12 µA | 1.55x | 2.5 | 27% |
| Leakage Current (Ileak) | 16.50 µA | 19.57 µA | 10.67 µA | 1.83x | 5.5 | 39% |
| Propagation Delay (tpd) | 8.92 ns | 9.05 ns | 8.96 ns | 1.01x | 0.2 | 60% |

**Parameter contribution:** Standby Current (Iddq) 37%, Leakage Current (Ileak) 60%, Propagation Delay (tpd) 3%

**Top attribution features:** leakage drift z-score (+5.466); Iddq drift z-score (+2.535); leakage z-score @24h (+2.331)

**Evidence:** Leakage Current (Ileak) reads 19.57 µA at 24h against a lot median of 10.67 µA (1.83x lot median) and uses 39% of the 50 µA datasheet limit. Drift is +18.6% versus a lot-median drift of +5.0%.

### Certificate 186 - SN04-0208 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.594

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.93 µA | 19.60 µA | 17.67 µA | 1.11x | 0.4 | 20% |
| Leakage Current (Ileak) | 7.74 µA | 9.35 µA | 6.43 µA | 1.45x | 4.0 | 19% |
| Propagation Delay (tpd) | 9.76 ns | 10.33 ns | 10.33 ns | 1.00x | 5.4 | 69% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 44%, Propagation Delay (tpd) 48%

**Top attribution features:** delay drift z-score (+5.436); leakage drift z-score (+3.963); leakage z-score @24h (+1.036)

**Evidence:** Propagation Delay (tpd) reads 10.33 ns at 24h against a lot median of 10.33 ns (1.00x lot median) and uses 69% of the 15 ns datasheet limit. Drift is +5.9% versus a lot-median drift of +1.4%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 187 - SN04-0073 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.594

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 23.24 µA | 25.85 µA | 17.67 µA | 1.46x | 2.6 | 26% |
| Leakage Current (Ileak) | 4.67 µA | 5.59 µA | 6.43 µA | 0.87x | 3.6 | 11% |
| Propagation Delay (tpd) | 10.46 ns | 11.08 ns | 10.33 ns | 1.07x | 5.4 | 74% |

**Parameter contribution:** Standby Current (Iddq) 31%, Leakage Current (Ileak) 27%, Propagation Delay (tpd) 42%

**Top attribution features:** delay drift z-score (+5.436); leakage drift z-score (+3.630); Iddq drift z-score (+2.622)

**Evidence:** Propagation Delay (tpd) reads 11.08 ns at 24h against a lot median of 10.33 ns (1.07x lot median) and uses 74% of the 15 ns datasheet limit. Drift is +5.9% versus a lot-median drift of +1.4%. Coordinated shifts also appear in Standby Current (Iddq), Leakage Current (Ileak).

### Certificate 188 - SN05-0013 (LOT-E)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.589

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.12 µA | 31.69 µA | 21.74 µA | 1.46x | 1.7 | 32% |
| Leakage Current (Ileak) | 13.63 µA | 16.20 µA | 5.71 µA | 2.84x | 5.4 | 32% |
| Propagation Delay (tpd) | 8.45 ns | 8.56 ns | 8.87 ns | 0.96x | 0.6 | 57% |

**Parameter contribution:** Standby Current (Iddq) 21%, Leakage Current (Ileak) 72%, Propagation Delay (tpd) 7%

**Top attribution features:** leakage z-score @24h (+5.380); leakage z-score @0h (+4.727); leakage drift z-score (+3.359)

**Evidence:** Leakage Current (Ileak) reads 16.20 µA at 24h against a lot median of 5.71 µA (2.84x lot median) and uses 32% of the 50 µA datasheet limit. Drift is +18.8% versus a lot-median drift of +6.7%.

### Certificate 189 - SN08-0159 (LOT-H)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.583

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.76 µA | 12.86 µA | 12.78 µA | 1.01x | 1.5 | 13% |
| Leakage Current (Ileak) | 15.41 µA | 15.78 µA | 5.03 µA | 3.14x | 5.3 | 32% |
| Propagation Delay (tpd) | 8.67 ns | 8.78 ns | 8.48 ns | 1.04x | 1.0 | 59% |

**Parameter contribution:** Standby Current (Iddq) 11%, Leakage Current (Ileak) 76%, Propagation Delay (tpd) 13%

**Top attribution features:** leakage z-score @24h (+5.319); leakage z-score @0h (+5.199); Iddq drift z-score (+1.535)

**Evidence:** Leakage Current (Ileak) reads 15.78 µA at 24h against a lot median of 5.03 µA (3.14x lot median) and uses 32% of the 50 µA datasheet limit. Drift is +2.4% versus a lot-median drift of +3.5%.

### Certificate 190 - SN04-0123 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.579

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.46 µA | 14.72 µA | 17.67 µA | 0.83x | 5.3 | 15% |
| Leakage Current (Ileak) | 11.67 µA | 12.26 µA | 6.43 µA | 1.91x | 2.2 | 25% |
| Propagation Delay (tpd) | 10.15 ns | 10.46 ns | 10.33 ns | 1.01x | 2.0 | 70% |

**Parameter contribution:** Standby Current (Iddq) 49%, Leakage Current (Ileak) 35%, Propagation Delay (tpd) 17%

**Top attribution features:** Iddq drift z-score (+5.269); leakage z-score @0h (+2.213); leakage z-score @24h (+2.067)

**Evidence:** Standby Current (Iddq) reads 14.72 µA at 24h against a lot median of 17.67 µA (0.83x lot median) and uses 15% of the 100 µA datasheet limit. Drift is +18.1% versus a lot-median drift of +4.5%.

### Certificate 191 - SN02-0031 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.579

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 17.42 µA | 18.95 µA | 0.92x | 0.3 | 17% |
| Leakage Current (Ileak) | 19.76 µA | 21.32 µA | 6.95 µA | 3.07x | 5.3 | 43% |
| Propagation Delay (tpd) | 10.17 ns | 10.37 ns | 9.82 ns | 1.06x | 0.9 | 69% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 79%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage z-score @24h (+5.269); leakage z-score @0h (+5.042); leakage drift z-score (+1.267)

**Evidence:** Leakage Current (Ileak) reads 21.32 µA at 24h against a lot median of 6.95 µA (3.07x lot median) and uses 43% of the 50 µA datasheet limit. Drift is +7.9% versus a lot-median drift of +4.6%.

### Certificate 192 - SN04-0244 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.574

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.42 µA | 19.05 µA | 17.67 µA | 1.08x | 0.4 | 19% |
| Leakage Current (Ileak) | 16.39 µA | 20.56 µA | 6.43 µA | 3.20x | 5.2 | 41% |
| Propagation Delay (tpd) | 9.86 ns | 9.90 ns | 10.33 ns | 0.96x | 1.1 | 66% |

**Parameter contribution:** Standby Current (Iddq) 5%, Leakage Current (Ileak) 82%, Propagation Delay (tpd) 13%

**Top attribution features:** leakage drift z-score (+5.218); leakage z-score @24h (+5.005); leakage z-score @0h (+4.053)

**Evidence:** Leakage Current (Ileak) reads 20.56 µA at 24h against a lot median of 6.43 µA (3.20x lot median) and uses 41% of the 50 µA datasheet limit. Drift is +25.4% versus a lot-median drift of +6.5%.

### Certificate 193 - SN03-0254 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.569

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.31 µA | 13.81 µA | 14.53 µA | 0.95x | 1.2 | 14% |
| Leakage Current (Ileak) | 24.20 µA | 26.18 µA | 8.19 µA | 3.20x | 5.2 | 52% |
| Propagation Delay (tpd) | 8.57 ns | 8.60 ns | 8.33 ns | 1.03x | 1.0 | 57% |

**Parameter contribution:** Standby Current (Iddq) 10%, Leakage Current (Ileak) 75%, Propagation Delay (tpd) 14%

**Top attribution features:** leakage z-score @24h (+5.171); leakage z-score @0h (+4.932); leakage drift z-score (+1.724)

**Evidence:** Leakage Current (Ileak) reads 26.18 µA at 24h against a lot median of 8.19 µA (3.20x lot median) and uses 52% of the 50 µA datasheet limit. Drift is +8.2% versus a lot-median drift of +4.4%.

### Certificate 194 - SN03-0101 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.568

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 11.45 µA | 14.68 µA | 14.53 µA | 1.01x | 5.2 | 15% |
| Leakage Current (Ileak) | 6.82 µA | 6.96 µA | 8.19 µA | 0.85x | 1.1 | 14% |
| Propagation Delay (tpd) | 8.13 ns | 8.17 ns | 8.33 ns | 0.98x | 0.7 | 54% |

**Parameter contribution:** Standby Current (Iddq) 66%, Leakage Current (Ileak) 20%, Propagation Delay (tpd) 14%

**Top attribution features:** Iddq drift z-score (+5.154); leakage drift z-score (+1.061); delay drift z-score (+0.739)

**Evidence:** Standby Current (Iddq) reads 14.68 µA at 24h against a lot median of 14.53 µA (1.01x lot median) and uses 15% of the 100 µA datasheet limit. Drift is +28.2% versus a lot-median drift of +7.1%.

### Certificate 195 - SN01-0052 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.564

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 58.74 µA | 64.04 µA | 24.51 µA | 2.61x | 3.9 | 64% |
| Leakage Current (Ileak) | 10.27 µA | 10.71 µA | 9.64 µA | 1.11x | 0.3 | 21% |
| Propagation Delay (tpd) | 7.42 ns | 7.47 ns | 8.46 ns | 0.88x | 2.0 | 50% |

**Parameter contribution:** Standby Current (Iddq) 65%, Leakage Current (Ileak) 6%, Propagation Delay (tpd) 30%

**Top attribution features:** Iddq z-score @24h (+3.917); Iddq z-score @0h (+3.645); Iddq drift z-score (+2.404)

**Evidence:** Standby Current (Iddq) reads 64.04 µA at 24h against a lot median of 24.51 µA (2.61x lot median) and uses 64% of the 100 µA datasheet limit. Drift is +9.0% versus a lot-median drift of +3.8%.

### Certificate 196 - SN03-0022 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.561

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 13.65 µA | 17.41 µA | 14.53 µA | 1.20x | 5.0 | 17% |
| Leakage Current (Ileak) | 8.88 µA | 10.26 µA | 8.19 µA | 1.25x | 5.1 | 21% |
| Propagation Delay (tpd) | 8.64 ns | 8.77 ns | 8.33 ns | 1.05x | 0.9 | 58% |

**Parameter contribution:** Standby Current (Iddq) 40%, Leakage Current (Ileak) 43%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+5.089); Iddq drift z-score (+4.992); delay z-score @0h (+0.880)

**Evidence:** Leakage Current (Ileak) reads 10.26 µA at 24h against a lot median of 8.19 µA (1.25x lot median) and uses 21% of the 50 µA datasheet limit. Drift is +15.6% versus a lot-median drift of +4.4%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 197 - SN04-0040 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.556

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 43.43 µA | 48.82 µA | 17.67 µA | 2.76x | 5.0 | 49% |
| Leakage Current (Ileak) | 5.79 µA | 6.00 µA | 6.43 µA | 0.93x | 0.8 | 12% |
| Propagation Delay (tpd) | 10.35 ns | 10.42 ns | 10.33 ns | 1.01x | 0.7 | 69% |

**Parameter contribution:** Standby Current (Iddq) 85%, Leakage Current (Ileak) 7%, Propagation Delay (tpd) 8%

**Top attribution features:** Iddq z-score @24h (+5.038); Iddq z-score @0h (+4.534); Iddq drift z-score (+3.070)

**Evidence:** Standby Current (Iddq) reads 48.82 µA at 24h against a lot median of 17.67 µA (2.76x lot median) and uses 49% of the 100 µA datasheet limit. Drift is +12.4% versus a lot-median drift of +4.5%.

### Certificate 198 - SN08-0149 (LOT-H)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.556

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 22.60 µA | 23.93 µA | 12.78 µA | 1.87x | 2.0 | 24% |
| Leakage Current (Ileak) | 6.09 µA | 6.91 µA | 5.03 µA | 1.37x | 5.0 | 14% |
| Propagation Delay (tpd) | 8.28 ns | 8.50 ns | 8.48 ns | 1.00x | 1.7 | 57% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 52%, Propagation Delay (tpd) 15%

**Top attribution features:** leakage drift z-score (+5.035); Iddq z-score @0h (+2.000); Iddq z-score @24h (+1.924)

**Evidence:** Leakage Current (Ileak) reads 6.91 µA at 24h against a lot median of 5.03 µA (1.37x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +13.5% versus a lot-median drift of +3.5%.

### Certificate 199 - SN07-0031 (LOT-G)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.555

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 18.42 µA | 19.44 µA | 17.12 µA | 1.14x | 0.5 | 19% |
| Leakage Current (Ileak) | 6.65 µA | 7.81 µA | 10.67 µA | 0.73x | 5.0 | 16% |
| Propagation Delay (tpd) | 8.48 ns | 8.75 ns | 8.96 ns | 0.98x | 2.3 | 58% |

**Parameter contribution:** Standby Current (Iddq) 9%, Leakage Current (Ileak) 59%, Propagation Delay (tpd) 31%

**Top attribution features:** leakage drift z-score (+5.024); delay drift z-score (+2.276); leakage z-score @0h (+0.950)

**Evidence:** Leakage Current (Ileak) reads 7.81 µA at 24h against a lot median of 10.67 µA (0.73x lot median) and uses 16% of the 50 µA datasheet limit. Drift is +17.5% versus a lot-median drift of +5.0%.

### Certificate 200 - SN02-0072 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.551

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.50 µA | 36.60 µA | 18.95 µA | 1.93x | 5.0 | 37% |
| Leakage Current (Ileak) | 9.26 µA | 10.89 µA | 6.95 µA | 1.57x | 5.0 | 22% |
| Propagation Delay (tpd) | 9.69 ns | 9.82 ns | 9.82 ns | 1.00x | 0.1 | 65% |

**Parameter contribution:** Standby Current (Iddq) 59%, Leakage Current (Ileak) 40%, Propagation Delay (tpd) 1%

**Top attribution features:** leakage drift z-score (+4.986); Iddq drift z-score (+4.967); Iddq z-score @24h (+3.313)

**Evidence:** Standby Current (Iddq) reads 36.60 µA at 24h against a lot median of 18.95 µA (1.93x lot median) and uses 37% of the 100 µA datasheet limit. Drift is +24.1% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 201 - SN08-0102 (LOT-H)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.548

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 9.23 µA | 10.97 µA | 12.78 µA | 0.86x | 4.9 | 11% |
| Leakage Current (Ileak) | 4.61 µA | 5.01 µA | 5.03 µA | 1.00x | 2.5 | 10% |
| Propagation Delay (tpd) | 8.30 ns | 8.45 ns | 8.48 ns | 1.00x | 0.6 | 56% |

**Parameter contribution:** Standby Current (Iddq) 63%, Leakage Current (Ileak) 29%, Propagation Delay (tpd) 9%

**Top attribution features:** Iddq drift z-score (+4.950); leakage drift z-score (+2.521); delay drift z-score (+0.600)

**Evidence:** Standby Current (Iddq) reads 10.97 µA at 24h against a lot median of 12.78 µA (0.86x lot median) and uses 11% of the 100 µA datasheet limit. Drift is +18.8% versus a lot-median drift of +5.2%.

### Certificate 202 - SN06-0077 (LOT-F)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.547

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.10 µA | 25.49 µA | 21.75 µA | 1.17x | 4.9 | 25% |
| Leakage Current (Ileak) | 7.66 µA | 7.97 µA | 7.94 µA | 1.00x | 0.1 | 16% |
| Propagation Delay (tpd) | 10.37 ns | 10.46 ns | 9.80 ns | 1.07x | 1.3 | 70% |

**Parameter contribution:** Standby Current (Iddq) 65%, Leakage Current (Ileak) 2%, Propagation Delay (tpd) 33%

**Top attribution features:** Iddq drift z-score (+4.946); delay z-score @0h (+1.305); delay z-score @24h (+1.304)

**Evidence:** Standby Current (Iddq) reads 25.49 µA at 24h against a lot median of 21.75 µA (1.17x lot median) and uses 25% of the 100 µA datasheet limit. Drift is +20.8% versus a lot-median drift of +5.3%.

### Certificate 203 - SN01-0215 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.541

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 36.21 µA | 37.82 µA | 24.51 µA | 1.54x | 1.3 | 38% |
| Leakage Current (Ileak) | 27.46 µA | 28.44 µA | 9.64 µA | 2.95x | 4.9 | 57% |
| Propagation Delay (tpd) | 8.03 ns | 8.06 ns | 8.46 ns | 0.95x | 1.1 | 54% |

**Parameter contribution:** Standby Current (Iddq) 19%, Leakage Current (Ileak) 65%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage z-score @0h (+4.889); leakage z-score @24h (+4.562); Iddq z-score @24h (+1.318)

**Evidence:** Leakage Current (Ileak) reads 28.44 µA at 24h against a lot median of 9.64 µA (2.95x lot median) and uses 57% of the 50 µA datasheet limit. Drift is +3.6% versus a lot-median drift of +5.1%.

### Certificate 204 - SN06-0139 (LOT-F)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.534

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 57.54 µA | 61.91 µA | 21.75 µA | 2.85x | 4.8 | 62% |
| Leakage Current (Ileak) | 13.36 µA | 13.63 µA | 7.94 µA | 1.72x | 2.0 | 27% |
| Propagation Delay (tpd) | 9.35 ns | 9.39 ns | 9.80 ns | 0.96x | 0.8 | 63% |

**Parameter contribution:** Standby Current (Iddq) 59%, Leakage Current (Ileak) 28%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq z-score @24h (+4.817); Iddq z-score @0h (+4.796); leakage z-score @0h (+2.013)

**Evidence:** Standby Current (Iddq) reads 61.91 µA at 24h against a lot median of 21.75 µA (2.85x lot median) and uses 62% of the 100 µA datasheet limit. Drift is +7.6% versus a lot-median drift of +5.3%.

### Certificate 205 - SN07-0101 (LOT-G)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.533

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 12.63 µA | 14.54 µA | 17.12 µA | 0.85x | 3.1 | 15% |
| Leakage Current (Ileak) | 7.43 µA | 8.69 µA | 10.67 µA | 0.81x | 4.8 | 17% |
| Propagation Delay (tpd) | 9.39 ns | 9.51 ns | 8.96 ns | 1.06x | 1.3 | 63% |

**Parameter contribution:** Standby Current (Iddq) 34%, Leakage Current (Ileak) 47%, Propagation Delay (tpd) 20%

**Top attribution features:** leakage drift z-score (+4.806); Iddq drift z-score (+3.143); delay z-score @0h (+1.272)

**Evidence:** Leakage Current (Ileak) reads 8.69 µA at 24h against a lot median of 10.67 µA (0.81x lot median) and uses 17% of the 50 µA datasheet limit. Drift is +16.9% versus a lot-median drift of +5.0%. Coordinated shifts also appear in Standby Current (Iddq).

### Certificate 206 - SN04-0207 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.531

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 32.51 µA | 37.99 µA | 17.67 µA | 2.15x | 4.8 | 38% |
| Leakage Current (Ileak) | 8.36 µA | 9.86 µA | 6.43 µA | 1.53x | 3.2 | 20% |
| Propagation Delay (tpd) | 9.84 ns | 10.14 ns | 10.33 ns | 0.98x | 2.0 | 68% |

**Parameter contribution:** Standby Current (Iddq) 57%, Leakage Current (Ileak) 28%, Propagation Delay (tpd) 15%

**Top attribution features:** Iddq drift z-score (+4.792); Iddq z-score @24h (+3.287); leakage drift z-score (+3.161)

**Evidence:** Standby Current (Iddq) reads 37.99 µA at 24h against a lot median of 17.67 µA (2.15x lot median) and uses 38% of the 100 µA datasheet limit. Drift is +16.9% versus a lot-median drift of +4.5%. Coordinated shifts also appear in Leakage Current (Ileak), Propagation Delay (tpd).

### Certificate 207 - SN02-0125 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.529

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.54 µA | 18.02 µA | 18.95 µA | 0.95x | 0.8 | 18% |
| Leakage Current (Ileak) | 18.51 µA | 19.96 µA | 6.95 µA | 2.87x | 4.8 | 40% |
| Propagation Delay (tpd) | 10.79 ns | 10.92 ns | 9.82 ns | 1.11x | 2.0 | 73% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 67%, Propagation Delay (tpd) 25%

**Top attribution features:** leakage z-score @24h (+4.769); leakage z-score @0h (+4.567); delay z-score @0h (+1.999)

**Evidence:** Leakage Current (Ileak) reads 19.96 µA at 24h against a lot median of 6.95 µA (2.87x lot median) and uses 40% of the 50 µA datasheet limit. Drift is +7.8% versus a lot-median drift of +4.6%.

### Certificate 208 - SN02-0057 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `MULTIVARIATE_LATENT_DRIFT` | **Confidence:** 0.525

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 34.56 µA | 36.51 µA | 18.95 µA | 1.93x | 3.8 | 37% |
| Leakage Current (Ileak) | 3.95 µA | 4.62 µA | 6.95 µA | 0.67x | 4.7 | 9% |
| Propagation Delay (tpd) | 10.05 ns | 10.31 ns | 9.82 ns | 1.05x | 1.4 | 69% |

**Parameter contribution:** Standby Current (Iddq) 44%, Leakage Current (Ileak) 39%, Propagation Delay (tpd) 17%

**Top attribution features:** leakage drift z-score (+4.735); Iddq z-score @0h (+3.823); Iddq z-score @24h (+3.297)

**Evidence:** Standby Current (Iddq) reads 36.51 µA at 24h against a lot median of 18.95 µA (1.93x lot median) and uses 37% of the 100 µA datasheet limit. Drift is +5.6% versus a lot-median drift of +6.1%. Coordinated shifts also appear in Leakage Current (Ileak).

### Certificate 209 - SN01-0191 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.524

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 24.46 µA | 24.90 µA | 24.51 µA | 1.02x | 0.9 | 25% |
| Leakage Current (Ileak) | 26.84 µA | 27.72 µA | 9.64 µA | 2.88x | 4.7 | 55% |
| Propagation Delay (tpd) | 8.06 ns | 8.12 ns | 8.46 ns | 0.96x | 0.7 | 54% |

**Parameter contribution:** Standby Current (Iddq) 8%, Leakage Current (Ileak) 77%, Propagation Delay (tpd) 15%

**Top attribution features:** leakage z-score @0h (+4.724); leakage z-score @24h (+4.388); Iddq drift z-score (+0.942)

**Evidence:** Leakage Current (Ileak) reads 27.72 µA at 24h against a lot median of 9.64 µA (2.88x lot median) and uses 55% of the 50 µA datasheet limit. Drift is +3.3% versus a lot-median drift of +5.1%.

### Certificate 210 - SN06-0004 (LOT-F)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.524

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.00 µA | 16.72 µA | 21.75 µA | 0.77x | 0.6 | 17% |
| Leakage Current (Ileak) | 10.35 µA | 12.07 µA | 7.94 µA | 1.52x | 4.7 | 24% |
| Propagation Delay (tpd) | 9.24 ns | 9.33 ns | 9.80 ns | 0.95x | 1.0 | 62% |

**Parameter contribution:** Standby Current (Iddq) 13%, Leakage Current (Ileak) 65%, Propagation Delay (tpd) 22%

**Top attribution features:** leakage drift z-score (+4.717); leakage z-score @24h (+1.389); delay z-score @0h (+1.006)

**Evidence:** Leakage Current (Ileak) reads 12.07 µA at 24h against a lot median of 7.94 µA (1.52x lot median) and uses 24% of the 50 µA datasheet limit. Drift is +16.6% versus a lot-median drift of +4.4%.

### Certificate 211 - SN02-0248 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.521

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 13.04 µA | 13.62 µA | 18.95 µA | 0.72x | 1.0 | 14% |
| Leakage Current (Ileak) | 6.16 µA | 7.19 µA | 6.95 µA | 1.03x | 4.7 | 14% |
| Propagation Delay (tpd) | 9.16 ns | 9.38 ns | 9.82 ns | 0.96x | 1.2 | 63% |

**Parameter contribution:** Standby Current (Iddq) 24%, Leakage Current (Ileak) 48%, Propagation Delay (tpd) 28%

**Top attribution features:** leakage drift z-score (+4.693); delay drift z-score (+1.237); Iddq z-score @0h (+1.028)

**Evidence:** Leakage Current (Ileak) reads 7.19 µA at 24h against a lot median of 6.95 µA (1.03x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +16.8% versus a lot-median drift of +4.6%.

### Certificate 212 - SN03-0160 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.520

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 6.32 µA | 6.90 µA | 14.53 µA | 0.47x | 1.6 | 7% |
| Leakage Current (Ileak) | 6.28 µA | 7.20 µA | 8.19 µA | 0.88x | 4.7 | 14% |
| Propagation Delay (tpd) | 8.34 ns | 8.49 ns | 8.33 ns | 1.02x | 1.2 | 57% |

**Parameter contribution:** Standby Current (Iddq) 33%, Leakage Current (Ileak) 51%, Propagation Delay (tpd) 16%

**Top attribution features:** leakage drift z-score (+4.685); Iddq z-score @0h (+1.555); Iddq z-score @24h (+1.518)

**Evidence:** Leakage Current (Ileak) reads 7.20 µA at 24h against a lot median of 8.19 µA (0.88x lot median) and uses 14% of the 50 µA datasheet limit. Drift is +14.7% versus a lot-median drift of +4.4%.

### Certificate 213 - SN03-0150 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.519

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 24.54 µA | 30.98 µA | 14.53 µA | 2.13x | 4.7 | 31% |
| Leakage Current (Ileak) | 11.08 µA | 11.52 µA | 8.19 µA | 1.41x | 1.0 | 23% |
| Propagation Delay (tpd) | 7.71 ns | 7.77 ns | 8.33 ns | 0.93x | 1.1 | 52% |

**Parameter contribution:** Standby Current (Iddq) 69%, Leakage Current (Ileak) 14%, Propagation Delay (tpd) 17%

**Top attribution features:** Iddq drift z-score (+4.672); Iddq z-score @24h (+3.272); Iddq z-score @0h (+2.385)

**Evidence:** Standby Current (Iddq) reads 30.98 µA at 24h against a lot median of 14.53 µA (2.13x lot median) and uses 31% of the 100 µA datasheet limit. Drift is +26.2% versus a lot-median drift of +7.1%.

### Certificate 214 - SN06-0124 (LOT-F)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.517

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 56.20 µA | 60.60 µA | 21.75 µA | 2.79x | 4.7 | 61% |
| Leakage Current (Ileak) | 8.84 µA | 9.56 µA | 7.94 µA | 1.20x | 1.4 | 19% |
| Propagation Delay (tpd) | 9.12 ns | 9.22 ns | 9.80 ns | 0.94x | 1.2 | 61% |

**Parameter contribution:** Standby Current (Iddq) 66%, Leakage Current (Ileak) 16%, Propagation Delay (tpd) 19%

**Top attribution features:** Iddq z-score @24h (+4.660); Iddq z-score @0h (+4.624); leakage drift z-score (+1.445)

**Evidence:** Standby Current (Iddq) reads 60.60 µA at 24h against a lot median of 21.75 µA (2.79x lot median) and uses 61% of the 100 µA datasheet limit. Drift is +7.8% versus a lot-median drift of +5.3%.

### Certificate 215 - SN06-0135 (LOT-F)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.517

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 39.95 µA | 47.88 µA | 21.75 µA | 2.20x | 4.7 | 48% |
| Leakage Current (Ileak) | 5.65 µA | 6.05 µA | 7.94 µA | 0.76x | 1.0 | 12% |
| Propagation Delay (tpd) | 10.13 ns | 10.27 ns | 9.80 ns | 1.05x | 1.1 | 68% |

**Parameter contribution:** Standby Current (Iddq) 67%, Leakage Current (Ileak) 15%, Propagation Delay (tpd) 18%

**Top attribution features:** Iddq drift z-score (+4.653); Iddq z-score @24h (+3.134); Iddq z-score @0h (+2.526)

**Evidence:** Standby Current (Iddq) reads 47.88 µA at 24h against a lot median of 21.75 µA (2.20x lot median) and uses 48% of the 100 µA datasheet limit. Drift is +19.9% versus a lot-median drift of +5.3%.

### Certificate 216 - SN03-0005 (LOT-C)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.517

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 16.63 µA | 20.98 µA | 14.53 µA | 1.44x | 4.7 | 21% |
| Leakage Current (Ileak) | 10.34 µA | 10.74 µA | 8.19 µA | 1.31x | 0.7 | 21% |
| Propagation Delay (tpd) | 8.28 ns | 8.42 ns | 8.33 ns | 1.01x | 1.0 | 56% |

**Parameter contribution:** Standby Current (Iddq) 69%, Leakage Current (Ileak) 18%, Propagation Delay (tpd) 13%

**Top attribution features:** Iddq drift z-score (+4.653); Iddq z-score @24h (+1.284); delay drift z-score (+0.959)

**Evidence:** Standby Current (Iddq) reads 20.98 µA at 24h against a lot median of 14.53 µA (1.44x lot median) and uses 21% of the 100 µA datasheet limit. Drift is +26.1% versus a lot-median drift of +7.1%.

### Certificate 217 - SN01-0206 (LOT-A)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.517

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 27.30 µA | 29.02 µA | 24.51 µA | 1.18x | 1.2 | 29% |
| Leakage Current (Ileak) | 6.74 µA | 7.99 µA | 9.64 µA | 0.83x | 4.7 | 16% |
| Propagation Delay (tpd) | 7.82 ns | 7.96 ns | 8.46 ns | 0.94x | 1.1 | 53% |

**Parameter contribution:** Standby Current (Iddq) 18%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 29%

**Top attribution features:** leakage drift z-score (+4.653); Iddq drift z-score (+1.150); delay z-score @0h (+1.115)

**Evidence:** Leakage Current (Ileak) reads 7.99 µA at 24h against a lot median of 9.64 µA (0.83x lot median) and uses 16% of the 50 µA datasheet limit. Drift is +18.6% versus a lot-median drift of +5.1%.

### Certificate 218 - SN02-0193 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.516

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 21.00 µA | 22.99 µA | 18.95 µA | 1.21x | 0.9 | 23% |
| Leakage Current (Ileak) | 13.67 µA | 14.41 µA | 6.95 µA | 2.07x | 2.7 | 29% |
| Propagation Delay (tpd) | 7.71 ns | 7.88 ns | 9.82 ns | 0.80x | 3.5 | 53% |

**Parameter contribution:** Standby Current (Iddq) 16%, Leakage Current (Ileak) 37%, Propagation Delay (tpd) 48%

**Top attribution features:** delay z-score @0h (+3.462); delay z-score @24h (+3.034); leakage z-score @24h (+2.736)

**Evidence:** Propagation Delay (tpd) reads 7.88 ns at 24h against a lot median of 9.82 ns (0.80x lot median) and uses 53% of the 15 ns datasheet limit. Drift is +2.3% versus a lot-median drift of +1.4%.

### Certificate 219 - SN04-0273 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.515

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 13.34 µA | 14.35 µA | 17.67 µA | 0.81x | 1.2 | 14% |
| Leakage Current (Ileak) | 7.12 µA | 7.65 µA | 6.43 µA | 1.19x | 0.4 | 15% |
| Propagation Delay (tpd) | 10.83 ns | 11.39 ns | 10.33 ns | 1.10x | 4.6 | 76% |

**Parameter contribution:** Standby Current (Iddq) 22%, Leakage Current (Ileak) 11%, Propagation Delay (tpd) 67%

**Top attribution features:** delay drift z-score (+4.641); delay z-score @24h (+1.544); Iddq drift z-score (+1.213)

**Evidence:** Propagation Delay (tpd) reads 11.39 ns at 24h against a lot median of 10.33 ns (1.10x lot median) and uses 76% of the 15 ns datasheet limit. Drift is +5.2% versus a lot-median drift of +1.4%.

### Certificate 220 - SN02-0167 (LOT-B)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.509

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 9.43 µA | 10.63 µA | 18.95 µA | 0.56x | 1.8 | 11% |
| Leakage Current (Ileak) | 4.31 µA | 5.03 µA | 6.95 µA | 0.72x | 4.6 | 10% |
| Propagation Delay (tpd) | 10.51 ns | 10.88 ns | 9.82 ns | 1.11x | 2.5 | 73% |

**Parameter contribution:** Standby Current (Iddq) 31%, Leakage Current (Ileak) 36%, Propagation Delay (tpd) 33%

**Top attribution features:** leakage drift z-score (+4.582); delay drift z-score (+2.470); Iddq z-score @0h (+1.842)

**Evidence:** Leakage Current (Ileak) reads 5.03 µA at 24h against a lot median of 6.95 µA (0.72x lot median) and uses 10% of the 50 µA datasheet limit. Drift is +16.5% versus a lot-median drift of +4.6%.

### Certificate 221 - SN04-0241 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.508

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 29.83 µA | 34.69 µA | 17.67 µA | 1.96x | 4.6 | 35% |
| Leakage Current (Ileak) | 6.04 µA | 6.47 µA | 6.43 µA | 1.01x | 0.2 | 13% |
| Propagation Delay (tpd) | 9.25 ns | 9.42 ns | 10.33 ns | 0.91x | 1.5 | 63% |

**Parameter contribution:** Standby Current (Iddq) 73%, Leakage Current (Ileak) 2%, Propagation Delay (tpd) 25%

**Top attribution features:** Iddq drift z-score (+4.575); Iddq z-score @24h (+2.753); Iddq z-score @0h (+2.214)

**Evidence:** Standby Current (Iddq) reads 34.69 µA at 24h against a lot median of 17.67 µA (1.96x lot median) and uses 35% of the 100 µA datasheet limit. Drift is +16.3% versus a lot-median drift of +4.5%.

### Certificate 222 - SN04-0061 (LOT-D)

**Verdict:** REJECT | **Risk:** ELEVATED | **Root cause:** `SINGLE_PARAMETER_PEER_OUTLIER` | **Confidence:** 0.501

| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |
|---|---|---|---|---|---|---|
| Standby Current (Iddq) | 31.43 µA | 34.03 µA | 17.67 µA | 1.93x | 2.6 | 34% |
| Leakage Current (Ileak) | 17.28 µA | 19.16 µA | 6.43 µA | 2.98x | 4.5 | 38% |
| Propagation Delay (tpd) | 9.89 ns | 10.16 ns | 10.33 ns | 0.98x | 1.7 | 68% |

**Parameter contribution:** Standby Current (Iddq) 35%, Leakage Current (Ileak) 53%, Propagation Delay (tpd) 12%

**Top attribution features:** leakage z-score @24h (+4.509); leakage z-score @0h (+4.401); Iddq z-score @24h (+2.647)

**Evidence:** Leakage Current (Ileak) reads 19.16 µA at 24h against a lot median of 6.43 µA (2.98x lot median) and uses 38% of the 50 µA datasheet limit. Drift is +10.8% versus a lot-median drift of +6.5%.

