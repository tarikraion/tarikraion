# Raion: GPU Market Intelligence for ICP Definition (buyers needing capacity Feb-Apr 2027)

Prepared 2026-10-02. Analyst: competitive-intelligence / fact-check pass.

## Read this first: method and confidence

- **How it was gathered.** Every figure comes from web-search result extracts (around 60 queries). Direct page fetches were blocked by the sandbox's egress proxy, including dev.to, SemiAnalysis, Wikipedia, sec.gov, DCD, TechCrunch and nebius.com. The session's web-search budget then ran out (200 calls shared across the session). So **no figure below has been checked against its original page**. Spot-check any number before it goes into external sales material.
- **Source tiers.** Each source is tagged:
  - **[A]** primary: company filings, press releases, OEM specs.
  - **[B]** reputable analyst or media: SemiAnalysis, DCD, TechCrunch, Forbes, Bloomberg via secondary.
  - **[C]** aggregator or vendor blog: Spheron, gpusmith, getdeploying, computeprices and similar. These are often SEO content that sells compute. Use them only as directional signals.
- **Labels.** "**Estimate**" marks Raion-side arithmetic or analyst judgment. "**UNVERIFIED / GAP**" marks a claim I could not source this session.
- **Under-sourced areas.** Section 5 (VC totals) and parts of Section 4 (evroc, Genesis Cloud, Sesterce, Northern Data/Taiga) are thin because the search budget ran out. See the gap list at the end.

---

## 1. GPU market state, Sep/Oct 2026

### 1a. Pricing per GPU-hour (USD)

| GPU | On-demand: market reference points | Reserved / contract reference points | Sources |
|---|---|---|---|
| **H100** | Average **$3.84** across 27 providers (13 Sep 2026); cheapest $1.79 (Cudo); cheapest hyperscaler $5.38 (GCP). Median on-demand **$3.42** across 40 providers, week of 28 Sep 2026, **+15% YoY**. Nebius on-demand rises to **$4.50** from 1 Oct 2026. Voltage Park (now Lightning AI) still lists $1.99 on-demand. | SemiAnalysis H100 **1-yr contract index rose ~40%, from $1.70 (Oct 2025) to $2.35 (Mar 2026)**. Ornn OCPI (volume-weighted *transacted* price) settled at **$2.71 on 30 Sep 2026**, down from $3.17 on 7 Sep. SF Compute dedicated H100 was about $1.49-1.68 in Feb-Mar 2026. | [dev.to/fastgpu, C](https://dev.to/fastgpu/what-it-costs-to-rent-an-h100-b200-or-rtx-4090-in-september-2026-live-prices-from-28-gpu-clouds-12n3); [datastorage.com Sep-2026 report, C](https://datastorage.com/articles/the-state-of-gpu-cloud-september-2026-report); [Seeking Alpha on SemiAnalysis, B](https://seekingalpha.com/news/4572260-nvidias-h100-gpu-rental-prices-surge-nearly-40-in-6-months-semianalysis); [SemiAnalysis index, B](https://gpu-index.semianalysis.com/); [Ornn OCPI, B](https://data.ornn.com/preview); [Nebius hike, Motley Fool, B](https://www.fool.com/investing/2026/09/27/nebius-is-raising-the-price-of-its-ai-compute-on-oct-1-here-s-what-that-says-about-the-shortage/); [Spheron on Voltage Park, C](https://www.spheron.network/blog/voltage-park-is-now-lightning-ai-gpu-pricing-2026/); [SF Compute summary, C](https://dailydropout.substack.com/p/sf-compute-the-stock-market-for-gpus) |
| **H200** | Specialist neoclouds publish $4.29-6.31. Ornn OCPI-H200 shown at **$5.58 (30 Sep 2026)**; this looks high next to the H100 index, so verify it. Nebius rises to **$5.40** from 1 Oct. JarvisLabs $3.99 (Aug 2026). | 1-yr reserved from **$2.51** (Seeweb) to **$5.82** (Azure). | [Ornn H200, B](https://data.ornn.com/markets/h200); [JarvisLabs, C](https://jarvislabs.ai/blog/h200-price); [Nebius via KuCoin, C](https://www.kucoin.com/news/flash/nebius-to-hike-gpu-rental-prices-by-up-to-21-from-october-1) |
| **B200** | Average **$6.39** across 12 providers (Sep 2026); cheapest $3.69 (DeepInfra); GCP $11.28. "B200 benchmark **+27.6% YTD**." Nebius rises to **$8.50** from 1 Oct. Lambda HGX B200 from about $6.69 (unverified). | Not well published. Quote-based at most neoclouds. | [dev.to/fastgpu, C](https://dev.to/fastgpu/what-it-costs-to-rent-an-h100-b200-or-rtx-4090-in-september-2026-live-prices-from-28-gpu-clouds-12n3); [datastorage.com, C](https://datastorage.com/articles/the-state-of-gpu-cloud-september-2026-report); [effectstory, C](https://effectstory.com/en/articles/cloud-gpu-h100-b200-pricing-comparison-2026) |
| **B300 (HGX)** | On-demand median **$7.87** (14 Sep 2026). Nebius goes from **$7.85 to $9.50 (+21%)** on 1 Oct 2026. | **Reserved median $5.71** (14 Sep 2026). 12-mo: $6.05 (TheAI Cloud), $7.94 (DigitalOcean). 24-mo: $5.30. 48-mo: as low as **$3.13**. | [savrn B300 index, C](https://savrn.com/ai-index/pricing/gpus/b300); [getdeploying B300, C](https://getdeploying.com/gpus/nvidia-b300); [X/@StockSavvyShay on Nebius, C](https://x.com/StockSavvyShay/status/2100326882621493697) |
| **GB200 (NVL72)** | CoreWeave on-demand **$42/hr per 4-GPU instance = $10.50/GPU-hr**. Market range **$10.50-27/GPU-hr**, which is **$756-1,944/hr per full 72-GPU rack**. | Quote-based. | [Spheron CoreWeave pricing, C](https://www.spheron.network/blog/coreweave-gpu-pricing-2026/); [Spheron GB200 guide, C](https://www.spheron.network/blog/nvidia-gb200-nvl72-guide/); [IntuitionLabs, C](https://intuitionlabs.ai/articles/data-center-gpu-pricing-2026) |
| **GB300 (NVL72)** | Very wide: **$3.02** (Verda, cheapest listing) to **$18.00** (Oracle on-demand). Hyperscalers typically $7.20-7.95. | Runcrate reserved **$2.97**. "Early cloud rental $3.02-30/GPU-hr depending on commitment." | [getdeploying GB300, C](https://getdeploying.com/gpus/nvidia-gb300); [computeprices GB300, C](https://computeprices.com/gpus/gb300); [io.net, C](https://io.net/p/gb300-nvl72-cloud-rental-how-to-access-nvidias-blackwell-ultra-architecture-in-2026) |

**Market direction (Q3 2026).**
- Cloud GPU rental prices were **up 13% over 12 months** to 28 Sep 2026. Of 22 GPU models tracked, 16 rose. The median model was up another 2.8% in the last 4 weeks. [datastorage.com, C](https://datastorage.com/articles/the-state-of-gpu-cloud-september-2026-report)
- Getdeploying's index shows a smaller increase (+6% in 12 months; H100 +14% in 12 months). The methodologies differ. [getdeploying GPU price index, C](https://getdeploying.com/gpu-price-index)
- **Nebius is raising on-demand H100/H200/B200/B300 prices by about 17-21% from 1 Oct 2026**, its second increase in a few months. Media read this as evidence of a deepening supply crunch. [Motley Fool, B](https://www.fool.com/investing/2026/09/27/nebius-is-raising-the-price-of-its-ai-compute-on-oct-1-here-s-what-that-says-about-the-shortage/); [Simply Wall St, C](https://simplywall.st/stocks/us/software/nasdaq-nbis/nebius-group/news/price-hikes-could-be-a-big-test-for-nebius-stock-nbis)
- **Compute is becoming a traded commodity.** ICE and Ornn are launching GPU compute futures ([ICE press release, A](https://ir.theice.com/press/news-details/2026/ICE-and-Ornn-to-Launch-GPU-Compute-Futures-Contracts/default.aspx); [ICE exchange notice 29 Sep 2026, A](https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_Exchange_Notice_ORNN_Compute_4Q2026_20260929.pdf)). CME plans GPU rental futures from **5 Oct 2026**, pending regulatory review ([datastorage.com, C](https://datastorage.com/articles/the-state-of-gpu-cloud-september-2026-report)). CFO-level buyers can now benchmark Raion quotes against a public index.

**Revenue per MW: the cleanest sizing benchmark, from a primary source.**
- Nebius said its large Q2-2026 deals (each over $1B on average, **1-3 year terms**) carry **revenue yields of $20-25M per MW per year**.
- It is negotiating **short-term deals at $40-50M per MW**, "sometimes higher".
- [Yahoo Finance on Nebius Q2, B](https://finance.yahoo.com/technology/ai/articles/nebius-q2-revenue-jumps-454-140044127.html); [Nebius Q2 2026 shareholder letter, A](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf?cache-buster=2026-08-12T11%3A54%3A46.695Z)

### 1b. Availability and lead times

- **Rental capacity is booked well ahead.** SemiAnalysis's "Great GPU Shortage" (spring 2026) reported that **all capacity coming online until Aug-Sep 2026 was already booked**. Blackwell lead times were stretching into Jun-Jul, and half the providers contacted were **completely sold out even for 8 nodes (64 GPUs) of H100/H200**, with no Hopper capacity coming off contract. [SemiAnalysis, B](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity); [Yahoo Finance on SemiAnalysis, B](https://finance.yahoo.com/technology/ai/articles/nvidia-gpu-demand-extreme-even-164322203.html)
- **Hardware lead times are 36-52 weeks for dedicated clusters**, and reserved cloud capacity is booked **6+ months ahead**. **OEMs ask for non-refundable deposits 9-12 months before ship** for HGX/NVL systems. These figures come from search-result extracts of aggregator pages. [gpusmith lead-times PDF, C](https://gpusmith.com/articles/en/pdfs/nvidia-gpu-lead-times-h100-h200-gb200.pdf); [vexxhost, C](https://vexxhost.com/blog/gpu-capacity-crisis-ai-infrastructure-2026/); [gpuaas, C](https://gpuaas.com/blog/gpu-capacity-window-2026)
- **Mid-sized corporates buying directly from OEMs see 12-18 month delivery.** [Digital Chiefs, C](https://www.digital-chiefs.de/en/between-nvidia-dominance-and-alternatives-how-cios-are/)
- **Minimum terms.** Providers generally will not sign **under 6 months** for premium GPUs. The sweet spot is **1-2 years**. [Compute Exchange, C](https://compute.exchange/blogs/reserved-gpus-contract-length)
- **Upstream constraints.** HBM is reported sold out for 2026, and **TSMC CoWoS is fully allocated through at least mid-2027**. Hyperscaler forward orders placed in 2025 consumed most Blackwell allocation through end-2026 and into 2027. [barrack.ai, C](https://blog.barrack.ai/2026-gpu-memory-crisis/); [Electropages/Fusion Worldwide, C](https://www.electropages.com/blog/2026/03/fusion-worldwide-gpu-shortage-and-price-increases-2026)
- **Estimate: what this means for Feb-Apr 2027.** A buyer who needs dedicated capacity in Feb-Apr 2027 is already inside the normal booking window (6-12 months). Raion's Nov-2026 live capacity is a genuine **time-to-compute advantage**: a 3-5 month lead time against a 6-12+ month market norm.

### 1c. Typical contract terms

- **Term.** 1 year is standard and widely available. 2-3 years are available, usually with **~20% of total contract value (TCV) prepaid**. [Compute Exchange, C](https://compute.exchange/blogs/reserved-gpus-contract-length); [Spheron negotiation guide, C](https://www.spheron.network/blog/gpu-cluster-reservation-contract-negotiation-2026/)
- **Prepayment examples.** A search extract cited a 2026 neocloud contract with **~$2.95M upfront = 15% of TCV on a 24-month term**. The specific SEC 8-K could not be confirmed; candidates include [Axe Compute 8-K](https://www.sec.gov/Archives/edgar/data/0001446159/000117184326002636/exh_991.htm). **UNVERIFIED.**
- **Why prepayment matters.** Neoclouds use customer prepayments to help finance their own hardware. [Spheron, C](https://www.spheron.network/blog/gpu-cluster-reservation-contract-negotiation-2026/); [Solvimon, C](https://www.solvimon.com/blog/neoclouds-owe-customers-years-of-compute)
- **Discount curves.** Sources disagree:
  - Compute Exchange: 6-month ~20-30% below on-demand, 1-year ~40-50%, 3-year ~55-72%.
  - Getdeploying: 1-year ~28%, 3-year ~49%.
  - Azure: 37% (1-yr) and 60-62% (3-yr).
  - [Compute Exchange, C](https://compute.exchange/blogs/reserved-gpus-contract-length); [getdeploying, C](https://getdeploying.com/gpu-price-trends)
- **Large-deal benchmark.** Nebius's 2026 deals run 1-3 year terms ([Nebius Q2 letter, A](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf?cache-buster=2026-08-12T11%3A54%3A46.695Z)). CoreWeave's backlog is multi-year ($104B at Q2 end, plus more than $25B added early in Q3) ([CoreWeave Q2-26 8-K, A](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000362/coreweave2q26earningspress.htm); [Yahoo, B](https://finance.yahoo.com/markets/stocks/articles/coreweave-inc-crwv-q2-2026-050033531.html)).
- **New financing models compete with prepayment.** In July 2026 Nvidia began offering compute access in exchange for a **revenue share** instead of full upfront payment. Firmus and Sharon AI are the early partners. [CNBC, B](https://www.cnbc.com/amp/2026/07/02/nvidia-plans-to-offer-start-up-customers-access-to-revenue-sharing-deals.html); [TNW, B](https://thenextweb.com/news/nvidia-offers-ai-startups-compute-now-payment-later)

### 1d. Where the shortages are

- **Blackwell Ultra is the volume product now.** NVIDIA Q2 FY27 (quarter ended 26 Jul 2026): revenue $96.2B, **Data Center $89.0B (+117% YoY)**, "driven by the ramp of Blackwell Ultra". [NVIDIA Q2 FY27 8-K, A](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)
- **Hopper is scarce on the secondary market.** H100/H200 are sold out at many providers and not coming off contract ([SemiAnalysis, B](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)). The H100 one-year contract price rose about 40% between Oct 2025 and Mar 2026 (same source).
- **Power.** Power availability is the binding constraint in established hubs (London, Frankfurt). In some major US markets new grid capacity takes **3-4 years**. [CBRE Global DC Trends 2026, B](https://www.cbre.com/insights/reports/global-data-center-trends-2026); [Enki.AI, C](https://enkiai.com/data-center/data-center-power-crisis-2026-the-grid-bottleneck/); [Schneider Electric blog, Jul 2026, A](https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/)
- **Liquid cooling and density.** Average rack density was reported at ~16 kW (2025) and ~27 kW (2026). **Only about 1 in 5 operators say they can support 50-70 kW racks**, while GB300 NVL72 needs about 130-140 kW. Those figures come from a search extract and the exact originating report was not confirmed. [EIN Presswire Europe DC trends, C](https://world.einnews.com/pr_news/908714298/europe-data-center-market-trends-in-2026-liquid-cooling-power-constraints-and-new-site-selection-priorities); [Lombard Odier, B](https://www.lombardodier.com/insights/2026/january/ai-supercharges-the-race.html)

### 1e. Vera Rubin timing

- **Production and partners.** Full production was announced at GTC Taipei on **1 Jun 2026**. Production shipments go to **8 cloud partners "this fall"**: AWS, Google Cloud, Azure, OCI, CoreWeave, Lambda, Nebius, Nscale. [TechTimes, B](https://www.techtimes.com/articles/319203/20260627/nvidia-vera-rubin-ships-this-fall-8-cloud-partners-10x-lower-token-cost-hbm4-triples-bandwidth.htm); [GCN, B](https://gcn.com/nvidia-vera-rubin-chips-begin-shipping/20421/)
- **First production deployment.** CoreWeave announced the **first production Vera Rubin NVL72** on **30 Sep 2026**, with Cognition as the first customer. The cluster was stood up in early September and Cognition reports **4.8x over GB200**. Microsoft had brought up a validation system in March 2026. [CoreWeave press release, A](https://www.coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition); [DCD, B](https://www.datacenterdynamics.com/en/news/coreweave-claims-to-have-first-nvidia-vera-rubin-nvl72-up-and-running/); [StorageReview, B](https://www.storagereview.com/news/coreweave-vera-rubin-nvl72-production-cognition-4-8x-vera-cpu-forge)
- **Availability for non-hyperscalers.** Meaningful availability for non-hyperscaler customers likely **extends into 2027** (commentary, not a primary source). [barrack.ai, C](https://blog.barrack.ai/nvidia-rubin-vs-blackwell-rent-now-or-wait/)
- **Rack price.** VR200 NVL72 is quoted at about **$5-7M per rack**. Morgan Stanley estimates about **$7.8M** for hyperscalers. The often-quoted "$8.8M" applies to later Rubin Ultra systems. [Tom's Hardware, B](https://www.tomshardware.com/tech-industry/artificial-intelligence/price-of-nvidias-vera-rubin-nvl72-racks-skyrockets-to-as-much-as-usd8-8-million-apiece-but-server-makers-margins-will-be-tight-nvidia-is-moving-closer-to-shipping-entire-full-scale-systems); [Guru3D, C](https://www.guru3d.com/story/nvidia-vera-rubin-ai-rack-cost-reportedly-hits-million/)
- **Rubin Ultra.** Kyber racks of up to **600 kW** are planned for **2027**. [Tom's Hardware, B](https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-rubin-ultra-with-600-000-watt-kyber-racks-and-infrastructure-coming-in-2027); [The Register, B](https://www.theregister.com/2025/03/19/nvidia_charts_course_for_600kw/)
- **Estimate: implication for Raion.** Feb-Apr 2027 buyers outside the top-8 clouds will realistically get **B300 / GB300**, not Rubin. Expect objections like "why lock in Blackwell when Rubin promises 10x lower token cost?" Answer them with term length and an upgrade path.

---

## 2. Power and density: sizing a 0.5 MW block

### 2a. Reference power figures

| System | GPUs | Power | Per-GPU (all-in at system level) | Source |
|---|---|---|---|---|
| DGX/HGX B200 (8-GPU node) | 8 | **~14.3 kW max** | ~1.79 kW | [NVIDIA DGX B200, A](https://www.nvidia.com/en-us/data-center/dgx-b200/); [NVIDIA DGX B200 user guide, A](https://docs.nvidia.com/dgx/dgxb200-user-guide/introduction-to-dgxb200.html) |
| DGX/HGX B300 (8-GPU node) | 8 | **~14.5 kW max**; B300 GPU up to 1,100-1,400 W TDP (liquid) | ~1.81 kW | [gpusmith DGX B300, C](https://gpusmith.com/hardware/systems/nvidia-dgx-b300); [barrack.ai B300 1,400 W, C](https://blog.barrack.ai/nvidia-b300-1400w-data-center-requirements/) |
| GB200 NVL72 (rack) | 72 | **~120 kW** (NVIDIA reference) to **132 kW** (HPE: 115 kW liquid + 17 kW air) | ~1.67-1.83 kW | [HPE QuickSpecs, A](https://www.hpe.com/us/en/collaterals/collateral.a50009224enw.html); [HPE product page, A](https://buy.hpe.com/us/en/Compute/Rack-Scale-System/Nvidia-NVL-System/Nvidia-NVL-System/NVIDIA-GB200-NVL72-by-HPE/p/1014890104) |
| GB300 NVL72 (rack) | 72 | **~132-142 kW** nominal; up to ~155 kW peak | ~1.85-1.97 kW | [Lenovo GB300 NVL72 press doc, A](https://lenovopress.lenovo.com/lp2357.pdf); [Sunbird DCIM, C](https://www.sunbirddcim.com/blog/how-much-power-does-nvidia-gb300-nvl72-need) |
| Vera Rubin NVL72 (rack) | 72 | **~190-230 kW** (aggregator estimate) | ~2.6-3.2 kW | [Moduledge, C](https://www.moduledge.com/blog/nvidia-vera-rubin) |
| Rubin Ultra (Kyber) | 144 packages / 576 dies | **600 kW** | n/a | [Tom's Hardware, B](https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-rubin-ultra-with-600-000-watt-kyber-racks-and-infrastructure-coming-in-2027) |

### 2b. Converting 0.5 MW into GPUs (estimate, Raion-side arithmetic)

Assumptions:
- **Case 1:** 0.5 MW = 500 kW of IT load.
- **Case 2:** 0.5 MW = total facility power. At a liquid-cooled PUE of about 1.15-1.25 that leaves about **400-435 kW of IT**.
- In both cases, allow about 8-12% of IT power for the network fabric, storage and management.

| Platform | Case 1 (500 kW IT) | Case 2 (~400-435 kW IT) |
|---|---|---|
| HGX B200 | ~30-32 nodes = **~240-256 GPUs** (32 nodes = 458 kW of servers) | ~26-28 nodes = **~208-224 GPUs** |
| HGX B300 | ~30-32 nodes = **~240-256 GPUs** (32 nodes = 464 kW) | ~26-28 nodes = **~208-224 GPUs** |
| GB200 NVL72 | **3 racks = 216 GPUs** comfortably; 4 racks (480-528 kW) only if fabric/storage power sits outside the block | **3 racks = 216 GPUs** |
| GB300 NVL72 | **3 racks = 216 GPUs** (396-426 kW, plus networking) | **2-3 racks = 144-216 GPUs** (3 racks is tight at peak) |
| Vera Rubin NVL72 | **2 racks = 144 GPUs** | **~2 racks = 144 GPUs** (tight) |

**Rule of thumb (estimate):** 0.5 MW is about **200-250 Blackwell-class GPUs**, roughly **3 NVL72 racks or about 30 HGX nodes**.

### 2c. Rough annual contract value (ACV) of a 0.5 MW block (estimate)

ACV = GPUs x 8,760 h x price, assuming 100% of hours are billed under a reserved contract.

| Config | GPU-hrs/yr | @ $3.00 (aggressive long-term) | @ $4.00 | @ $5.71 (B300 reserved median, Sep-26) | @ $7.87 (B300 on-demand median) |
|---|---|---|---|---|---|
| 216 GPUs (3x NVL72) | 1.89M | $5.7M | $7.6M | $10.8M | $14.9M |
| 256 GPUs (32 HGX nodes) | 2.24M | $6.7M | $9.0M | $12.8M | $17.7M |

- **Cross-check against Nebius's disclosed yields** ([A](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf?cache-buster=2026-08-12T11%3A54%3A46.695Z)). $20-25M per MW per year on 1-3 year deals implies **$10-12.5M per 0.5 MW per year**. Short-term deals at $40-50M per MW imply $20-25M.
- **Working number (estimate):** **about $7-13M ACV per 0.5 MW block** on 1-3 year reserved terms, which is **about $20-38M TCV over 3 years**. A ~20% prepayment norm would mean **about $4-8M upfront** on a 3-year deal.

### 2d. Capex of a 0.5 MW block, for SPV / ownership deals (estimate from analyst and reseller prices)

| Item | Unit price | Block cost |
|---|---|---|
| HGX B200 8-GPU server | $400-500k ([Mercatus, C](https://www.mercatus-ai.com/blog/b200-server-price)) | 32 nodes ≈ **$12.8-16M** plus network and storage |
| HGX B300 8-GPU server | $550-750k (reseller listings $497k-795k, Sep 2026) ([qdna, C](https://qdna.fr/en/architecture/materiel/b300-sxm); [tech-insider, C](https://tech-insider.org/nvidia-blackwell-gpu-pricing/)) | 32 nodes ≈ **$17.6-24M** |
| GB200 NVL72 rack | ~$3M (Wolfe) | 3 racks ≈ $9M |
| GB300 NVL72 rack | **$3.7-4.3M** (Loop Capital, Wolfe); some inference configs cited at $6-6.5M ([Yahoo/Wolfe, B](https://ca.finance.yahoo.com/news/wolfe-lifts-nvidia-target-25-145211458.html); [aitooldiscovery, C](https://www.aitooldiscovery.com/ai-infra/nvidia-gb300-explained)) | 3 racks ≈ **$11-13M** (up to ~$19.5M) |
| VR200 NVL72 rack | $5-7.8M (Tom's Hardware / Morgan Stanley, B) | 2 racks ≈ $10-15.6M |
| All-in AI facility incl. GPUs | **$30-40M per MW** ([Archdesk, C](https://archdesk.com/blog/global-ai-data-center-construction-2026); [Goldman Sachs, B](https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out)) | **≈ $15-20M per 0.5 MW** |

Estimated payback at Nebius-style yields: about **1.5-2 years** of ACV.

---

## 3. GPU buyer procurement: startups vs enterprises

### 3a. Who signs

- **AI startups.** Purchases are founder-led. The CEO and CTO decide, and the CFO or the board approves larger multi-year commitments.
  - **This is analyst judgment.** I found no 2026 survey that quantifies signers at startups.
  - Supporting evidence: compute is the largest variable cost line. At sub-$100M companies the AI share of R&D spend rose from 25% to 45% year on year. AI-native gross margins average about 52% (2026), against 75-85% for SaaS, with inference about 20-23% of total AI product cost. [ICONIQ State of AI 2026, B](https://www.iconiq.com/growth/reports/state-of-ai-2026); [SaaStr summary, C](https://www.saastr.com/iconiqs-latest-state-of-ai-report-the-10-most-important-data-points-for-saas-founders)
- **Enterprises.** GPU procurement is "not settled by the procurement team alone". It needs IT infrastructure, facilities and the CFO to agree, and **CFOs treat it as a capital-allocation problem**. [SoftwareSeni, C](https://www.softwareseni.com/gpu-procurement-strategy-in-2025-2026-a-decision-framework-for-the-peak-nvidia-era/)
  - Enterprise tech buying committees are large. One report cites **33 people on average** at large enterprises (17 IT, 16 business). [Britopian ITDM 2025 PDF, C](https://www.britopian.com/wp-content/uploads/2025/03/IT-Decision-Makers-and-B2B-Buyers-2025.pdf)
  - The CIO/CTO approves; the CFO owns capex versus opex and financing.
  - **Estimate:** for C-level-only outreach, also target the Chief AI / Data Officer where one exists.
- **The procurement lens is shifting to TCO.** In VentureBeat's Q1-2026 tracker, the share of IT decision-makers ranking "cost per inference / TCO" as a top priority rose **from 34% to 41% in one quarter**, overtaking performance. [VentureBeat, B](https://venturebeat.com/infrastructure/5-gpu-utilization-the-401-billion-ai-infrastructure-problem-enterprises-cant-keep-ignoring)

### 3b. What triggers a purchase

1. **A new funding round.** Large rounds are often paired with compute commitments. Example: Together AI's **$800M Series C (Jul 2026)** came with **500+ MW of capacity commitments financed separately** ([Sacra, C](https://sacra.com/c/together-ai/); [DCD, B](https://www.datacenterdynamics.com/en/news/together-ai-seeks-1bn-in-funding-report/)). VC firms now bundle compute to win deals, for example a16z's Oxygen cluster, which was overbooked ([Yahoo/TechCrunch, B](https://www.yahoo.com/tech/andreessen-horowitz-helps-founders-meet-140000886.html)).
2. **Credit expiry (the "credit cliff").** Most hyperscaler startup credits expire in **12-24 months**: AWS Activate Founders 1 yr, Microsoft Founders Hub 12 months, Google 1-2 yrs. Hyperscaler GPU rates are **2-3x specialist providers**, and moving GPU workloads to a neocloud saves **30-50%**. Teams are told to set up their post-credit provider **90 days before expiry**. [Lyceum, C](https://lyceum.technology/magazine/hyperscaler-credits-expired-next-steps/); [causo.ai, C](https://hub.causo.ai/guides/startup-cloud-credits-compared-2026); [Spheron credits, C](https://www.spheron.network/blog/free-gpu-cloud-credits-2026/)
3. **Inference growth, the "inference flip".** Inference reaches about 23% of AI product cost at the scaling stage ([ICONIQ, B](https://www.iconiq.com/growth/reports/state-of-ai-2026)). SemiAnalysis ties Blackwell lead-time extension to inference and open-weight model demand ([SemiAnalysis, B](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)).
4. **A planned training run or new model generation.** This needs contiguous, InfiniBand-connected clusters, which are hardest to source at short notice ([SemiAnalysis, B](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)).
5. **Contract renewal and price shocks.** One-year contracts are the norm ([Compute Exchange, C](https://compute.exchange/blogs/reserved-gpus-contract-length)). Contracts signed Feb-Apr 2026 therefore come up for renewal Feb-Apr 2027. On-demand price increases such as Nebius's from 1 Oct 2026 push on-demand users toward reserved capacity.

### 3c. How long evaluations take

- **Evaluation practice.** Buyers run timed PoCs or full-scale pilots before signing ([Cudo checklist, C](https://www.cudocompute.com/blog/gpu-cloud-provider-evaluation-checklist)).
- **Burn-in and acceptance.** Operator burn-in is usually **72 h minimum, 5-7 days for large or liquid-cooled deployments**. Cluster-wide burn-in of **3-4 weeks** is recommended to catch early ("infant mortality") failures. [rdp.in burn-in guide, C](https://rdp.in/gpu-mart/knowledge-base/gpu-cluster-burn-in-validation-infant-mortality/); [Together AI practitioner guide, A](https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models)
- **Third-party ratings act as a shortlist filter.** SemiAnalysis ClusterMAX 3.0 (23 Sep 2026) rated 77 providers, based in part on **200+ user interviews** ([SemiAnalysis, B](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard); [clustermax.ai, B](https://www.clustermax.ai/overview)). Raion is not rated; expect buyers to ask about this.
- **Timelines (ESTIMATE; no survey found):**
  - Funded AI startup: about **3-8 weeks** from first C-level call to signature, including a 1-2 week PoC on existing capacity, then 1-2 weeks of acceptance testing at handover.
  - Enterprise: about **3-9 months**, driven by security review, legal and procurement. Enterprises buying owned hardware through OEMs face **12-18 month** delivery ([Digital Chiefs, C](https://www.digital-chiefs.de/en/between-nvidia-dominance-and-alternatives-how-cios-are/)).
  - Feb-Apr 2027 go-lives therefore need **enterprise conversations started now** (Oct 2026) and **startup conversations Nov 2026 - Jan 2027**.

---

## 4. Competitive landscape for dedicated clusters (US / UK / EU)

### 4a. Ratings snapshot: SemiAnalysis ClusterMAX 3.0 (23 Sep 2026)

| Tier | Providers |
|---|---|
| Platinum | CoreWeave (the only provider to hold Platinum in all 3 editions), Nebius (newly upgraded) |
| Gold | Oracle, Google Cloud |
| Silver | Lambda, Firmus, TensorWave |
| Bronze | **Crusoe (downgraded)**, **Together AI (downgraded, reliability)** |
| Unavailable | **Fluidstack** (SemiAnalysis could not verify) |
| Not covered | Nscale's rating was not found in the search extracts |
| Coverage | Only 19 of 77 rated providers received a medal |

Sources: [Blockspace, B](https://blockspace.media/insight/clustermax-3-gpu-cloud-rankings-coreweave-nebius/); [remio.ai, C](https://www.remio.ai/post/clustermax-3-0-ratings-return-and-cheap-gpu-clouds-face-a-harder-test); [Nebius blog, A](https://nebius.com/blog/posts/nebius-platinum-clustermax-3-0); [CoreWeave blog, A](https://wf.coreweave.com/blog/coreweave-becomes-the-only-provider-to-earn-three-consecutive-platinum-clustermax-tm-ratings). Vultr is rated Silver per the [clustermax.ai Vultr review, B](https://www.clustermax.ai/cloudreview/vultr); confirm whether that is the 3.0 edition.

### 4b. Provider-by-provider

| Provider | 2026 position and capacity | Pricing posture | Weaknesses Raion can exploit |
|---|---|---|---|
| **CoreWeave** (US; UK/EU sites) | Q2-26 revenue $2.6B (+112% YoY). **Backlog $104B**, plus more than $25B added early in Q3. **1.5 GW active** (51 DCs), 4.2 GW contracted, target >1.85 GW active by YE-26. First production **Vera Rubin NVL72** on 30 Sep 2026. [8-K, A](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000362/coreweave2q26earningspress.htm); [Yahoo, B](https://finance.yahoo.com/markets/stocks/articles/coreweave-inc-crwv-q2-2026-050033531.html); [CoreWeave, A](https://www.coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition) | Premium. GB200 at $10.50/GPU-hr on-demand. | Backlog dominated by hyperscaler and lab mega-deals, so mid-size buyers wait in line. US-owned, which matters for sovereignty buyers. Customer rents and never owns. |
| **Nebius** (NL/US; Finland, UK, France, Iceland, Israel) | Q2-26 revenue $582M (+454%), ARR $3B. Contracted-power target raised to **5 GW** for YE-26. UK: **£1.7B** commitment, Kao Data Harlow (22 MW), Vantage Newport. [Yahoo, B](https://finance.yahoo.com/technology/ai/articles/nebius-q2-revenue-jumps-454-140044127.html); [Nebius letter, A](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf?cache-buster=2026-08-12T11%3A54%3A46.695Z); [DCD Kao, B](https://www.datacenterdynamics.com/en/news/nebius-signs-22mw-capacity-agreement-with-kao-data-in-the-uk/); [Fibre Systems, B](https://www.fibre-systems.com/article/nebius-scales-uk-ai-cloud-infrastructure-ps17bn-expansion) | **Raising prices.** On-demand +17-21% from 1 Oct 2026 (H100 $4.50, H200 $5.40, B200 $8.50, B300 $9.50). Large deals at $20-25M/MW, short-term at $40-50M/MW. | Price hikes, so on-demand customers are now price-sensitive. Shared cloud model. Prioritises $1B+ deals. |
| **Nscale** (UK) | S-1 filed 18 Sep 2026 (NYSE: NSCL). H1-26 revenue $140.6M, net loss $1.02B. **Contracted TCV $103.4B, only ~2.5% active.** About 85% of it is concentrated in Microsoft ($43.8B through 2033) and Anthropic ($44.6B). Loughton (Essex): 50→90 MW, 23,040 GB300 **from Q1 2027**. Stargate UK: 8,000 GPUs in 2026, scaling to 31,000. Stargate Norway. [TechCrunch, B](https://techcrunch.com/2026/09/22/nscales-ipo-will-test-wall-streets-appetite-for-concentrated-ai-bets-once-again/); [Yahoo, B](https://finance.yahoo.com/markets/stocks/articles/nscale-files-ipo-pipeline-passes-203402491.html); [S-1, A](https://www.sec.gov/Archives/edgar/data/0002110365/000119312526395475/ck0002110365-20260918.htm); [RCR, B](https://www.rcrwireless.com/20250919/ai-infrastructure/nscale-uk-ai); [DCD Stargate UK, B](https://www.datacenterdynamics.com/en/news/openai-announces-stargate-uk-with-up-to-8000-gpus-at-nscale-data-centers/) | Hyperscale offtake model. | Capacity is committed to 2 anchor tenants, so the UK mid-market is under-served. Execution risk: 97.5% of TCV is not yet live. Loughton GB300 arrives Q1 2027, the same window as Raion, but it is likely spoken for. |
| **Fluidstack** (moved HQ from London to New York, Dec 2025) | Raised **$1.5B at $18B** (Sep 2026). Building TX/NY for Anthropic's $50B plan. **Pulled out of the €10B French project** (Mar 2026) to focus on the US. Projected revenue ~$660M while "owning zero chips". [Forbes, B](https://www.forbes.com/sites/iainmartin/2026/09/03/a-tiny-startup-helping-google-take-on-nvidia-is-now-worth-18-billion/); [AI Magazine, B](https://aimagazine.com/news/fluidstack-leading-anthropics-us-50bn-compute-build-out); [TechTimes, B](https://www.techtimes.com/articles/326746/20260905/fluidstack-closes-15b-revenue-soars-18m-660m-projected-while-owning-zero-chips.htm) | Lab-scale contracts. | **Exited Europe's flagship project.** ClusterMAX "Unavailable". Focused on frontier labs, not 0.5-5 MW buyers. |
| **Lambda** (US) | Multi-billion Microsoft deal (GB300 NVL72). Kansas City 24 MW (more than 10k Blackwell Ultra), **initial deployment dedicated to a single customer**. Pre-IPO talks of up to $3B at $12B+ (Aug-Sep 2026). 1-Click Clusters of 16-512 B200 GPUs on demand. [DCD, B](https://www.datacenterdynamics.com/en/news/microsoft-signs-multi-billion-dollar-cloud-capacity-deal-with-lambda/); [DCD KC, B](https://www.datacenterdynamics.com/en/news/ai-cloud-firm-lambda-targets-data-center-deployment-in-kansas-city-missouri/); [Sacra, C](https://sacra.com/c/lambda-labs/) | Developer-friendly self-serve; B200 from about $6.69 (unverified). | US-only footprint, so no EU/UK sovereignty. Capacity increasingly pre-sold to Microsoft. ClusterMAX Silver. |
| **Crusoe** (US; Norway, Iceland) | Raised $3.9B+ Series F (2026); pre-IPO talks of about $3B at about $30B valuation. Abilene 700+ MW live by Dec 2026. Norway 12→52 MW (Polar). Iceland (atNorth ICE02). [Sacra PDF, C](https://sacra-pdfs.s3.us-east-2.amazonaws.com/crusoe.pdf); [Crusoe newsroom, A](https://www.crusoe.ai/resources/newsroom/crusoe-expands-iceland-data-center-capacity) | Energy-first; large AI factories. | **Downgraded to Bronze.** Mega-campus focus (OpenAI/Oracle/Microsoft). Small European footprint. |
| **Together AI** (US; EU via Hypertec/5C) | **$800M Series C at $8.3B (Jul 2026)** plus 500+ MW commitments. EU plan with **Hypertec + 5C**: up to 2 GW and about 100k GPUs (FR, UK, IT, PT) through 2028. Also buys capacity from Rumble. [Sacra, C](https://sacra.com/c/together-ai/); [DCD Hypertec/5C, B](https://www.datacenterdynamics.com/en/news/hypertec-and-5c-target-europe-plan-2gw-roll-out-for-together-ai/); [Together blog, A](https://www.together.ai/blog/together-ai-expands-in-europe); [DCD Rumble, B](https://www.datacenterdynamics.com/en/news/together-ai-taps-rumble-for-nvidia-blackwell-gpu-capacity/) | Inference API plus GPU clusters (16 to 100k+ GPUs). | **Downgraded to Bronze (reliability).** Clusters run on third-party DCs. It competes with its own cluster customers' inference products. |
| **Vultr** (US; 33 regions incl. Milan) | $333M at $3.5B (LuminArx, AMD Ventures). GB300 NVL72 with HPE (Jun 2026). Pre-orders for AMD MI455X/Helios **for 2027-28**. [BusinessWire, A](https://www.businesswire.com/news/home/20260723323194/en/Vultr-Scales-Next-Generation-AI-Infrastructure-with-AMD-Helios-Rackscale-Solution-Powered-by-AMD-Instinct-MI455X-GPUs); [StorageNewsletter, B](https://www.storagenewsletter.com/2026/06/22/hpe-discover-2026-vultr-selects-hpe-and-nvidia-for-next-generation-ai-infrastructure-for-cloud-scale-data-centers/) | "Alternative hyperscaler"; reserved pre-orders. | General-purpose cloud. AMD-heavy roadmap. Shared multi-tenant. |
| **Voltage Park → Lightning AI** (US) | Merged into Lightning AI on 21 Jan 2026. Fleet of 35-36k H100/B200/GB300. H100 on-demand $1.99. Reserve contracts 6+ months, 32 to 8,000+ GPUs, quote-based. [Spheron, C](https://www.spheron.network/blog/voltage-park-is-now-lightning-ai-gpu-pricing-2026/) | Low-price Hopper. | US-only. Mostly Hopper. Platform-led (Lightning) rather than infrastructure-led. |
| **Firmus / Sustainable Metal Cloud** (AU; SG) | ASX IPO of up to about A$7B targeted for end-Oct 2026, with OpenAI as anchor. Project Southgate up to 1.6 GW in Australia by 2028. Early partner in Nvidia's revenue-share programme. [Marcus Today, C](https://marcustoday.com.au/2026/09/is-the-firmus-ipo-worth-the-hype/); [techi, C](https://www.techi.com/firmus-ipo-asx-7-billion-openai-anchor-nvidia/); [Firmus, A](https://firmus.co/newsroom/southgate-expansion) | Silver ClusterMAX. | **Australia-centric.** Little US/UK/EU dedicated supply. |
| **Verda (ex-DataCrunch)** (Finland/Iceland) | Lists the cheapest GB300 at **$3.02/GPU-hr**. [getdeploying, C](https://getdeploying.com/gpus/nvidia-gb300) | Price leader. | **GAP:** 2026 capacity and funding not verified this session. |
| **Hypertec** (Canada; EU via 5C) | Partner to Together AI for up to 2 GW in Europe. [DCD, B](https://www.datacenterdynamics.com/en/news/hypertec-and-5c-target-europe-plan-2gw-roll-out-for-together-ai/) | Infrastructure and OEM partner. | **GAP:** direct-to-customer offer not verified. |
| **Northern Data / Taiga Cloud** (DE) | **UNVERIFIED (background):** reported acquisition by Rumble in 2025-26. The Together AI-Rumble Blackwell capacity deal ([DCD, B](https://www.datacenterdynamics.com/en/news/together-ai-taps-rumble-for-nvidia-blackwell-gpu-capacity/)) suggests this capacity now goes wholesale through Rumble. | n/a | Ownership change and uncertainty. Verify. |
| **evroc** (SE), **Genesis Cloud** (DE), **Sesterce** (FR) | **GAP:** no 2026 data gathered (search budget exhausted). | n/a | Likely angle: sovereignty peers. Check scale, Blackwell availability and minimum terms. |
| **Other dedicated-compute alternatives** | **SF Compute**: marketplace for short-term clusters, raised a $40M Series A, manages more than $100M of hardware ([DCD, B](https://www.datacenterdynamics.com/en/news/sf-compute-raises-40m-for-ai-compute-marketplace-offering/)). **Andromeda**: $60M at $1.5B, helps hot AI companies find GPUs ([Upstarts, B](https://www.upstartsmedia.com/p/andromeda-ai-compute-startup-raises-60m)). **a16z Oxygen**: VC-provided GPUs for equity ([Yahoo, B](https://www.yahoo.com/tech/andreessen-horowitz-helps-founders-meet-140000886.html)). **Nvidia revenue-share compute** ([CNBC, B](https://www.cnbc.com/amp/2026/07/02/nvidia-plans-to-offer-start-up-customers-access-to-revenue-sharing-deals.html)). | Flexible, short-term or financing-led. | These compete on *financing and flexibility*, not ownership. |

### 4c. Cross-cutting weaknesses Raion can exploit

- **Mid-market neglect.** The leading neoclouds' backlogs are dominated by a handful of hyperscaler and lab contracts:
  - Nscale: about 85% from Microsoft and Anthropic.
  - Fluidstack: Anthropic and Google.
  - Lambda: Microsoft.
  - CoreWeave: $104B backlog.
  - Sources: [TechCrunch, B](https://techcrunch.com/2026/09/22/nscales-ipo-will-test-wall-streets-appetite-for-concentrated-ai-bets-once-again/); [Forbes, B](https://www.forbes.com/sites/iainmartin/2026/09/03/a-tiny-startup-helping-google-take-on-nvidia-is-now-worth-18-billion/); [DCD, B](https://www.datacenterdynamics.com/en/news/microsoft-signs-multi-billion-dollar-cloud-capacity-deal-with-lambda/)
  - Buyers of 0.5-5 MW are deprioritised, as startups were in the H100 crunch ([Yahoo on a16z Oxygen, B](https://www.yahoo.com/tech/andreessen-horowitz-helps-founders-meet-140000886.html)).
- **Rent versus own.** Every competitor above rents. Raion's client-controlled SPV gives **asset ownership or control**, a residual value claim and balance-sheet options. This positioning is unique in the set but **unverified as a buyer preference**, so test it in discovery.
- **Sovereignty.** Fluidstack moved to New York and exited France. CoreWeave, Lambda and Crusoe are US-owned. UK/Gibraltar-law SPVs with client control may appeal to EU/UK regulated buyers. Sovereignty-driven public programmes are listed in Section 5.
- **Speed-to-power.** Market lead times are 36-52 weeks for hardware and 6+ months for reserved capacity, and Nscale's Loughton GB300 arrives Q1 2027. Raion's capacity live from Nov 2026, in 0.5 MW increments, is a direct counter.
- **Reliability churn.** Together AI and Crusoe were downgraded to Bronze and Fluidstack is "Unavailable" in ClusterMAX 3.0. Their customers are open to approaches, so build reliability proof: burn-in reports and SLAs.
- **Pricing pressure.** Nebius's 17-21% on-demand increase and a market up 13% YoY make **fixed-price multi-year** capacity attractive. Ornn/ICE/CME indices let buyers benchmark, so price transparently against them.

---

## 5. Demand data points

### 5a. AI VC funding totals (H1 2026, Q3 2026)

**GAP, not verified this session.** The web-search budget ran out before this section. Do not quote numbers until sourced. Recommended sources:
- **Crunchbase News** quarterly global and AI funding reports (Q3-2026 report usually lands in the first week of October): https://news.crunchbase.com/
- **PitchBook-NVCA Venture Monitor** (Q3-2026 edition, mid-October): https://pitchbook.com/news/reports
- **Dealroom** AI and Europe reports: https://dealroom.co/
- **Atomico State of European Tech 2026** (usually Nov/Dec): https://www.stateofeuropeantech.com/
- **Sifted** for European AI round coverage: https://sifted.eu/

**Verified compute-adjacent capital flows (2026)** that show where money is going:
- Fluidstack: $1.5B at $18B ([Forbes, B](https://www.forbes.com/sites/iainmartin/2026/09/03/a-tiny-startup-helping-google-take-on-nvidia-is-now-worth-18-billion/)).
- Together AI: $800M at $8.3B ([Sacra, C](https://sacra.com/c/together-ai/)).
- Crusoe: $3.9B+ Series F ([Sacra, C](https://sacra-pdfs.s3.us-east-2.amazonaws.com/crusoe.pdf)).
- Lambda: up to $3B pre-IPO talks ([Sacra, C](https://sacra.com/c/lambda-labs/)).
- Andromeda: $60M ([Upstarts, B](https://www.upstartsmedia.com/p/andromeda-ai-compute-startup-raises-60m)).
- Ornn: $33M led by a16z ([AI Weekly, C](https://aiweekly.co/alerts/ornn-raises-33m-led-by-a16z-to-build-gpu-compute-futures-market)).
- Silicon Data: $30M Series A ([TechCrunch via search, B](https://techcrunch.com/video/meet-the-startup-helping-wall-street-put-a-price-on-ai-compute/)).

**Infrastructure demand proxies:**
- NVIDIA Data Center revenue of **$89.0B in one quarter** (+117% YoY) ([A](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)).
- CoreWeave backlog of **$104B** ([A](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000362/coreweave2q26earningspress.htm)).
- Nscale contracted TCV of **$103.4B** ([B](https://finance.yahoo.com/markets/stocks/articles/nscale-files-ipo-pipeline-passes-203402491.html)).
- Nebius targeting **5 GW** contracted ([B](https://finance.yahoo.com/technology/ai/articles/nebius-q2-revenue-jumps-454-140044127.html)).

### 5b. Share of startup budgets going to compute

All figures are from vendor or blog sources. Treat them as directional.

- **GPU compute is 40-60% of technical budgets** in an AI startup's first 2 years ([GPUnex, C](https://www.gpunex.com/blog/ai-startup-compute-costs/)).
- **15-25% of burn goes to compute pre-revenue**, against 5-10% of revenue on cloud at SaaS companies (search extract; originating source unclear) ([GMI Cloud, C](https://www.gmicloud.ai/en/blog/how-much-do-gpu-cloud-platforms-cost-for-ai-startups-in-2026)).
- **Top European AI startups allocate 17-80% of funding to compute** (search extract; originating study not confirmed) ([mean.ceo, C](https://blog.mean.ceo/ai-infrastructure-startup-funding-statistics/)).
- ICONIQ is the most robust source:
  - Inference is 20-23% of AI product cost.
  - High-growth companies spend about 57% of R&D on AI.
  - AI-native gross margins are about 52%.
  - [ICONIQ State of AI 2026, B](https://www.iconiq.com/growth/reports/state-of-ai-2026)

### 5c. Sovereign AI programmes

Items marked "(bg)" are pre-2026 background knowledge that was **not re-verified this session**. Confirm the figure and URL before external use.

| Programme | What is known | Source / status |
|---|---|---|
| **EU InvestAI / AI Gigafactories** | (bg) InvestAI announced Feb 2025: **€200B** mobilisation, including **€20B for about 4-5 AI Gigafactories** (about 100k GPUs each). Gigafactory call / selection timing in 2026 needs verification. | European Commission press corner (verify) |
| **EuroHPC AI Factories** | (bg) About 19 AI Factories selected across 2024-25, giving startups and SMEs access to EuroHPC compute. | EuroHPC JU site (verify) |
| **UK** | **Stargate UK** (OpenAI + Nscale + Nvidia): 8,000 GPUs in 2026, scaling to 31,000, including an AI Growth Zone ([DCD, B](https://www.datacenterdynamics.com/en/news/openai-announces-stargate-uk-with-up-to-8000-gpus-at-nscale-data-centers/)). Private commitments: Nscale £2B ([Nscale PR, A](https://www.nscale.com/press-releases/ai-hyperscaler-nscale-to-invest-gbp-2-billion-in-the-uk-data-centre-industry)), Nebius £1.7B ([Fibre Systems, B](https://www.fibre-systems.com/article/nebius-scales-uk-ai-cloud-infrastructure-ps17bn-expansion)). (bg) AI Opportunities Action Plan (Jan 2025) and the compute commitments in the June 2025 Spending Review (about £2B for the AI Action Plan) need verification. | Mixed |
| **France** | (bg) **€109B** of private AI infrastructure commitments announced at the Feb 2025 AI Action Summit. Fluidstack's €10B French project was **cancelled** in Mar 2026 ([AI Magazine / Bloomberg via search, B](https://aimagazine.com/news/fluidstack-leading-anthropics-us-50bn-compute-build-out)). | Partly verified |
| **Germany** | (bg) Deutsche Telekom + Nvidia "Industrial AI Cloud" in Munich (about 10k GPUs, about €1B, announced late 2025). Germany bidding for EU Gigafactories. | Verify |

---

## 6. Public signals that predict GPU need in 4-6 months, and how to monitor them

Signal strength is analyst judgment, grounded in the evidence cited. No academic study validating these predictors was found.

| # | Signal | Why it predicts need (evidence) | Lead time to need (estimate) | How to monitor |
|---|---|---|---|---|
| 1 | **Funding round of $30M or more closed in the last 0-120 days** (AI-native, model-building or inference-heavy) | Compute is the largest variable cost (40-60% of technical budget, [C](https://www.gpunex.com/blog/ai-startup-compute-costs/)). Large rounds are paired with compute commitments, e.g. Together AI's $800M plus 500 MW ([C](https://sacra.com/c/together-ai/)). | 1-6 months | Crunchbase alerts/API, Dealroom (EU coverage), PitchBook, Harmonic, Sifted / TechCrunch / Axios Pro Rata newsletters |
| 2 | **Hyperscaler credit cliff** (accelerator cohort or credits granted 9-18 months ago) | Credits expire in 12-24 months; hyperscaler GPU rates are 2-3x neoclouds; teams are advised to line up a provider 90 days before expiry ([C](https://lyceum.technology/magazine/hyperscaler-credits-expired-next-steps/)) | 2-6 months | Accelerator cohort lists (YC, Google for Startups AI, AWS Generative AI Accelerator, Microsoft for Startups, NVIDIA Inception), founder interviews in Raion's forum |
| 3 | **Hiring for GPU and ML infrastructure roles** ("ML infra", "HPC", "Slurm", "InfiniBand", "distributed training", "Head of Compute") | Teams staff up before standing up or migrating clusters (analyst judgment) | 2-6 months | LinkedIn Sales Navigator job-change and hiring alerts; Harmonic headcount signals; Explorium firmographic and hiring signals; ATS feeds (Greenhouse, Lever, Ashby); Welcome to the Jungle / Otta for EU |
| 4 | **Own-model activity**: Hugging Face model uploads, arXiv papers, open-weight releases, benchmark entries | Training the next model needs contiguous clusters. Open-weight demand is extending Blackwell lead times ([SemiAnalysis, B](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)). | 3-9 months (next model generation) | Hugging Face Hub API (org model uploads, downloads, trending), arXiv author affiliations, GitHub orgs, Epoch AI notable-models database |
| 5 | **Inference traffic growth** | Inference is about 23% of AI product cost at scaling stage ([ICONIQ, B](https://www.iconiq.com/growth/reports/state-of-ai-2026)) | 1-4 months | Similarweb or app-store rank trends, OpenRouter model/app rankings, API usage leaderboards, revenue announcements |
| 6 | **Contract roll-off**: 1-yr reserved contracts signed Feb-Apr 2026 | 1-yr is the standard term ([C](https://compute.exchange/blogs/reserved-gpus-contract-length)). Those contracts were signed at elevated prices ($2.35 H100 1-yr index in Mar 2026) and renew Feb-Apr 2027. | 3-6 months | Discovery calls; customer case studies and press releases from neoclouds (e.g. "X selects Nebius/Lambda"); Raion forum |
| 7 | **Exposure to price shocks or reliability downgrades** | Nebius on-demand +17-21% from 1 Oct 2026 ([B](https://www.fool.com/investing/2026/09/27/nebius-is-raising-the-price-of-its-ai-compute-on-oct-1-here-s-what-that-says-about-the-shortage/)). Together and Crusoe moved to Bronze, Fluidstack "Unavailable" ([B](https://blockspace.media/insight/clustermax-3-gpu-cloud-rankings-coreweave-nebius/)). | 1-4 months | Provider customer-logo pages and case studies, BuiltWith-type tech-stack tools, community channels (Discord, X) |
| 8 | **Sovereignty or regulatory triggers** (EU/UK regulated sectors, public-sector AI programmes) | Sovereignty programmes in Section 5; US-owned providers dominate supply | 3-12 months | EU/UK tender portals (TED, Find a Tender, Contracts Finder), EuroHPC calls, AI Growth Zone announcements, UK Companies House filings (new SPVs or charges) |
| 9 | **Market-price timing** | Rising indices create urgency to lock in fixed prices | Continuous | SemiAnalysis H100 index ([B](https://gpu-index.semianalysis.com/)), Ornn OCPI ([B](https://data.ornn.com/preview)), ICE/CME GPU futures |

**Tool notes:**
- Crunchbase and Dealroom are the funding backbone; Dealroom is stronger for UK/EU.
- Harmonic is good for early-stage discovery and headcount momentum.
- Explorium is a data API for firmographic and intent enrichment.
- Sifted covers EU round news.
- LinkedIn Sales Navigator is the main C-level targeting layer.
- The Hugging Face Hub API is free and scriptable by organisation.
- Raion's **own 900+ founder forum** is the highest-signal first-party source for credit-cliff and contract-renewal timing.

---

## 7. Implications for Raion's ICP (Feb-Apr 2027 capacity, C-level only)

1. **Sell the timing gap.** The market is 6-12+ months from commitment to capacity: 36-52 week hardware lead times, reserved capacity booked 6+ months ahead, CoWoS allocated through mid-2027. A buyer who needs GPUs in Feb-Apr 2027 and has not signed is already late. Raion's capacity live from Nov 2026 is the headline: "sign in Q4 2026, run in Q1 2027". **Signature deadline for Feb-Apr go-lives:** about Dec 2026 for startups, and **now** for enterprises.
2. **Size the ICP to the block.** 0.5 MW is about **200-250 Blackwell GPUs** (3x GB300 NVL72 or about 30 HGX B300 nodes), which is about **$7-13M ACV** (estimate; Nebius discloses $20-25M/MW). That is about **$20-38M TCV over 3 years** and about **$11-24M of hardware capex**.
   - Target buyers who can commit at least ~$7M a year or finance an SPV of about $15-20M.
   - In practice that means **Series B+ AI-native companies with $50M+ raised** (estimate), well-funded inference businesses, or enterprises and sovereign entities.
   - Seed and Series A companies belong in a pooled, fractional or forum-led offer, not the core ICP.
3. **Lead with B300 / GB300.** Feb-Apr 2027 buyers will not get Vera Rubin at scale outside the 8 launch clouds; CoreWeave's first production deployment was only 30 Sep 2026. Pre-empt the "wait for Rubin" objection with 12-24 month terms or a Rubin refresh option in later 0.5 MW blocks.
4. **Primary segment: under-served mid-market AI-native companies (US/UK/EU) needing 0.5-5 MW.** The large neoclouds' backlogs are dominated by Microsoft, Anthropic, OpenAI and Google mega-deals (Nscale about 85% from 2 customers; CoreWeave $104B backlog). Position Raion as the provider for which these buyers are a priority, not an afterthought.
5. **Secondary segment: European regulated or sovereignty-sensitive buyers** in finance, health, defence and public-sector suppliers.
   - The case: Fluidstack moved to New York and exited France; CoreWeave, Lambda and Crusoe are US-owned.
   - UK/Gibraltar-law SPVs with client control and dedicated (not shared) hardware are a differentiated answer.
   - Validate the willingness to pay for sovereignty in discovery; it is not yet evidenced.
6. **Trigger-based list building.** Combine (a) a funding round of $30M+ in the last 120 days, (b) GPU or ML-infrastructure hiring, (c) Hugging Face or open-weight model releases or fast inference traffic growth, and (d) a credit cliff or 1-yr contract roll-off in Q1 2027. Companies showing 2 or more signals form the active ICP.
7. **Displacement plays.** Target C-levels at customers of providers that just raised prices (Nebius on-demand +17-21% from 1 Oct 2026) or were downgraded in ClusterMAX 3.0 (Together, Crusoe to Bronze; Fluidstack "Unavailable"). Pitch fixed-price, dedicated, liquid-cooled capacity with a published burn-in and acceptance process.
8. **Who to target at the C-level.**
   - **Startups:** CEO and CTO decide; the CFO is the key to SPV financing and prepayment structure.
   - **Enterprises:** CIO/CTO plus CFO. Add the Chief AI / Data Officer where present. The CFO lens is now TCO and capital allocation; "cost per inference / TCO" was a top priority for 41% of IT decision-makers in Q1-26.
9. **Use financing as the wedge against cash drag.** Market norm is about 15-20% of TCV prepaid on 2-3 year deals, which is $4-8M on one block. Competing financing models exist: Nvidia revenue-share compute, a16z Oxygen equity-for-compute, and SF Compute short-term clusters. Raion's SPV structure should be pitched to CFOs as ownership with financing, compared explicitly with rent plus prepayment.
10. **Price against public benchmarks.** H100 1-yr index $2.35 (Mar-26); OCPI H100 $2.71 (30 Sep 26); B300 reserved median $5.71 and on-demand $7.87 (Sep-26). Rental prices are up about 13% YoY, and futures on ICE and CME start in Q4-26. Index-referenced quotes and fixed-price multi-year terms will land with CFOs.
11. **Exclude or deprioritise:**
    - Frontier labs needing GW scale (served by Fluidstack, Nscale, CoreWeave).
    - Enterprises still at the AI exploration stage, whose 12-18 month cycles miss the window.
    - Buyers who need fewer than about 64 GPUs; route them to on-demand partners or forum offers.
12. **Close the credibility gap early.** Raion has no ClusterMAX rating or production track record yet. Buyers shortlist using ratings and PoCs. Offer a PoC on Nov-2026 capacity, burn-in reports (72 h to 3-4 weeks), and SLA credits, and pursue a ClusterMAX evaluation.

---

### Open gaps to close before external use

1. 2026 AI VC totals (US/UK/EU; H1 and Q3) and compute share. Pull from Crunchbase, PitchBook-NVCA and Dealroom.
2. 2026 status of the EU AI Gigafactories selection, UK compute budgets, the France €109B follow-through, and Germany's programmes.
3. 2026 profiles of evroc, Verda, Genesis Cloud, Sesterce and Northern Data/Taiga (including whether Rumble's acquisition closed). Hypertec's direct offer.
4. Original-page verification of the Tier C pricing figures, especially Ornn H200 at $5.58 and the GB300 $3.02-18 spread.
5. The specific SEC 8-K behind the "15% upfront on a 24-month contract" example.
