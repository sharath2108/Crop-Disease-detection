"""
Crop Disease Knowledge Base
Covers all 38 PlantVillage benchmark classes with exact scientific names, 
visual markers, cultural precautions, precision fertilizer formulations, 
chemical treatments, and organic remedies.
"""

DISEASE_PROFILES = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "condition": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Apple scab is a severe fungal disease that attacks foliage and young fruit, resulting in defoliation and scarred unmarketable fruit.",
        "symptoms": [
            "Olive-green to velvety dark brown circular spots on leaf surface",
            "Crinkled, puckered leaves that drop prematurely",
            "Corky, brown scab lesions with cracked margins on developing fruit"
        ],
        "causes": "High humidity, continuous leaf wetness (6+ hours), and cool spring temperatures (12-24°C). Spores overwinter in fallen leaves.",
        "precautions": [
            "Rake, chop, or burn fallen leaf litter in autumn to eliminate overwintering ascospore inoculum.",
            "Prune tree canopy annually in late winter to maximize sunlight penetration and rapid air circulation.",
            "Avoid overhead irrigation; use drip lines to keep foliage completely dry.",
            "Disinfect pruning shears between cuts with 70% isopropyl alcohol."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-15-20 (Balanced with elevated Potassium and Phosphorus).",
            "micronutrients": "Foliar Zinc (Zn), Boron (B), and soluble Silicon (Si) to reinforce cell walls.",
            "application_advice": "Apply Urea (5%) spray to autumn foliage right before leaf drop to accelerate leaf decomposition. Maintain soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid excessive Nitrogen in early spring, which promotes tender, susceptible succulent shoots."
        },
        "chemical_control": {
            "active_agents": "Captan 50% WP (2.5 g/L) or Myclobutanil 10% WP (1 g/L) or Difenoconazole 25% EC (0.5 ml/L).",
            "spray_timing": "Apply protectant spray at green tip stage and repeat every 7-10 days through petal fall during wet weather."
        },
        "organic_control": {
            "remedies": "Liquid Lime Sulfur (pre-bloom), wettable elemental sulfur (3 g/L), or Serenade ASO (Bacillus subtilis strain QST 713).",
            "frequency": "Spray preventive sulfur at tight cluster stage prior to predicted rain events."
        },
        "recovery_plan": {
            "days_1_3": "Prune severely blighted twigs; apply urgent protectant fungicide or wettable sulfur.",
            "days_4_10": "Ensure soil moisture is managed via base drip; apply foliar potassium to toughen cuticles.",
            "days_14_plus": "Inspect new leaf flushes weekly; maintain protective barrier until fruit reaches maturity."
        }
    },

    "Apple___Black_rot": {
        "crop": "Apple",
        "condition": "Black Rot (Frogeye Leaf Spot)",
        "scientific_name": "Botryosphaeria obtusa",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Fungal pathogen producing distinct frogeye leaf spots, cankers on branches, and firm rotting mummified fruit.",
        "symptoms": [
            "Small purple specks expanding into tan centers with dark brown borders ('frogeye' spots)",
            "Sunken, reddish-brown cankers on bark",
            "Mummified black shriveled fruit remaining attached to the tree"
        ],
        "causes": "Overwinters in dead wood, pruned branches, and mummified apples. Thrives in warm, wet weather (20-27°C).",
        "precautions": [
            "Cut out branch cankers at least 6-8 inches below visible infected margins.",
            "Remove and burn all mummified fruits left hanging from prior harvest.",
            "Seal pruning wounds with an approved tree sealant during rainy months.",
            "Control fire blight and insect damage which create entry wounds for the fungus."
        ],
        "fertilizers": {
            "primary_npk": "NPK 8-15-15 with balanced organic compost.",
            "micronutrients": "Calcium Chloride foliar sprays to boost fruit firmness and rind resistance; Magnesium sulfate (Epsom salt).",
            "application_advice": "Soil drench humic acid and potassium silicate. Soil pH target: 6.2 - 6.5.",
            "avoid_fertilizer": "Avoid high ammoniacal nitrogen which promotes soft growth."
        },
        "chemical_control": {
            "active_agents": "Thiophanate-methyl 70% WP (1 g/L) or Captan 80% WDG (2 g/L) or Mancozeb 75% WP (2.5 g/L).",
            "spray_timing": "Apply at petal fall and cover sprays every 10 to 14 days throughout summer."
        },
        "organic_control": {
            "remedies": "Copper octanoate (copper soap) or Bordeaux mixture (copper sulfate + lime); Trichoderma harzianum soil drench.",
            "frequency": "Apply copper sprays as a delayed-dormant wash before bud burst."
        },
        "recovery_plan": {
            "days_1_3": "Physically strip and incinerate all mummified apples and cankered branches.",
            "days_4_10": "Apply systemic fungicide combined with calcium foliar feed.",
            "days_14_plus": "Monitor canker cut sites for re-infection; repeat cover spray post heavy rains."
        }
    },

    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "condition": "Cedar Apple Rust",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Heteroecious rust fungus requiring both apple trees and Eastern red cedar (Juniperus) to complete its complex lifecycle.",
        "symptoms": [
            "Bright yellow-orange spots on the upper leaf surface with a red border",
            "Raised dark dots (spermogonia) inside the orange lesions",
            "Tube-like aecia structures forming on the underside of leaves and fruit"
        ],
        "causes": "Wind-dispersed basidiospores from cedar galls during warm rainy spring periods.",
        "precautions": [
            "Remove Eastern red cedar trees within a 1-2 mile radius of apple orchards if feasible.",
            "Prune gelatinous orange telial horns off neighboring junipers during early spring rains.",
            "Plant rust-resistant apple cultivars (e.g., Liberty, Freedom, Enterprise)."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-12-17 with high Potassium sulphate.",
            "micronutrients": "Zinc chelate (Zn-EDTA) and seaweed extract to mitigate rust-induced physiological stress.",
            "application_advice": "Apply potassium-rich foliar feeds every 14 days during leaf expansion.",
            "avoid_fertilizer": "Avoid nitrogen overload during the 6-week spring rust infection window."
        },
        "chemical_control": {
            "active_agents": "Myclobutanil 20% EW (0.4 ml/L) or Tebuconazole 250 EC (0.7 ml/L) or Mancozeb 75% WP.",
            "spray_timing": "Apply from pink-bud stage until 3 weeks after petal fall at 7-10 day intervals."
        },
        "organic_control": {
            "remedies": "Liquid Sulfur or copper soap applied preventatively prior to rain forecasts.",
            "frequency": "Weekly applications during peak spring spore flight."
        },
        "recovery_plan": {
            "days_1_3": "Identify rust spots; spray systemic sterol-inhibitor fungicide to stop lesion expansion.",
            "days_4_10": "Inspect surrounding landscape for cedar galls; apply biostimulant kelp extract.",
            "days_14_plus": "Record rust severity for autumn cultivar planning; maintain protective cover."
        }
    },

    "Apple___healthy": {
        "crop": "Apple",
        "condition": "Healthy Foliage",
        "scientific_name": "Malus domestica (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "The leaf shows vigorous chlorophyll distribution, firm cuticle architecture, and no fungal, bacterial, or viral lesion patterns.",
        "symptoms": [
            "Vibrant green leaf blade without chlorosis or necrotic margins",
            "Smooth vein network and intact stomatal leaf underside",
            "Balanced canopy growth and robust shoot turgidity"
        ],
        "causes": "Optimal soil moisture, balanced nutrition, active beneficial rhizosphere, and adequate preventive maintenance.",
        "precautions": [
            "Maintain bi-weekly scouting routine for early signs of aphids or mite colonies.",
            "Maintain clean orchard floor with controlled groundcover or mulch.",
            "Ensure regular irrigation scheduling tailored to evapotranspiration rates."
        ],
        "fertilizers": {
            "primary_npk": "NPK 14-14-14 balanced controlled-release or organic compost top-dressing.",
            "micronutrients": "Annual maintenance dose of Boron (B) and Zinc (Zn) to support blossom and fruit set.",
            "application_advice": "Apply in two splits: 60% at bud break and 40% post-bloom. Soil pH 6.0 - 6.5.",
            "avoid_fertilizer": "Avoid late summer nitrogen applications that prevent wood hardening before winter."
        },
        "chemical_control": {
            "active_agents": "None required. Maintain IPM monitoring with pheromone traps.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Preventive foliar compost tea or cold-pressed neem oil (0.3%) as a prophylactic repellent.",
            "frequency": "Monthly preventive foliar wash."
        },
        "recovery_plan": {
            "days_1_3": "Continue standard irrigation and pruning regime.",
            "days_4_10": "Inspect new flushes; mulch tree dripline with aged woodchips.",
            "days_14_plus": "Schedule seasonal soil testing to maintain nutrient equilibrium."
        }
    },

    "Blueberry___healthy": {
        "crop": "Blueberry",
        "condition": "Healthy Bush",
        "scientific_name": "Vaccinium corymbosum (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Strong acid-loving foliage with deep glossy green coloration and healthy shoot vigor.",
        "symptoms": [
            "Glossy waxy cuticle, deep green foliage without interveinal chlorosis",
            "Active vegetative apical growth points",
            "Uniform root growth in acidic mulch matrix"
        ],
        "causes": "Acidic soil equilibrium (pH 4.5 - 5.2), high organic matter, and consistent moisture.",
        "precautions": [
            "Maintain 3-4 inches of pine bark or acidic sawdust mulch.",
            "Avoid overhead city tap water high in carbonates that elevate soil pH.",
            "Prune canes older than 6 years to stimulate new vigorous cane flushes."
        ],
        "fertilizers": {
            "primary_npk": "Ammonium sulfate (21-0-0) or special acid-forming fertilizer (NPK 10-10-10 for acid plants).",
            "micronutrients": "Chelated Iron (Fe-EDDHA) to prevent chlorosis under high pH conditions.",
            "application_advice": "Apply in three equal doses: early spring bud break, late bloom, and early summer.",
            "avoid_fertilizer": "Never use Nitrate forms of nitrogen (like Calcium Nitrate); blueberries cannot metabolize nitrate effectively."
        },
        "chemical_control": {
            "active_agents": "None required.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Elemental sulfur granules applied annually to maintain pH below 5.0.",
            "frequency": "Annual spring soil amendment."
        },
        "recovery_plan": {
            "days_1_3": "Ensure soil pH stays strictly between 4.5 and 5.0.",
            "days_4_10": "Replenish pine needle mulch around base.",
            "days_14_plus": "Monitor drip irrigation lines for uniform delivery."
        }
    },

    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "condition": "Powdery Mildew",
        "scientific_name": "Podosphaera clandestina",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Obligate fungal pathogen creating powdery white patches on leaves and fruit, causing leaf curling and fruit russeting.",
        "symptoms": [
            "White circular powdery patches of fungal mycelium on lower leaf surfaces",
            "Upward curling, twisting, and distortion of young terminal shoots",
            "Severely affected leaves become brittle and turn pale brown"
        ],
        "causes": "High relative humidity with warm, dry ambient temperatures (15-27°C) without free rain.",
        "precautions": [
            "Prune vigorous water sprouts and dense inner branches to maximize canopy airflow.",
            "Eliminate sucker growth near tree base where mildew builds up early.",
            "Avoid high nitrogen applications that stimulate lush susceptible vegetative flushes."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-20-25 with low nitrogen and elevated potassium.",
            "micronutrients": "Potassium Silicate foliar spray to deposit a physical silica barrier in epidermal cells.",
            "application_advice": "Foliar feed soluble potassium and seaweed extract. Keep soil pH at 6.3 - 6.8.",
            "avoid_fertilizer": "Avoid urea or ammonium-rich feeds during summer growth flushes."
        },
        "chemical_control": {
            "active_agents": "Triflumizole 50% WP (0.5 g/L) or Tebuconazole 25% WP (1 g/L) or Pyraclostrobin.",
            "spray_timing": "Begin at petal fall / shuck fall and repeat every 10-14 days until harvest."
        },
        "organic_control": {
            "remedies": "Potassium Bicarbonate (Kaligreen) @ 3 g/L or JMS Stylet-Oil (1-2%) or dilute milk spray (40% whole milk).",
            "frequency": "Spray weekly at dusk during dry warm periods."
        },
        "recovery_plan": {
            "days_1_3": "Prune out curled white shoot tips; apply potassium bicarbonate or horticultural oil.",
            "days_4_10": "Apply systemic DMI fungicide if infection is spreading to fruit clusters.",
            "days_14_plus": "Maintain open canopy architecture; scout weekly until harvest."
        }
    },

    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "condition": "Healthy Tree",
        "scientific_name": "Prunus cerasus (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Deep glossy green leaves with serrated margins, firm petiole attachment, and vibrant photosynthetic activity.",
        "symptoms": [
            "Intact waxy foliage without leaf spots, powdery deposits, or holes",
            "Strong terminal shoot elongation",
            "Healthy fruit buds and sturdy spur wood"
        ],
        "causes": "Balanced fertility, proper winter dormant oil sprays, and good orchard drainage.",
        "precautions": [
            "Apply dormant lime-sulfur or copper wash before spring bud swelling to prevent fungal spore germination.",
            "Maintain clean under-canopy strip to prevent rodent girdling."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-12-17 or mature compost at 15 kg/tree in late winter.",
            "micronutrients": "Boron and Calcium foliar spray at bloom to support pollination and prevent fruit cracking.",
            "application_advice": "Soil application in early spring followed by drip irrigation. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid late summer fertilization that delays winter dormancy."
        },
        "chemical_control": {
            "active_agents": "None required.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Dormant neem or horticultural mineral oil during bud break.",
            "frequency": "Single dormant application."
        },
        "recovery_plan": {
            "days_1_3": "Maintain moisture balance; check tree basin.",
            "days_4_10": "Inspect leaves for early chewing insects.",
            "days_14_plus": "Continue regular seasonal orchard maintenance."
        }
    },

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "condition": "Gray Leaf Spot",
        "scientific_name": "Cercospora zeae-maydis",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Destructive fungal foliar disease causing rectangular block lesions bounded by leaf veins, drastically reducing grain yield.",
        "symptoms": [
            "Small tan spots with yellow halos expanding into long, narrow rectangular lesions (1-6 cm)",
            "Lesions strictly delimited by parallel leaf veins, giving a blocky appearance",
            "Foliage blight turns entire upper leaves gray-brown, causing premature senescence"
        ],
        "causes": "High relative humidity (>90%), prolonged leaf dew, warm temperatures (25-32°C), and reduced-tillage residue.",
        "precautions": [
            "Rotate out of corn for at least 1-2 years with soybeans, alfalfa, or wheat.",
            "Incorporate crop residue with deep tillage to bury infected stalk debris.",
            "Select corn hybrids with high Gray Leaf Spot (GLS) tolerance ratings."
        ],
        "fertilizers": {
            "primary_npk": "NPK 18-46-0 (DAP) base followed by sidedressed Urea with high Potassium (K).",
            "micronutrients": "Zinc (Zn) sulphate and foliar Manganese (Mn) to boost plant defense enzyme production.",
            "application_advice": "Ensure adequate potassium availability; potassium deficiency severely exacerbates GLS severity. Soil pH 5.8 - 6.8.",
            "avoid_fertilizer": "Avoid unbalanced pure nitrogen without adequate potash."
        },
        "chemical_control": {
            "active_agents": "Azoxystrobin + Difenoconazole (Amistar Top @ 1 ml/L) or Pyraclostrobin (Headline @ 0.7 ml/L).",
            "spray_timing": "Apply at VT (tasseling) through R1 (silking) stage if lesions appear on the third leaf below ear or higher."
        },
        "organic_control": {
            "remedies": "Bacillus amyloliquefaciens strain D747 or copper hydroxide foliar sprays.",
            "frequency": "Preventive application before tasseling in organic production."
        },
        "recovery_plan": {
            "days_1_3": "Scout canopy: evaluate whether lesions have reached the ear leaf.",
            "days_4_10": "Apply dual-action strobilurin + triazole fungicide if threshold is exceeded.",
            "days_14_plus": "Monitor upper canopy greenness through grain-fill stage."
        }
    },

    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "condition": "Common Rust",
        "scientific_name": "Puccinia sorghi",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Fungal rust producing powdery cinnamon-brown pustules on both upper and lower leaf surfaces.",
        "symptoms": [
            "Small, oval to elongated cinnamon-brown pustules scattered over leaf surfaces",
            "Pustules rupture the epidermis releasing powdery reddish-brown urediniospores",
            "Severe infections turn leaves yellow, cause tissue necrosis, and reduce ear fill"
        ],
        "causes": "Cool to moderate temperatures (16-25°C) with high humidity and 6+ hours of dew. Spores blow in on southern winds.",
        "precautions": [
            "Plant resistant corn hybrids carrying the Rp resistance gene.",
            "Plant early in the season to avoid late-season spore flights.",
            "Maintain balanced planting density to avoid dense humid microclimates."
        ],
        "fertilizers": {
            "primary_npk": "NPK 20-10-20 balanced blend.",
            "micronutrients": "Soluble Boron (B) and chelated Zinc (Zn) to support ear formation during disease stress.",
            "application_advice": "Split nitrogen application; boost potassium (MOP) to harden stalk and leaf epidermal walls.",
            "avoid_fertilizer": "Avoid late-stage high ammonium applications."
        },
        "chemical_control": {
            "active_agents": "Azoxystrobin + Propiconazole (Quilt @ 1.5 ml/L) or Pyraclostrobin + Fluxapyroxad.",
            "spray_timing": "Spray if rust pustules cover >5% of leaves prior to or during silking."
        },
        "organic_control": {
            "remedies": "Wettable sulfur sprays (3 g/L) or bio-fungicide Bacillus subtilis.",
            "frequency": "Apply at first appearance of pustules on lower leaves."
        },
        "recovery_plan": {
            "days_1_3": "Count pustules per leaf; verify whether pustules are active or pustule rupture has ceased.",
            "days_4_10": "Apply triazole fungicide if threshold exceeded; ensure adequate potassium nutrition.",
            "days_14_plus": "Track kernel development and moisture retention."
        }
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "condition": "Northern Corn Leaf Blight",
        "scientific_name": "Exserohilum turcicum",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Devastating foliar disease characterized by large, cigar-shaped grayish-green lesions that scorch the foliage.",
        "symptoms": [
            "Long, elliptical, cigar-shaped grayish-green lesions (3 to 15 cm in length)",
            "Lesions turn tan and necrotic, with olive-green fungal spores forming under damp conditions",
            "Extensive leaf blighting gives the field a frosted, dead appearance"
        ],
        "causes": "Moderate temperatures (18-27°C) and prolonged wet periods (6-18 hours). Pathogen overwinters in corn residue.",
        "precautions": [
            "Plant resistant hybrids carrying Ht1, Ht2, or Ht3 resistance genes.",
            "Rotate fields with non-host crops like soybeans for at least 1-2 seasons.",
            "Till infected crop residue into the soil to accelerate fungal decay."
        ],
        "fertilizers": {
            "primary_npk": "NPK 15-15-20 balanced formulation.",
            "micronutrients": "Foliar Zinc sulphate (0.5%) and Magnesium sulphate to support photosynthesis.",
            "application_advice": "Ensure high potassium levels in soil; low potassium dramatically worsens blight severity.",
            "avoid_fertilizer": "Avoid excess nitrogen without balanced potassium and phosphorus."
        },
        "chemical_control": {
            "active_agents": "Azoxystrobin + Difenoconazole (Amistar Top @ 1 ml/L) or Pyraclostrobin (Headline @ 0.8 ml/L) or Mancozeb.",
            "spray_timing": "Apply at first sign of lesions on lower leaves before tasseling (V8-VT stage)."
        },
        "organic_control": {
            "remedies": "Copper octanoate or bio-fungicide Bacillus subtilis strain QST 713.",
            "frequency": "Early preventive application during wet weather cycles."
        },
        "recovery_plan": {
            "days_1_3": "Assess lesion progression relative to the ear leaf.",
            "days_4_10": "Apply systemic fungicide; supplement with potassium foliar spray.",
            "days_14_plus": "Evaluate grain fill progression; record hybrid resistance performance."
        }
    },

    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "condition": "Healthy Maize",
        "scientific_name": "Zea mays (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Broad, vibrant dark-green leaves showing high photosynthetic efficiency and strong erect stalk architecture.",
        "symptoms": [
            "Uniform dark green leaf color with clean parallel veins",
            "Erect leaf angles optimized for sunlight interception",
            "Firm nodes, healthy brace roots, and vigorous tassel development"
        ],
        "causes": "Optimal soil nitrogen-potassium ratio, timely rainfall/irrigation, and effective weed management.",
        "precautions": [
            "Scout weekly for corn borers, fall armyworms, and early leaf lesions.",
            "Maintain soil drainage to prevent root hypoxia during heavy spring rains."
        ],
        "fertilizers": {
            "primary_npk": "NPK 120-60-60 kg/ha split: basal application + sidedress urea at knee-high (V6) stage.",
            "micronutrients": "Zinc (Zn) is critical; apply 5 kg/ha Zinc sulphate at land preparation.",
            "application_advice": "Side-dress nitrogen when maize is knee-high; avoid root pruning during cultivation.",
            "avoid_fertilizer": "Avoid surface urea broadcasting without incorporation prior to high heat."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Farmyard manure (10 t/ha) or vermicompost + Azotobacter biofertilizer.",
            "frequency": "Pre-planting soil application."
        },
        "recovery_plan": {
            "days_1_3": "Monitor moisture during critical tasseling-silking window.",
            "days_4_10": "Ensure no weed competition at canopy closure.",
            "days_14_plus": "Track kernel development and test ear fill uniformity."
        }
    },

    "Grape___Black_rot": {
        "crop": "Grape",
        "condition": "Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Destructive fungal disease attacking leaves, shoots, and berry clusters, causing berries to shrivel into hard black mummies.",
        "symptoms": [
            "Small circular reddish-brown spots with dark borders on leaves",
            "Black pimple-like pycnidia fruiting bodies embedded inside leaf spots",
            "Berries turn brown, rot rapidly, and shrivel into hard, wrinkled black mummies"
        ],
        "causes": "Warm, wet weather (20-27°C) with prolonged rainfall (7+ hours). Overwinters in mummified berries and cane lesions.",
        "precautions": [
            "Prune out and destroy all mummified grape clusters from the vine and vineyard floor.",
            "Canopy management: prune leaves around grape clusters to allow rapid morning drying.",
            "Cultivate soil in early spring to bury overwintered mummies beneath 2 inches of soil."
        ],
        "fertilizers": {
            "primary_npk": "NPK 8-10-18 low nitrogen, high potassium blend.",
            "micronutrients": "Calcium and Magnesium foliar feeds to strengthen berry skin elasticity.",
            "application_advice": "Apply potassium sulphate to support grapevine vigor. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid excess nitrogen fertilizer which creates dense, shaded foliage."
        },
        "chemical_control": {
            "active_agents": "Mancozeb 75% WP (2.5 g/L) or Myclobutanil (Rally @ 0.5 g/L) or Kresoxim-methyl.",
            "spray_timing": "Apply at bud break (1-3 inches shoot length), pre-bloom, and post-bloom every 10-14 days."
        },
        "organic_control": {
            "remedies": "Bordeaux mixture (copper sulfate + hydrated lime) or copper hydroxide before rain events.",
            "frequency": "Apply preventatively every 7-10 days in wet conditions."
        },
        "recovery_plan": {
            "days_1_3": "Prune out diseased berry clusters and spotted shoots immediately.",
            "days_4_10": "Apply protective DMI or strobilurin fungicide; pull leaves around fruit zone.",
            "days_14_plus": "Inspect cluster health weekly until veraison."
        }
    },

    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "condition": "Esca (Black Measles)",
        "scientific_name": "Phaeomoniella chlamydospora & Fomitiporia mediterranea",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Complex trunk disease causing interveinal leaf tiger-striping, berry spotting ('measles'), and wood vascular necrosis.",
        "symptoms": [
            "'Tiger-stripe' leaf pattern: yellow or red interveinal chlorosis with green vein bands, turning necrotic",
            "Dark purple-brown spots with halos on berry skins ('black measles')",
            "Sudden vine collapse (apoplexy) during hot, dry spells; dark vascular streaking inside trunk wood"
        ],
        "causes": "Fungal trunk pathogens entering through winter pruning wounds. Manifests systemically as vines mature.",
        "precautions": [
            "Prune late in the dormant season when wound healing is rapid and spore flight is minimal.",
            "Treat all pruning wounds larger than 1 cm with wound sealant or Trichoderma paste.",
            "Disinfect pruning shears regularly between vines with bleach or quaternary ammonium."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-15 balanced slow-release; emphasize Potassium to support compromised vascular flow.",
            "micronutrients": "Foliar chelated iron, zinc, and magnesium to maintain residual photosynthesis in unaffected leaves.",
            "application_advice": "Avoid soil moisture stress; maintain steady drip irrigation. Soil pH 6.0 - 7.0.",
            "avoid_fertilizer": "Avoid high-salinity fertilizers and heavy nitrogen."
        },
        "chemical_control": {
            "active_agents": "No curative chemical exists. Treat pruning wounds with Thiophanate-methyl paste or pyraclostrobin.",
            "spray_timing": "Paint/spray on fresh pruning cuts within 24 hours of cutting."
        },
        "organic_control": {
            "remedies": "Trichoderma atroviride strain I-1237 applied to pruning wounds to competitively block trunk pathogens.",
            "frequency": "Apply immediately after winter pruning."
        },
        "recovery_plan": {
            "days_1_3": "Mark affected vines with surveyor tape; avoid stressing diseased vines with water deficits.",
            "days_4_10": "Apply remedial trunk renewal (training a sucker from trunk base) or curettage (scraping necrotic spongy wood).",
            "days_14_plus": "In winter, prune marked vines last to prevent transferring spores to healthy vines."
        }
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "condition": "Leaf Blight (Isariopsis Leaf Spot)",
        "scientific_name": "Pseudocercospora vitis (Isariopsis clavispora)",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Late-season foliar disease causing angular brown lesions with olive fuzzy fungal mats on the leaf underside.",
        "symptoms": [
            "Irregular, angular reddish-brown to dark brown leaf spots delimited by veins",
            "Olive-gray velvety spore clusters on the lower surface of lesions during humid periods",
            "Extensive premature defoliation in late summer, compromising fruit ripening and bud hardiness"
        ],
        "causes": "High humidity, moderate temperatures (20-28°C), and dense shaded canopies in late summer.",
        "precautions": [
            "Improve trellis airflow by removing shoots and lateral suckers in the fruit zone.",
            "Manage weeds under the vine row to eliminate ground humidity traps.",
            "Collect and compost fallen leaves after autumn harvest."
        ],
        "fertilizers": {
            "primary_npk": "NPK 6-12-18 balanced post-bloom blend.",
            "micronutrients": "Foliar Zinc (Zn) and Boron (B) to enhance vine carbohydrate storage before dormancy.",
            "application_advice": "Apply potassium foliar spray to bolster epidermal resistance. Maintain soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid late summer nitrogen feeding."
        },
        "chemical_control": {
            "active_agents": "Copper Oxychloride 50% WP (2.5 g/L) or Mancozeb 75% WP (2 g/L) or Carbendazim 50% WP (1 g/L).",
            "spray_timing": "Apply at the first appearance of leaf spots in mid-summer; repeat after 14 days."
        },
        "organic_control": {
            "remedies": "Bordeaux mixture (1%) or neem oil (0.5%) as a preventative leaf coating.",
            "frequency": "Bi-weekly sprays during rainy mid-summer periods."
        },
        "recovery_plan": {
            "days_1_3": "Prune out dense foliage blocking sunlight to inner leaves; apply copper spray.",
            "days_4_10": "Apply foliar potassium to assist remaining healthy leaves in sugar accumulation.",
            "days_14_plus": "Ensure vines hold adequate foliage until harvest to mature the crop."
        }
    },

    "Grape___healthy": {
        "crop": "Grape",
        "condition": "Healthy Grapevine",
        "scientific_name": "Vitis vinifera (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Lush, palmately lobed green foliage, strong cane elongation, and well-aerated cluster architecture.",
        "symptoms": [
            "Intact waxy green leaf blades without chlorotic spotting or curling",
            "Healthy tendril development and steady internode spacing",
            "Smooth canes with uniform lignification in late summer"
        ],
        "causes": "Well-balanced vine nutrition, excellent canopy airflow, proper trellis pruning, and timely drip irrigation.",
        "precautions": [
            "Perform regular leaf pulling around fruit zones to maintain sunlight and airflow.",
            "Keep vineyard floor mowed to reduce humidity and frost risk."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-15 slow release applied in early spring bud burst.",
            "micronutrients": "Foliar Boron (B) pre-bloom to optimize fruit set; Zinc (Zn) post-harvest.",
            "application_advice": "Drip fertigate based on petiole analysis. Soil pH 6.0 - 7.0.",
            "avoid_fertilizer": "Avoid over-fertilizing with nitrogen which creates excessive vegetative vigor and disease pockets."
        },
        "chemical_control": {
            "active_agents": "None needed. Maintain routine scouting program.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Compost tea or biodynamic silica (501) spray to promote leaf resilience.",
            "frequency": "Monthly foliar wash."
        },
        "recovery_plan": {
            "days_1_3": "Inspect canopy density; trim excess lateral shoot tips.",
            "days_4_10": "Maintain scheduled drip irrigation cycles.",
            "days_14_plus": "Monitor petiole nutrient levels and prepare for harvest."
        }
    },

    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange / Citrus",
        "condition": "Huanglongbing (Citrus Greening)",
        "scientific_name": "Candidatus Liberibacter asiaticus",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Incurable, highly destructive bacterial disease transmitted by Asian Citrus Psyllids, causing blotchy mottle leaves, bitter misshapen fruit, and tree death.",
        "symptoms": [
            "Asymmetrical blotchy mottle: yellow patterns cross veins irregularly, unlike symmetrical nutrient deficiency",
            "Vein corking, yellow veins, and upright 'rabbit-ear' leaf clusters",
            "Small, lopsided, bitter fruit that stays green at the stylar end ('greening'); inverted coloration"
        ],
        "causes": "Vector-borne phloem-limited bacterium transmitted by the Asian Citrus Psyllid (Diaphorina citri).",
        "precautions": [
            "Aggressively scout and control psyllid vector populations with systemic and contact insecticides.",
            "Plant only certified pathogen-free citrus nursery stock.",
            "Remove and destroy severely infected trees to prevent them acting as pathogen reservoirs for the grove."
        ],
        "fertilizers": {
            "primary_npk": "Enhanced Nutritional Program (ENP): balanced NPK with frequent low-dose foliar applications.",
            "micronutrients": "Foliar Zinc (Zn), Manganese (Mn), Iron (Fe), Boron (B), and Nickel (Ni) to overcome phloem transport blockage.",
            "application_advice": "Apply foliar phosphite (potassium phosphite) to stimulate systemic acquired resistance (SAR). Soil pH 6.0 - 6.5.",
            "avoid_fertilizer": "Avoid heavy single-dose soil nitrogen that triggers excessive psyllid-attracting leaf flushes."
        },
        "chemical_control": {
            "active_agents": "Control Psyllid vector: Imidacloprid (soil drench) or Thiamethoxam or Fenpropathrin / Bifenthrin spray.",
            "spray_timing": "Coordinate dormant winter psyllid sprays and target every new spring/summer vegetative flush."
        },
        "organic_control": {
            "remedies": "Release Tamarixia radiata parasitoid wasps; apply kaolin clay (Surround WP) or citrus oil sprays to deter psyllids.",
            "frequency": "Bi-weekly during vegetative flush periods."
        },
        "recovery_plan": {
            "days_1_3": "Check trees for Asian Citrus Psyllids (white wax filaments on shoots); apply immediate psyllid control spray.",
            "days_4_10": "Apply intensive foliar micronutrient cocktail (Zn, Mn, B, K-phosphite) to sustain tree production.",
            "days_14_plus": "Track grove infection percentage; eradicate non-productive trees."
        }
    },

    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "condition": "Bacterial Spot",
        "scientific_name": "Xanthomonas arboricola pv. pruni",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Bacterial infection causing angular water-soaked leaf spots, 'shot-hole' perforations, twig cankers, and pitted fruit.",
        "symptoms": [
            "Small, water-soaked polygonal lesions near leaf tips or along midribs",
            "Lesion centers dry, turn dark purple-brown, and drop out, creating a 'shot-hole' appearance",
            "Severe leaf yellowing and defoliation; sunken, cracked gumming craters on fruit"
        ],
        "causes": "Driven by wind-blown rain, sandy soils, and warm temperatures (21-27°C). Overwinters in twig cankers and buds.",
        "precautions": [
            "Plant bacterial spot-resistant peach cultivars (e.g., Candor, Dixired, Harvester).",
            "Avoid planting in wind-exposed, highly sandy sites without establishing windbreaks.",
            "Prune out dead shoots and cankers during dormant pruning."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-20 balanced orchard fertilizer.",
            "micronutrients": "Foliar Calcium and Potassium silicate to harden leaf cuticles against bacterial entry.",
            "application_advice": "Ensure adequate soil organic matter to buffer water stress. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid high spring nitrogen rates that induce tender, slow-hardening shoot growth."
        },
        "chemical_control": {
            "active_agents": "Copper hydroxide / Copper sulfate (dormant to pink bud) or Oxytetracycline (Mycoshield @ 1.5 g/L).",
            "spray_timing": "Apply low-rate copper or antibiotic sprays at 7-day intervals from petal fall through cover sprays."
        },
        "organic_control": {
            "remedies": "Low-rate copper octanoate or Serenade (Bacillus subtilis); avoid copper phytotoxicity on sensitive peach leaves.",
            "frequency": "Apply during rainy spring conditions before petal fall."
        },
        "recovery_plan": {
            "days_1_3": "Apply copper spray if pre-bloom or oxytetracycline if post-bloom.",
            "days_4_10": "Prune out blighted tips during dry weather; apply foliar calcium.",
            "days_14_plus": "Monitor fruit for pitting; maintain protective schedule during rainy spells."
        }
    },

    "Peach___healthy": {
        "crop": "Peach",
        "condition": "Healthy Peach Tree",
        "scientific_name": "Prunus persica (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Long lanceolate, rich green leaves with glossy surfaces and intact shoot extensions.",
        "symptoms": [
            "Clean lance-shaped green leaves without shot-holes, curls, or necrotic spots",
            "Vigorous shoot growth (30-45 cm new growth on bearing trees)",
            "Firm fruit development free of gumming lesions"
        ],
        "causes": "Proper dormant copper treatments, balanced nitrogen management, and good peach tree canopy pruning.",
        "precautions": [
            "Maintain open center (vase) pruning system to maximize sunlight and rapid leaf drying.",
            "Thin fruit clusters early to avoid limb breakage and fruit stress."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-10 at 450 g per year of tree age, up to 2.5 kg per mature tree.",
            "micronutrients": "Foliar Zinc and Boron after harvest while leaves remain green.",
            "application_advice": "Apply in early spring before growth begins. Soil pH 6.0 - 6.5.",
            "avoid_fertilizer": "Avoid late-summer fertilization that stimulates winter-tender growth."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Dormant neem or horticultural oil for scale and mite prevention.",
            "frequency": "Annual late-winter application."
        },
        "recovery_plan": {
            "days_1_3": "Inspect shoot terminals for oriental fruit moth or aphids.",
            "days_4_10": "Ensure soil moisture consistency via drip irrigation.",
            "days_14_plus": "Scout fruit weekly through ripening."
        }
    },

    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "condition": "Bacterial Spot",
        "scientific_name": "Xanthomonas euvesicatoria",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Devastating bacterial disease of peppers causing water-soaked leaf spots, defoliation, and rough, blistered lesions on fruit.",
        "symptoms": [
            "Small, circular to irregular water-soaked spots (1-3 mm) on foliage",
            "Spots become dark brown with greasy margins and yellow halos",
            "Lower leaves turn yellow and drop prematurely, leaving fruit exposed to sunscald"
        ],
        "causes": "Warm temperatures (24-30°C) combined with frequent rain or overhead sprinkler irrigation. Seed-borne.",
        "precautions": [
            "Use only certified disease-free, hot-water-treated seed or certified transplants.",
            "Avoid overhead irrigation; switch exclusively to drip irrigation lines beneath plastic mulch.",
            "Do not work in pepper fields while foliage is wet from dew or rain.",
            "Rotate with non-solanaceous crops (beans, corn, cabbage) for at least 2-3 years."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-11-18 with elevated Potassium and Calcium.",
            "micronutrients": "Calcium Nitrate and Boron to reinforce cell wall pectins; soluble Silicon (Si).",
            "application_advice": "Fertigate small, frequent nutrient doses. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid heavy ammonium nitrogen that promotes succulent, tender foliage."
        },
        "chemical_control": {
            "active_agents": "Copper Hydroxide 53.8% DF (2 g/L) tank-mixed with Mancozeb 75% WP (2 g/L) to break copper resistance, or Kasugamycin.",
            "spray_timing": "Begin sprays at transplanting and repeat every 7-10 days in humid rainy weather."
        },
        "organic_control": {
            "remedies": "Fixed copper bactericide (Nu-Cop) or Bacillus subtilis (Serenade) or Actinovate (Streptomyces lydicus).",
            "frequency": "Weekly preventive spray."
        },
        "recovery_plan": {
            "days_1_3": "Stop overhead watering immediately; apply copper + mancozeb bactericide tank-mix.",
            "days_4_10": "Prune severely spotted lower leaves using sanitized shears; add calcium feed.",
            "days_14_plus": "Monitor new growth flushes; maintain dry canopy environment."
        }
    },

    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "condition": "Healthy Pepper Plant",
        "scientific_name": "Capsicum annuum (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Robust, deep green foliage, erect branching habit, and prolific flower and fruit set.",
        "symptoms": [
            "Glossy, emerald-green leaves with smooth margins and no lesions",
            "Sturdy main stem and well-developed lateral fruiting branches",
            "Firm, blocky bell peppers free of blossom end rot or sunscald"
        ],
        "causes": "Consistent drip irrigation, adequate calcium uptake, warm soil, and balanced nutrition.",
        "precautions": [
            "Apply reflective mulch to deter aphids and thrips vectoring viruses.",
            "Stake or cage pepper plants to support heavy fruit loads and prevent branch snapping."
        ],
        "fertilizers": {
            "primary_npk": "NPK 15-15-15 at transplanting, shifting to NPK 12-8-24 during fruit bulking.",
            "micronutrients": "Calcium (prevents blossom-end rot) and Magnesium sulfate (Epsom salt @ 5 g/L).",
            "application_advice": "Drip fertigate weekly; ensure soil moisture remains consistently moist but not saturated. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid water fluctuations that hinder calcium transpirational movement."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Seaweed foliar extract and neem oil repellent spray.",
            "frequency": "Bi-weekly foliar tonic."
        },
        "recovery_plan": {
            "days_1_3": "Check blossom drop and soil moisture uniformity.",
            "days_4_10": "Ensure calcium supplementation during rapid fruit expansion.",
            "days_14_plus": "Maintain steady harvesting schedule to encourage continuous flowering."
        }
    },

    "Potato___Early_blight": {
        "crop": "Potato",
        "condition": "Early Blight",
        "scientific_name": "Alternaria solani",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Common fungal disease attacking older foliage first, causing distinctive dark 'target-board' concentric rings and defoliation.",
        "symptoms": [
            "Dark brown to black spots with distinct concentric rings ('target-board' pattern)",
            "Yellow halo surrounds individual lesions",
            "Symptoms start on lower, older leaves and progress upward, causing extensive leaf death"
        ],
        "causes": "Alternating periods of wet and dry weather, warm temperatures (24-29°C), and nutrient-stressed plants.",
        "precautions": [
            "Use certified disease-free seed tubers.",
            "Avoid overhead irrigation; water early in the day so foliage dries quickly.",
            "Ensure adequate nitrogen and potassium; plants stressed by malnutrition are highly susceptible.",
            "Rotate potato fields with non-solanaceous crops for at least 3 years."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-15-20 balanced potato fertilizer with high Potassium sulphate (SOP).",
            "micronutrients": "Foliar Magnesium (Mg) and Zinc (Zn) to support chlorophyll in remaining green leaves.",
            "application_advice": "Maintain steady nutrient levels throughout tuber bulking. Soil pH 5.2 - 6.4.",
            "avoid_fertilizer": "Avoid letting plants run out of nitrogen mid-season, which triggers early blight senescence."
        },
        "chemical_control": {
            "active_agents": "Chlorothalonil 720 SC (2 ml/L) or Mancozeb 75% WP (2.5 g/L) or Azoxystrobin (Amistar @ 1 ml/L).",
            "spray_timing": "Begin spraying when plants meet in the row (canopy closure) and repeat every 7-10 days."
        },
        "organic_control": {
            "remedies": "Copper octanoate or Bacillus subtilis (Serenade) or potassium bicarbonate.",
            "frequency": "Preventative spray at 7-day intervals during warm, humid conditions."
        },
        "recovery_plan": {
            "days_1_3": "Apply protectant fungicide (Chlorothalonil or Mancozeb); stop evening overhead irrigation.",
            "days_4_10": "Apply foliar potassium and magnesium to strengthen upper canopy resilience.",
            "days_14_plus": "Scout weekly; keep protective spray barrier active until vine kill."
        }
    },

    "Potato___Late_blight": {
        "crop": "Potato",
        "condition": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Extremely aggressive oomycete pathogen capable of destroying entire potato fields within 7 to 14 days and rotting tubers in storage.",
        "symptoms": [
            "Pale to dark water-soaked irregular lesions on leaves that rapidly enlarge and turn black",
            "Delicate white cottony mildew growth on the underside of infected leaves in humid morning conditions",
            "Stems develop dark greasy brown lesions; foul decaying odor in severely infected fields"
        ],
        "causes": "High humidity (>90%) and cool-to-moderate temperatures (12-24°C) with prolonged rain or fog.",
        "precautions": [
            "Plant only certified disease-free seed tubers; destroy all volunteer potatoes and cull piles.",
            "Hill potatoes deeply (cover tubers with 3-4 inches of soil) to prevent wash-down of sporangia onto tubers.",
            "Kill potato vines 2-3 weeks before harvest to ensure all foliage is dead before digging tubers."
        ],
        "fertilizers": {
            "primary_npk": "NPK 8-16-24 with high Potassium; strengthen tuber skin finish.",
            "micronutrients": "Foliar Potassium Phosphite to activate plant systemic immune defenses; Zinc and Boron.",
            "application_advice": "Drip fertigate balanced nutrients; avoid high nitrogen. Soil pH 5.5 - 6.2.",
            "avoid_fertilizer": "Strictly avoid excess nitrogen which produces excessive succulent canopy humidity."
        },
        "chemical_control": {
            "active_agents": "Cymoxanil + Mancozeb (Curzate @ 2.5 g/L) or Metalaxyl-M + Mancozeb (Ridomil Gold @ 2.5 g/L) or Mandipropamid (Revus @ 0.8 ml/L).",
            "spray_timing": "Apply immediately upon disease alert or first visual lesion; repeat every 5-7 days in wet weather."
        },
        "organic_control": {
            "remedies": "Fixed copper fungicides (Copper Hydroxide @ 2-3 g/L) applied strictly as a preventative shield.",
            "frequency": "Every 5-7 days before and during continuous rainy weather."
        },
        "recovery_plan": {
            "days_1_3": "EMERGENCY: Apply systemic anti-oomycete fungicide (e.g. Cymoxanil or Metalaxyl-M) immediately.",
            "days_4_10": "Re-spray after 5 days with translaminar fungicide; maintain deep tuber hilling.",
            "days_14_plus": "If infection cannot be checked, mow down vines to save tubers from rot."
        }
    },

    "Potato___healthy": {
        "crop": "Potato",
        "condition": "Healthy Potato Plant",
        "scientific_name": "Solanum tuberosum (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Lush, bushy green canopy with vigorous upright stems and healthy subterranean tuber initiation.",
        "symptoms": [
            "Vibrant, dark green compound leaves with firm texture and no necrotic spotting",
            "Stout, sturdy stems and vigorous flowering/tuber set",
            "Absence of leaf roll, mosaic mottling, or foliar blights"
        ],
        "causes": "Clean seed tubers, balanced fertilizer program, proper hilling, and consistent soil moisture.",
        "precautions": [
            "Maintain soil moisture at 70-80% available water capacity during tuber bulking to avoid scab.",
            "Hill plants when they are 6-8 inches tall to protect developing tubers from greening."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-20-20 basal fertilizer + sidedress nitrogen (Urea/Ammonium nitrate) before canopy closure.",
            "micronutrients": "Magnesium (Epsom salt), Zinc, and Boron to support tuber starch synthesis.",
            "application_advice": "Split nitrogen into 2-3 applications: planting, emergence, and tuber initiation. Soil pH 5.2 - 6.0.",
            "avoid_fertilizer": "Avoid lime applications that raise pH above 6.2, which triggers Common Scab (Streptomyces scabies)."
        },
        "chemical_control": {
            "active_agents": "None needed. Maintain preventative scouting.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Compost tea and organic neem repellent for Colorado potato beetles.",
            "frequency": "Bi-weekly scouting and preventive maintenance."
        },
        "recovery_plan": {
            "days_1_3": "Check moisture uniformity and inspect lower foliage for signs of blight.",
            "days_4_10": "Ensure mounds/hills are thick and free of tuber exposure.",
            "days_14_plus": "Prepare for vine desiccation before scheduled harvest."
        }
    },

    "Raspberry___healthy": {
        "crop": "Raspberry",
        "condition": "Healthy Raspberry Cane",
        "scientific_name": "Rubus idaeus (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Strong primocanes with rich green trifoliate leaves, healthy canes, and abundant lateral fruiting spurs.",
        "symptoms": [
            "Bright green leaves with serrated edges and silvery undersides",
            "Sturdy erect canes without spur blight or cane botrytis lesions",
            "Vigorous flower clusters and healthy aggregate berry formation"
        ],
        "causes": "Excellent soil drainage, raised bed culture, adequate trellis support, and annual cane pruning.",
        "precautions": [
            "Prune out spent floricanes immediately after summer harvest to increase sunlight and airflow.",
            "Trellis canes properly to prevent lodging and fruit soil contact."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-10 or 20-10-20 at 50 g/meter of row in early spring.",
            "micronutrients": "Foliar Iron (Fe) and Magnesium (Mg) to prevent chlorosis on alkaline soils.",
            "application_advice": "Apply compost mulch along the row in spring. Soil pH 5.8 - 6.5.",
            "avoid_fertilizer": "Avoid chloride-containing fertilizers; raspberries are sensitive to chloride salts."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Compost top-dressing and neem oil preventive sprays.",
            "frequency": "Seasonal maintenance."
        },
        "recovery_plan": {
            "days_1_3": "Check trellis wiring and cane tie-offs.",
            "days_4_10": "Maintain shallow drip irrigation.",
            "days_14_plus": "Scout for cane borers and spider mites."
        }
    },

    "Soybean___healthy": {
        "crop": "Soybean",
        "condition": "Healthy Soybean Plant",
        "scientific_name": "Glycine max (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Broad trifoliate leaves with uniform chlorophyll, sturdy nodules on roots, and excellent pod development.",
        "symptoms": [
            "Deep green trifoliate leaves without mosaic, rust pustules, or frog-eye spots",
            "Active pink/red Bradyrhizobium nodules on taproot (fixing atmospheric nitrogen)",
            "Uniform pod clusters at nodes with plump developing beans"
        ],
        "causes": "Successful seed inoculation, balanced phosphorus-potassium fertility, and good weed suppression.",
        "precautions": [
            "Scout for soybean cyst nematodes (SCN) and sudden death syndrome (SDS).",
            "Maintain crop rotation with corn or small grains."
        ],
        "fertilizers": {
            "primary_npk": "NPK 0-40-60 (High Phosphorus and Potassium; soybeans fix their own Nitrogen via root nodules).",
            "micronutrients": "Molybdenum (Mo) and Cobalt (Co) for nitrogenase enzyme function in nodules; Manganese (Mn).",
            "application_advice": "Apply fertilizer prior to planting. Inoculate seeds with Bradyrhizobium japonicum. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid high synthetic nitrogen fertilizers which shut down natural nodulation."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Rhizobial biofertilizer seed treatment and beneficial entomopathogens for stink bugs.",
            "frequency": "Pre-planting seed treatment."
        },
        "recovery_plan": {
            "days_1_3": "Inspect root nodules by slicing open (should be reddish-pink inside).",
            "days_4_10": "Monitor canopy closure and moisture during R3 (pod set).",
            "days_14_plus": "Track pod filling stage and scout for late-season pests."
        }
    },

    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "condition": "Powdery Mildew",
        "scientific_name": "Podosphaera xanthii",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Ubiquitous cucurbit fungal disease forming talcum-like white powdery fungal colonies across both leaf surfaces.",
        "symptoms": [
            "Circular white, powdery talc-like patches on leaves, petioles, and stems",
            "Spots spread rapidly until entire leaf surface is coated in white mycelium",
            "Leaves turn yellow, brown, and brittle, leading to premature senescence and fruit sunscald"
        ],
        "causes": "Warm temperatures (20-27°C) and high humidity; thrives in shady, dense foliage even without free moisture.",
        "precautions": [
            "Plant powdery mildew-resistant squash hybrids (PMR cultivars).",
            "Provide ample plant spacing (minimum 3-4 feet between hills) to reduce canopy humidity.",
            "Plant in full sun; powdery mildew develops rapidly in shaded microclimates."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-20 with low nitrogen and high potassium.",
            "micronutrients": "Potassium Silicate foliar spray to strengthen leaf epidermal cells against fungal haustoria penetration.",
            "application_advice": "Apply compost tea and soluble potassium to maintain vine energy. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid excess nitrogen fertilizer which stimulates lush, mildew-susceptible young foliage."
        },
        "chemical_control": {
            "active_agents": "Triflumizole (Procure @ 0.5 g/L) or Myclobutanil (Rally @ 0.5 g/L) or Azoxystrobin (Amistar @ 1 ml/L).",
            "spray_timing": "Apply at first sign of white spots on underside of older crown leaves; repeat every 7-10 days."
        },
        "organic_control": {
            "remedies": "Potassium Bicarbonate (MilStop @ 3 g/L) or Horticultural Oil (1%) or diluted milk spray (40% milk / 60% water).",
            "frequency": "Spray weekly thoroughly covering both top and bottom of leaves."
        },
        "recovery_plan": {
            "days_1_3": "Prune severely coated bottom leaves; spray potassium bicarbonate or horticultural oil.",
            "days_4_10": "Spray systemic or biological fungicide; ensure sunlight reaches lower crown.",
            "days_14_plus": "Continue bi-weekly organic sprays until fruit harvest completes."
        }
    },

    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "condition": "Leaf Scorch",
        "scientific_name": "Diplocarpon earlianum",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Common fungal disease producing numerous small, irregular purple to dark brown spots that scorch leaf blades.",
        "symptoms": [
            "Numerous small, irregular purple to reddish-brown blotches without light centers",
            "Blotches coalesce causing margins and entire leaves to curl up and look scorched or burned",
            "Lesions extend to petioles, runners, and calyxes, stunting fruit production"
        ],
        "causes": "Frequent rainfall, overhead irrigation, and prolonged leaf wetness at moderate temperatures (15-25°C).",
        "precautions": [
            "Plant on raised beds covered with straw or plastic mulch to avoid soil splash.",
            "Mow and renovate June-bearing strawberry beds immediately after harvest.",
            "Switch to drip irrigation to keep crown and foliage dry."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-20 balanced strawberry formula.",
            "micronutrients": "Calcium (prevents tip burn and strengthens tissue) and chelated Iron.",
            "application_advice": "Fertigate small amounts frequently through drip lines. Soil pH 5.5 - 6.5.",
            "avoid_fertilizer": "Avoid heavy spring nitrogen applications that produce soft, dense foliage."
        },
        "chemical_control": {
            "active_agents": "Captan 50% WP (2 g/L) or Pyraclostrobin (Cabrio @ 1 g/L) or Thiophanate-methyl (Topsin-M).",
            "spray_timing": "Apply at bud break, early bloom, and post-harvest renovation."
        },
        "organic_control": {
            "remedies": "Liquid copper soap or Bacillus subtilis (Serenade) applied preventatively.",
            "frequency": "Every 10 days in wet spring conditions."
        },
        "recovery_plan": {
            "days_1_3": "Remove and discard severely scorched leaves; ensure drip irrigation lines are clear.",
            "days_4_10": "Apply protective copper or captan spray; supply foliar calcium.",
            "days_14_plus": "Renovate beds after harvest; destroy infected foliage."
        }
    },

    "Strawberry___healthy": {
        "crop": "Strawberry",
        "condition": "Healthy Strawberry Plant",
        "scientific_name": "Fragaria x ananassa (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Compact crown with lush trifoliate dark-green leaves, vigorous runner development, and clean white blossoms.",
        "symptoms": [
            "Glossy, dark green leaves without purple spotting or burned margins",
            "Stout central crown with healthy white feeder roots",
            "Uniform conical red berries with bright green calyxes"
        ],
        "causes": "Well-drained soil, plastic or straw mulch barrier, balanced drip fertigation, and disease-free runner stock.",
        "precautions": [
            "Renew strawberry beds every 3-4 years to avoid build-up of root pathogens.",
            "Keep berries elevated off moist soil using clean straw or black plastic mulch."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-5-20 or 15-15-15 at planting, shifting to high potassium during fruiting.",
            "micronutrients": "Foliar Calcium and Boron at flowering to ensure symmetrical berry development.",
            "application_advice": "Drip feed weekly during fruit formation. Soil pH 5.8 - 6.5.",
            "avoid_fertilizer": "Avoid excess nitrogen during flowering which causes soft fruit prone to Botrytis grey mold."
        },
        "chemical_control": {
            "active_agents": "None needed.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Neem oil repellent and beneficial Trichoderma root dip.",
            "frequency": "Monthly preventive maintenance."
        },
        "recovery_plan": {
            "days_1_3": "Check mulch cover and crown height (crown should not be buried under soil).",
            "days_4_10": "Inspect flowers for tarnished plant bugs or thrips.",
            "days_14_plus": "Pick ripe fruit every 2 days to prevent attracting rodents and pests."
        }
    },

    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "condition": "Bacterial Spot",
        "scientific_name": "Xanthomonas perforans / euvesicatoria",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Widespread bacterial disease causing dark, greasy leaf spots, severe defoliation, and rough raised black scabs on tomato fruits.",
        "symptoms": [
            "Small (less than 3 mm), dark brown to black greasy water-soaked lesions on leaves",
            "Lesions develop a prominent yellow chlorotic halo and may have shot-hole centers",
            "Premature drop of infected leaves exposing green tomatoes to sunburn; raised scab-like spots on fruit"
        ],
        "causes": "Warm temperatures (24-30°C), driving rainstorms, overhead irrigation, and seed-borne bacteria.",
        "precautions": [
            "Use only certified pathogen-free seeds treated with hot water (50°C for 25 minutes).",
            "Strictly avoid overhead sprinkler irrigation; use ground drip lines.",
            "Do not prune, tie, or harvest plants when the foliage is wet.",
            "Rotate tomato crops with corn, wheat, or brassicas for a minimum of 2-3 years."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-25 with high Potassium and Calcium.",
            "micronutrients": "Calcium Nitrate (Ca(NO3)2) foliar spray and Potassium Silicate to harden cell walls.",
            "application_advice": "Fertigate via drip; avoid foliar nitrogen sprays. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid high ammonium nitrogen which softens tissue and increases bacterial invasion."
        },
        "chemical_control": {
            "active_agents": "Copper Hydroxide 53.8% DF (2 g/L) + Mancozeb 75% WP (2 g/L) tank mix, or Kasugamycin (Kasu-B).",
            "spray_timing": "Spray immediately at transplanting; repeat every 7 days during rainy spells."
        },
        "organic_control": {
            "remedies": "Bacteriophage bio-control (AgriPhage) or fixed copper bactericide or Serenade (Bacillus subtilis).",
            "frequency": "Apply twice weekly during active disease outbreak."
        },
        "recovery_plan": {
            "days_1_3": "Apply copper + mancozeb combination spray; cease overhead irrigation.",
            "days_4_10": "Prune infected bottom leaves with disinfected shears; apply foliar calcium.",
            "days_14_plus": "Monitor new top flushes; maintain clean mulch barrier."
        }
    },

    "Tomato___Early_blight": {
        "crop": "Tomato",
        "condition": "Early Blight",
        "scientific_name": "Alternaria solani",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Classic fungal disease of tomatoes causing dark concentric target-like rings on older foliage, stem cankers, and collar rot.",
        "symptoms": [
            "Dark brown to black spots with concentric rings resembling a target board",
            "Prominent yellow chlorosis surrounding each lesion",
            "Defoliation starting from the bottom foliage and moving upward toward the growing tip",
            "Sunken dark leathery lesions at the stem end of ripe or green fruits"
        ],
        "causes": "Fungal spores survive in soil and solanaceous crop debris. Thrives in warm temperatures (24-29°C) with heavy dews or rain.",
        "precautions": [
            "Prune off the lowest 12-18 inches of leaves once plants reach 3 feet tall to prevent soil splash.",
            "Apply 2-3 inches of straw or black plastic mulch around the base of plants as a splash barrier.",
            "Stake, cage, or trellis tomatoes to keep vines erect and well-aerated.",
            "Practice a strict 3-year crop rotation away from potatoes, eggplants, and peppers."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-15-25 with elevated Potassium.",
            "micronutrients": "Calcium (prevents blossom end rot) and Magnesium sulfate (Epsom salt @ 5 g/L).",
            "application_advice": "Apply balanced nutrition; early blight targets physiologically stressed, nutrient-depleted plants. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid allowing plants to exhaust nitrogen during heavy fruiting; do not over-apply rapid synthetic nitrogen."
        },
        "chemical_control": {
            "active_agents": "Chlorothalonil 720 SC (2 ml/L) or Mancozeb 75% WP (2.5 g/L) or Azoxystrobin (Amistar @ 1 ml/L).",
            "spray_timing": "Begin preventive sprays when first fruit clusters form; repeat every 7-10 days."
        },
        "organic_control": {
            "remedies": "Copper octanoate (liquid copper soap) or Bacillus subtilis (Serenade) or Trichoderma viride soil drench.",
            "frequency": "Apply every 7 days preventatively, especially following rain events."
        },
        "recovery_plan": {
            "days_1_3": "Prune out all infected bottom leaves with sanitized shears and bag for disposal; apply Chlorothalonil or Copper spray.",
            "days_4_10": "Mulch bare soil under plants with clean straw; side-dress with potassium sulfate.",
            "days_14_plus": "Inspect upper leaves weekly; maintain dry foliage."
        }
    },

    "Tomato___Late_blight": {
        "crop": "Tomato",
        "condition": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Extremely destructive oomycete disease capable of killing mature tomato plants and rotting entire fruit crops within days.",
        "symptoms": [
            "Large, irregular water-soaked greasy olive-green to brown lesions on leaves and stems",
            "White fungal-like fuzz (sporangiophores) on the undersides of leaves in humid conditions",
            "Stems develop dark brown cankers, causing sudden collapse of branches",
            "Fruits develop large, firm, greasy golden-brown blemishes that rot rapidly"
        ],
        "causes": "Cool, wet, cloudy weather (15-22°C) with relative humidity above 90%. Spores are wind-borne over tens of miles.",
        "precautions": [
            "Plant resistant tomato cultivars (e.g., Mountain Magic, Defiant PhR, Iron Lady).",
            "Space plants generously (3 feet apart) in open, breezy rows for rapid drying.",
            "Destroy and bury all volunteer tomato and potato plants in spring.",
            "Eliminate overhead watering; irrigate strictly at the root level."
        ],
        "fertilizers": {
            "primary_npk": "NPK 8-16-24 with high Potassium and low Nitrogen.",
            "micronutrients": "Foliar Potassium Phosphite (activates systemic acquired resistance); Calcium.",
            "application_advice": "Maintain robust root health with balanced humic extracts. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid high nitrogen feeds that produce excessively dense, wet canopies."
        },
        "chemical_control": {
            "active_agents": "Cymoxanil + Mancozeb (Curzate @ 2.5 g/L) or Metalaxyl-M + Mancozeb (Ridomil Gold @ 2.5 g/L) or Mandipropamid (Revus @ 0.8 ml/L).",
            "spray_timing": "Apply immediately upon disease alert or at first symptom; repeat every 5-7 days under wet conditions."
        },
        "organic_control": {
            "remedies": "Bordeaux mixture or fixed copper hydroxide applied as a heavy protective coating.",
            "frequency": "Every 5 days during persistent cool, rainy weather."
        },
        "recovery_plan": {
            "days_1_3": "EMERGENCY: Apply systemic anti-oomycete fungicide immediately; cut off severely infected stems.",
            "days_4_10": "Re-apply protective fungicide after 5 days; harvest unaffected mature green fruit early.",
            "days_14_plus": "If infection is systemic throughout the field, destroy crop to stop regional epidemic."
        }
    },

    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "condition": "Leaf Mold",
        "scientific_name": "Passalora fulva (Fulvia fulva)",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Foliar fungal disease predominant in high tunnels, polyhouses, and humid gardens, causing yellow leaf blotches and velvety olive mold.",
        "symptoms": [
            "Pale green to yellowish spots with indistinct margins on the upper leaf surface",
            "Dense olive-green to brown velvety mold growth directly beneath the spots on the lower leaf surface",
            "Leaves curl, turn brown, wither, and drop prematurely"
        ],
        "causes": "Relative humidity above 85% and temperatures of 21-24°C; very common in enclosed greenhouse structures.",
        "precautions": [
            "Ventilate greenhouses aggressively with exhaust fans and horizontal airflow fans to keep relative humidity below 80%.",
            "Avoid overhead watering; use ground drip lines.",
            "Prune lower suckers and foliage to open canopy up to sunlight."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-10-22 balanced greenhouse mix.",
            "micronutrients": "Foliar Calcium and Potassium silicate to reinforce leaf cuticles against fungal spore penetration.",
            "application_advice": "Drip feed with water-soluble nutrients. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid excess nitrogen which encourages soft, crowded vegetation."
        },
        "chemical_control": {
            "active_agents": "Difenoconazole (Score @ 0.5 ml/L) or Chlorothalonil 720 SC (2 ml/L) or Cyazofamid.",
            "spray_timing": "Apply at first sign of lower leaf mold; repeat every 10-14 days."
        },
        "organic_control": {
            "remedies": "Copper octanoate or bio-fungicide Bacillus amyloliquefaciens (Double Nickel 55).",
            "frequency": "Weekly preventive spray inside high tunnels."
        },
        "recovery_plan": {
            "days_1_3": "Open greenhouse vents and turn on circulation fans; prune infected lower leaves.",
            "days_4_10": "Apply targeted bio-fungicide or DMI fungicide; ensure night temperature heating to prevent condensation.",
            "days_14_plus": "Monitor relative humidity data loggers; ensure RH stays below 80%."
        }
    },

    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "condition": "Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Highly prevalent foliar fungal disease causing hundreds of tiny circular spots with dark margins and grayish centers, leading to rapid defoliation.",
        "symptoms": [
            "Numerous small (1.5-3 mm) circular spots with dark brown margins and sunken grayish-white centers",
            "Tiny black speckles (pycnidia fruiting bodies) visible inside the center of each spot",
            "Lower leaves turn yellow and drop off, leaving bare lower stems and sunscalded fruit"
        ],
        "causes": "Warm temperatures (20-25°C), high humidity, and rain splash spreading soil-borne spores onto lower leaves.",
        "precautions": [
            "Mulch heavily beneath plants with clean straw or plastic to eliminate soil splash.",
            "Prune off the bottom 12 inches of foliage as plants grow.",
            "Never work among tomato plants while leaves are wet.",
            "Rotate crops for at least 3 years away from solanaceous plants."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-15-25 with high Potassium.",
            "micronutrients": "Foliar Potassium Silicate and Calcium to thicken epidermal leaf walls.",
            "application_advice": "Fertigate through drip lines; maintain steady soil moisture. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid high ammonium nitrogen which softens leaf tissue."
        },
        "chemical_control": {
            "active_agents": "Chlorothalonil 720 SC (2 ml/L) or Mancozeb 75% WP (2.5 g/L) or Azoxystrobin (Amistar @ 1 ml/L).",
            "spray_timing": "Apply every 7-10 days starting right after transplanting or at first symptom."
        },
        "organic_control": {
            "remedies": "Copper Hydroxide or Serenade (Bacillus subtilis) or potassium bicarbonate.",
            "frequency": "Apply every 7 days during rainy spells."
        },
        "recovery_plan": {
            "days_1_3": "Prune out all spotted lower leaves and dispose away from the garden; apply protectant fungicide.",
            "days_4_10": "Install heavy straw mulch barrier; apply foliar potassium feed.",
            "days_14_plus": "Keep foliage dry; inspect mid-canopy leaves weekly."
        }
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "condition": "Spider Mites (Two-Spotted Spider Mite)",
        "scientific_name": "Tetranychus urticae",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Microscopic arachnid pests that pierce plant cells on leaf undersides, sucking sap and spinning fine protective webbing.",
        "symptoms": [
            "Fine white to yellow stippling (tiny speckled dots) on the upper leaf surface",
            "Leaves take on a bronzed, dusty, or scorched appearance and dry up",
            "Fine silky webbing visible on leaf undersides, growing tips, and between stems",
            "Stunted plant growth and severely reduced fruit sizing"
        ],
        "causes": "Hot, dry, and dusty weather (temperatures above 30°C); drought stress accelerates reproduction.",
        "precautions": [
            "Avoid letting tomato plants experience drought stress; maintain consistent root moisture.",
            "Wash down dusty roadways and field margins to reduce dust settling on leaves.",
            "Avoid broad-spectrum synthetic pyrethroid insecticides which kill natural predatory mites."
        ],
        "fertilizers": {
            "primary_npk": "NPK 14-14-20 balanced feed.",
            "micronutrients": "Seaweed/kelp extract foliar sprays to boost plant tolerance to sap-sucking stress.",
            "application_advice": "Ensure adequate soil potassium and calcium. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid excessive nitrogen fertilizers; high amino acid content in sap accelerates spider mite reproduction."
        },
        "chemical_control": {
            "active_agents": "Abamectin 1.8% EC (0.5 ml/L) or Spiromesifen 22.9% SC (1 ml/L) or Bifenazate (Floramite).",
            "spray_timing": "Apply miticide thoroughly targeting leaf undersides; repeat after 5-7 days to kill newly hatched eggs."
        },
        "organic_control": {
            "remedies": "Cold-pressed Neem Oil (1%) or Insecticidal Soap (potassium salts of fatty acids) or release predatory mites (Phytoseiulus persimilis).",
            "frequency": "Spray weekly thoroughly wetting the undersides of all leaves."
        },
        "recovery_plan": {
            "days_1_3": "Spray undersides of leaves with strong jet of water or insecticidal soap / miticide.",
            "days_4_10": "Re-spray 5-7 days later to destroy emerging mite nymphs; mulch to suppress dust.",
            "days_14_plus": "Scout weekly with a 10x hand lens; monitor predatory mite activity."
        }
    },

    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "condition": "Target Spot",
        "scientific_name": "Corynespora cassiicola",
        "status": "Infected",
        "severity": "Moderate",
        "overview": "Fungal foliar disease causing circular pinpoint lesions that expand with concentric rings, attacking leaves, stems, and fruits.",
        "symptoms": [
            "Small, pinpoint lesions that enlarge into circular brown lesions with light brown centers and dark concentric rings",
            "Lesions rupture and become ragged or torn in older stages",
            "Sunken, crater-like dark brown spots on green and ripe tomato fruits"
        ],
        "causes": "Warm, humid climates (20-28°C) with long periods of high humidity and free moisture on foliage.",
        "precautions": [
            "Maintain wide plant spacing and prune excess suckers to facilitate rapid canopy drying.",
            "Avoid overhead watering; irrigate strictly at soil level.",
            "Rake and eliminate all solanaceous crop residues after harvest."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-12-24 with high Potassium.",
            "micronutrients": "Calcium and soluble Silicon to bolster epidermal leaf cell wall strength.",
            "application_advice": "Drip feed balanced nutrients. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid excess nitrogen fertilizer that promotes dense, enclosed vegetative canopies."
        },
        "chemical_control": {
            "active_agents": "Azoxystrobin + Difenoconazole (Amistar Top @ 1 ml/L) or Fluxapyroxad + Pyraclostrobin (Priaxor) or Chlorothalonil.",
            "spray_timing": "Apply protectant sprays when first symptoms appear; repeat at 10-day intervals."
        },
        "organic_control": {
            "remedies": "Fixed copper fungicides or Bacillus subtilis (Serenade).",
            "frequency": "Bi-weekly preventative applications during warm, humid weather."
        },
        "recovery_plan": {
            "days_1_3": "Prune out diseased leaves; apply broad-spectrum protectant fungicide.",
            "days_4_10": "Ensure canopy airflow; apply foliar calcium and potassium.",
            "days_14_plus": "Inspect developing fruit clusters for crater lesions."
        }
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "condition": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "scientific_name": "Begomovirus (TYLCV)",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Severe viral disease transmitted exclusively by whiteflies (Bemisia tabaci), causing stunted growth, cupped yellow leaves, and total fruit drop.",
        "symptoms": [
            "Upward curling, cupping, and crumpling of leaf margins",
            "Interveinal yellowing (chlorosis) of young leaves; leaves become small, puckered, and leathery",
            "Severe plant stunting, shortened internodes, and compact 'bushy' appearance",
            "Flower buds drop prematurely, leading to negligible fruit set"
        ],
        "causes": "Vector-transmitted by Silverleaf Whiteflies (Bemisia tabaci). No chemical cure exists once the plant is infected.",
        "precautions": [
            "Plant TYLCV-resistant or tolerant tomato hybrids (e.g., Tycoon, Camaro, Charger).",
            "Use 50-mesh insect-proof netting in greenhouses and nursery seedling beds.",
            "Install yellow sticky traps (1 trap per 10-20 sq meters) to monitor and trap whitefly populations.",
            "Pull out and burn severely infected plants immediately to prevent acting as a virus reservoir."
        ],
        "fertilizers": {
            "primary_npk": "NPK 12-12-18 balanced liquid fertilizer.",
            "micronutrients": "Foliar Zinc, Boron, and amino acids to reduce physiological viral shock in mildly infected plants.",
            "application_advice": "Do not force heavy growth in symptomatic plants. Soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid heavy nitrogen feeding which encourages soft flush attractive to whiteflies."
        },
        "chemical_control": {
            "active_agents": "Target the Whitefly vector: Dinotefuran (Venom) or Spiromesifen (Oberon @ 1 ml/L) or Pyriproxyfen (growth regulator).",
            "spray_timing": "Spray whiteflies at early nymph/adult stage; alternate chemical classes to avoid insecticide resistance."
        },
        "organic_control": {
            "remedies": "Neem oil (1%) or insecticidal potassium soaps or Beauveria bassiana (entomopathogenic fungus); reflective silver mulch.",
            "frequency": "Spray whiteflies every 4-5 days during active flight."
        },
        "recovery_plan": {
            "days_1_3": "Isolate or rogue out stunted viral plants; apply immediate systemic whitefly knockdown spray.",
            "days_4_10": "Install yellow sticky cards; hang reflective silver mulch strips along row edges.",
            "days_14_plus": "Monitor whitefly counts on new flushes; maintain clean buffer perimeter."
        }
    },

    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "condition": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tobamovirus (ToMV)",
        "status": "Infected",
        "severity": "Severe",
        "overview": "Highly stable, easily transmitted viral disease causing leaf mottling, blistering, distortion, and fruit internal browning.",
        "symptoms": [
            "Mottled light and dark green mosaic patterns on leaves",
            "Leaf distortion, blistering, curling, or strap-like 'shoestring' narrowing of leaflets",
            "Stunted plant growth and reduced fruit yield with internal brown necrosis inside fruits"
        ],
        "causes": "Mechanically transmitted via handling, pruning shears, contaminated clothing, and tobacco products. Extremely persistent in soil and dry debris.",
        "precautions": [
            "Select ToMV-resistant cultivars (marked with 'T' or 'ToMV' on seed packets).",
            "Workers must wash hands thoroughly with soap and water or 20% skim milk before handling plants.",
            "Strictly ban smoking or chewing tobacco products inside or near tomato plots.",
            "Disinfect pruning tools by dipping in a 10% trisodium phosphate (TSP) or 20% non-fat dry milk solution."
        ],
        "fertilizers": {
            "primary_npk": "NPK 10-10-20 balanced formulation.",
            "micronutrients": "Foliar trace elements and humic acids to sustain remaining functional foliage.",
            "application_advice": "Supply balanced nutrition without over-stimulating growth. Soil pH 6.2 - 6.8.",
            "avoid_fertilizer": "Avoid high nitrogen which accelerates viral systemic multiplication."
        },
        "chemical_control": {
            "active_agents": "No chemical viricide exists. Disinfect tools with Trisodium Phosphate (TSP 10%) or Virkon-S.",
            "spray_timing": "Dip tools continuously during pruning."
        },
        "organic_control": {
            "remedies": "Dip hands and tools in whole milk or 20% dry milk solution while handling plants; rogue out infected plants.",
            "frequency": "Every handling event."
        },
        "recovery_plan": {
            "days_1_3": "Carefully dig up and incinerate infected mosaic plants; avoid touching adjacent healthy plants.",
            "days_4_10": "Disinfect all stakes, cages, and tools in TSP or bleach solution.",
            "days_14_plus": "Scout neighboring plants for mosaic symptoms; record clean seed sources."
        }
    },

    "Tomato___healthy": {
        "crop": "Tomato",
        "condition": "Healthy Tomato Plant",
        "scientific_name": "Solanum lycopersicum (Healthy)",
        "status": "Healthy",
        "severity": "Optimal",
        "overview": "Vigorous, dark-green indeterminate or determinate vine with robust stem caliper, clean foliage, and prolific flowering trusses.",
        "symptoms": [
            "Rich deep green compound leaves with crisp margins and no chlorosis or spots",
            "Sturdy, thick central stem covered in healthy glandular trichomes",
            "Vibrant yellow blossoms and uniform, firm fruit trusses free of blemishes"
        ],
        "causes": "Optimal root aeration, steady drip irrigation, balanced N-P-K-Ca nutrition, and disciplined pruning.",
        "precautions": [
            "Prune non-fruiting lower suckers to maintain single or double leader architecture for maximum airflow.",
            "Maintain 2-3 inches of clean organic straw mulch to keep soil temperatures regulated and prevent water evaporation.",
            "Scout weekly for early hornworms, aphids, and foliar spotting."
        ],
        "fertilizers": {
            "primary_npk": "NPK 15-15-15 during early vegetative growth, transitioning to NPK 10-10-30 or 12-8-24 during fruit sizing and ripening.",
            "micronutrients": "Calcium Nitrate (Ca(NO3)2 @ 2 g/L) weekly to prevent blossom end rot; Magnesium sulfate (Epsom salt @ 5 g/L).",
            "application_advice": "Drip fertigate in split weekly doses. Maintain soil pH between 6.2 and 6.8.",
            "avoid_fertilizer": "Avoid erratic watering and large single-dose nitrogen applications that trigger blossom drop and hollow fruit."
        },
        "chemical_control": {
            "active_agents": "None needed. Maintain proactive scouting and sticky traps.",
            "spray_timing": "N/A"
        },
        "organic_control": {
            "remedies": "Foliar cold-pressed neem oil (0.5%) and compost tea as an organic prophylactic wash.",
            "frequency": "Every 14 days as an organic defense tonic."
        },
        "recovery_plan": {
            "days_1_3": "Check trellis clips or ties; maintain consistent morning drip watering.",
            "days_4_10": "Ensure calcium supplementation during rapid fruit expansion.",
            "days_14_plus": "Prune out old bottom leaves as lower fruit clusters ripen to direct energy upward."
        }
    }
}

# 38 PlantVillage Ordered Class Mapping
ORDERED_CLASSES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

def get_disease_profile(class_name):
    """Retrieves full agronomic profile for a class, falling back to a structured default if missing."""
    if class_name in DISEASE_PROFILES:
        return DISEASE_PROFILES[class_name]
    
    # Generic fallback parser
    parts = class_name.split('___')
    crop = parts[0].replace('_', ' ')
    condition = parts[1].replace('_', ' ') if len(parts) > 1 else 'General Condition'
    is_healthy = 'healthy' in condition.lower()
    
    return {
        "crop": crop,
        "condition": condition,
        "scientific_name": f"{crop} species",
        "status": "Healthy" if is_healthy else "Infected",
        "severity": "Optimal" if is_healthy else "Moderate",
        "overview": f"Detected {condition} on {crop} foliage.",
        "symptoms": [f"Visual markers typical of {condition} on {crop} leaf tissue."],
        "causes": "Environmental factors, seasonal weather variation, or localized pathogen presence.",
        "precautions": [
            "Sanitize pruning equipment regularly.",
            "Water at the base of plants to minimize prolonged leaf wetness.",
            "Ensure proper spacing to promote adequate air circulation."
        ],
        "fertilizers": {
            "primary_npk": "Balanced NPK 15-15-15 or organic slow-release compost.",
            "micronutrients": "Foliar micronutrient blend with Zinc, Iron, and Magnesium.",
            "application_advice": "Apply according to soil test recommendations. Maintain soil pH 6.0 - 6.8.",
            "avoid_fertilizer": "Avoid excess nitrogen during periods of disease activity."
        },
        "chemical_control": {
            "active_agents": "Consult a local agricultural extension specialist for registered plant protectants.",
            "spray_timing": "Apply at the earliest sign of infection according to label instructions."
        },
        "organic_control": {
            "remedies": "Cold-pressed Neem Oil (0.5%) or bio-fungicide Bacillus subtilis.",
            "frequency": "Apply every 7-10 days preventatively."
        },
        "recovery_plan": {
            "days_1_3": "Isolate or prune visibly damaged leaves; ensure plant is not water-stressed.",
            "days_4_10": "Apply balanced micronutrient foliar spray; monitor progression.",
            "days_14_plus": "Record observations and adjust cultural practices for next season."
        }
    }

def get_healthy_counterpart(class_name):
    """Finds the corresponding healthy reference class for the same crop."""
    crop_prefix = class_name.split('___')[0]
    candidate = f"{crop_prefix}___healthy"
    if candidate in ORDERED_CLASSES:
        return candidate
    return None
