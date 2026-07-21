#!/usr/bin/env python3
"""Generator for the 75 species that grow the guide from 25 to 100.
Original wording. Facts are field-guide level; cautions are deliberately
conservative because foraging is a safety domain. Photo credits come from
scripts/credits_by_slug.json (Wikimedia Commons fetch)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEST = os.path.join(ROOT, "src", "content", "plants")
CREDITS = json.load(open(os.path.join(HERE, "credits_by_slug.json")))

P = []
def plant(slug, **kw): kw["slug"] = slug; P.append(kw)

SAFE = "Never eat a wild plant on this guide's word alone. Confirm identity against several sources and learn the look-alikes first."

# ---- FRUITS & BERRIES ----
plant("american-persimmon", name="American Persimmon", latin="Diospyros virginiana", family="Ebony",
  abundance="common", type="Tree", uses=["Fruit"], regions=["East","Central"], months=[9,10,11],
  facts={"what":"Orange fruit, dead ripe only","how":"Raw, pudding, dried into fruit leather","when":"After first frosts, September to November","where":"East Texas woods and old fields","value":"Sugars, vitamin C, fiber"},
  caution="Underripe fruit is mouth-puckeringly astringent. Take only fruit that is soft, wrinkled, and falling on its own. "+SAFE,
  sections=[{"title":"Harvesting","body":"Patience is the whole skill. A persimmon that fights you off the branch will dry your mouth to felt; one that drops into your palm tastes of dates and honey. Gather from the ground after a frost."},
    {"title":"In the kitchen","body":"Run ripe fruit through a food mill to lose the seeds, then bake the pulp into puddings and quick breads or spread it thin and dry it into leather."}],
  similar=["texas-persimmon","mayhaw"])

plant("mexican-plum", name="Mexican Plum", latin="Prunus mexicana", family="Rose",
  abundance="common", type="Tree", uses=["Fruit"], regions=["Central","East"], months=[7,8,9], flowerMonths=[3],
  facts={"what":"Purple-red plums","how":"Raw, jam, jelly","when":"Late summer","where":"Woodland edges, fence rows, creek banks","value":"Sugars, vitamin C"},
  caution="Eat the flesh, never the cracked pits: like all wild cherries and plums the seeds carry cyanide-forming compounds. "+SAFE,
  sections=[{"title":"Harvesting","body":"A single small tree can hang heavy with tart, thin-skinned plums. Pick the softest, darkest fruit; the tree fruits unevenly, so come back over a couple of weeks."},
    {"title":"In the kitchen","body":"Tart and a little wild, Mexican plums make a jam or jelly with far more character than a grocery plum. Cook, strain, and sweeten."}],
  similar=["chickasaw-plum","black-cherry"])

plant("chickasaw-plum", name="Chickasaw Plum", latin="Prunus angustifolia", family="Rose",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["East","Central"], months=[6,7], flowerMonths=[3],
  facts={"what":"Small red-yellow plums","how":"Raw, jelly, sauce","when":"Early summer","where":"Thickets, roadsides, old fields","value":"Sugars, vitamin C"},
  caution="Flesh only; discard cracked pits (cyanide-forming compounds). "+SAFE,
  sections=[{"title":"Harvesting","body":"Chickasaw plums grow in dense sun-loving thickets that turn red in June. The fruit is smaller than a Mexican plum but sweeter when fully ripe."},
    {"title":"In the kitchen","body":"Their high pectin makes them a jelly-maker's favorite: they set firm with little help."}],
  similar=["mexican-plum","dewberry"])

plant("black-cherry", name="Black Cherry", latin="Prunus serotina", family="Rose",
  abundance="common", type="Tree", uses=["Fruit"], regions=["East","Central"], months=[6,7,8], flowerMonths=[4],
  facts={"what":"Small dark cherries","how":"Cooked into syrup, jelly, wine; raw sparingly","when":"Midsummer","where":"Woods and fence rows across the eastern half","value":"Sugars, antioxidants"},
  caution="Ripe fruit is fine, but the pits, leaves, twigs, and bark all contain cyanide-forming compounds; never chew the seeds and keep the greenery out. "+SAFE,
  sections=[{"title":"Harvesting","body":"Fully black cherries are sweet with a bitter-almond edge. Strip whole clusters and expect to lose half the weight to seeds."},
    {"title":"In the kitchen","body":"Cooked and strained, black cherry becomes a deep, aromatic syrup that was the original flavor behind old-time cherry sodas."}],
  similar=["mexican-plum","red-mulberry"])

plant("red-mulberry", name="Red Mulberry", latin="Morus rubra", family="Mulberry",
  abundance="common", type="Tree", uses=["Fruit"], regions=["East","Central"], months=[4,5,6],
  facts={"what":"Dark red-black berries","how":"Raw by the handful, pie, jam","when":"Spring into early summer","where":"Woods, yards, fence rows","value":"Sugars, vitamin C, iron"},
  caution="Eat only fully ripe (dark) berries; unripe white-and-green fruit and the milky sap can upset the stomach. "+SAFE,
  sections=[{"title":"Harvesting","body":"Spread a sheet and shake the branches: ripe mulberries rain down and stain everything a cheerful purple. Wash and use quickly, as they don't keep."},
    {"title":"In the kitchen","body":"Sweet and mild, a little flat on their own, so cooks brighten them with lemon in pies and jams."}],
  similar=["dewberry","black-cherry"])

plant("muscadine", name="Muscadine Grape", latin="Vitis rotundifolia", family="Grape",
  abundance="common", type="Vine", uses=["Fruit"], regions=["East"], months=[8,9,10],
  facts={"what":"Large thick-skinned grapes","how":"Raw, juice, jelly, wine","when":"Late summer into fall","where":"East Texas woods, climbing high into trees","value":"Sugars, antioxidants"},
  caution="No toxic look-alikes when the fruit is present, but confirm the plant before eating any wild grape relative. "+SAFE,
  sections=[{"title":"Harvesting","body":"Muscadines hang high; the ripe ones drop, so check the ground under a loaded vine in September. Pop the sweet pulp from the tough skin with your teeth."},
    {"title":"In the kitchen","body":"The famous Southern grape: heavy, musky, and sweet. Cook the skins with the pulp for jelly the color of garnet."}],
  similar=["mustang-grape","maypop"])

plant("farkleberry", name="Farkleberry", latin="Vaccinium arboreum", family="Heath",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["East"], months=[9,10],
  facts={"what":"Small black berries","how":"Cooked; raw only a nibble","when":"Fall","where":"Sandy East Texas woods","value":"A wild relative of the blueberry"},
  caution="Edible but dry and seedy raw; best cooked. "+SAFE,
  sections=[{"title":"Identification","body":"A tough evergreen blueberry cousin whose small black fruit stays hard and seedy. Not a trailside treat, but a real ingredient once cooked down."},
    {"title":"In the kitchen","body":"Simmer with sugar and a splash of water to coax out what sweetness there is; the flavor is genuinely blueberry."}],
  similar=["beautyberry","elderberry"])

plant("rusty-blackhaw", name="Rusty Blackhaw", latin="Viburnum rufidulum", family="Moschatel",
  abundance="uncommon", type="Shrub", uses=["Fruit"], regions=["Central","East"], months=[9,10],
  facts={"what":"Blue-black berries with a bloom","how":"Raw ripe, or cooked into a preserve","when":"Fall","where":"Woodland edges and slopes","value":"Sugars"},
  caution="Eat only fully soft, dark, sweet fruit; the flat seed is not eaten. "+SAFE,
  sections=[{"title":"Identification","body":"A small tree with glossy leaves that flare red in autumn and clusters of raisin-sweet blue-black fruit dusted with a pale bloom."},
    {"title":"In the kitchen","body":"Ripe fruit tastes of dates and prunes; the thin flesh around the seed makes a modest but pleasant preserve."}],
  similar=["american-persimmon","farkleberry"])

plant("texas-madrone", name="Texas Madrone", latin="Arbutus xalapensis", family="Heath",
  abundance="uncommon", type="Tree", uses=["Fruit"], regions=["West","Central"], months=[9,10,11],
  facts={"what":"Red-orange berries","how":"Raw or cooked","when":"Fall","where":"Rocky Hill Country and West Texas slopes","value":"Sugars"},
  caution="Mealy and only mildly sweet; eaten in moderation. Prized more as a beautiful tree than a heavy food. "+SAFE,
  sections=[{"title":"Identification","body":"Unmistakable smooth peeling bark in cream, pink, and terracotta, with clusters of round red-orange fruit. A slow-growing Hill Country treasure worth protecting."},
    {"title":"In the kitchen","body":"The grainy berries are pleasant fresh in small amounts and cook into a mild jelly."}],
  similar=["texas-persimmon","agarita"])

plant("mayhaw", name="Mayhaw", latin="Crataegus opaca", family="Rose",
  abundance="uncommon", type="Tree", uses=["Fruit"], regions=["East"], months=[4,5], flowerMonths=[2,3],
  facts={"what":"Small red haws","how":"The classic jelly; juice","when":"May, as the name says","where":"Wet bottomlands and swamp edges of East Texas","value":"Sugars, pectin, vitamin C"},
  caution="Eat the flesh; the small seeds are not chewed. "+SAFE,
  sections=[{"title":"Harvesting","body":"Mayhaws drop into the water and shallows below the tree; traditional gatherers float them out with nets. A wet-footed harvest with a devoted following."},
    {"title":"In the kitchen","body":"Mayhaw jelly is a genuine Southern delicacy, tart and bright pink, and the whole reason anyone learns this tree."}],
  similar=["southern-crabapple","chickasaw-plum"])

plant("southern-crabapple", name="Southern Crabapple", latin="Malus angustifolia", family="Rose",
  abundance="uncommon", type="Tree", uses=["Fruit"], regions=["East"], months=[9,10],
  facts={"what":"Small hard green-yellow apples","how":"Cooked into jelly, butter, cider","when":"Fall","where":"East Texas woods and old homesteads","value":"Pectin, vitamin C"},
  caution="Very sour and hard raw; always cooked. As with all apples, do not eat the seeds in quantity. "+SAFE,
  sections=[{"title":"Harvesting","body":"Fragrant pink spring blossoms give way to golf-ball apples too tart to bite. Gather them for the pot, not the hand."},
    {"title":"In the kitchen","body":"Their sky-high pectin makes crabapples the secret weapon of jelly makers; they also cook into a fragrant apple butter."}],
  similar=["mayhaw","american-persimmon"])

plant("blackberry", name="Southern Blackberry", latin="Rubus argutus", family="Rose",
  abundance="abundant", type="Vine", uses=["Fruit"], regions=["East","Central"], months=[5,6],
  facts={"what":"Black aggregate berries","how":"Raw, cobbler, jam","when":"Late spring into summer","where":"Sunny fence rows, clearings, roadsides","value":"Sugars, vitamin C, fiber"},
  caution="No toxic look-alikes; the only hazards are thorns and the chiggers in the patch. "+SAFE,
  sections=[{"title":"Harvesting","body":"Upright thorny canes, unlike the ground-running dewberry. Pick fruit that is fully dull-black and releases at a touch; red means wait."},
    {"title":"In the kitchen","body":"The archetypal wild berry. Eat them warm off the cane, or bake the survivors into a cobbler."}],
  similar=["dewberry","red-mulberry"])

plant("anacua", name="Anacua", latin="Ehretia anacua", family="Borage",
  abundance="uncommon", type="Tree", uses=["Fruit"], regions=["West","Central"], months=[5,6,9,10],
  facts={"what":"Small orange-yellow fruit","how":"Raw","when":"Spring and again in fall","where":"South and Central Texas brushland","value":"Sugars"},
  caution="Mild and sweet, eaten fresh in small amounts. "+SAFE,
  sections=[{"title":"Identification","body":"The 'sandpaper tree,' named for its rough leaves, drops fragrant white flower clusters and then sweet orange fruit that birds adore."},
    {"title":"On the trail","body":"A pleasant fresh nibble rather than a kitchen crop; the fruit is small and mostly seed."}],
  similar=["brasil-bluewood","anacahuita"])

plant("brasil-bluewood", name="Brasil", latin="Condalia hookeri", family="Buckthorn",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["West"], months=[6,7,8,9],
  facts={"what":"Small black fruit","how":"Raw, jelly","when":"Summer into fall","where":"South Texas brush country","value":"Sugars"},
  caution="Edible when fully black and soft; the thorns are serious. "+SAFE,
  sections=[{"title":"Identification","body":"A dense thorny brush-country shrub, also called bluewood, whose tiny black fruit is sweet and a little tart."},
    {"title":"In the kitchen","body":"Gathered in quantity it makes a dark jelly; on the trail it is a welcome sweet in dry country."}],
  similar=["lotebush","anacua"])

plant("lotebush", name="Lotebush", latin="Ziziphus obtusifolia", family="Buckthorn",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["West"], months=[7,8,9],
  facts={"what":"Small blue-black fruit","how":"Raw","when":"Summer","where":"Dry South and West Texas","value":"Sugars"},
  caution="Edible in small amounts when ripe; a spiny, tangled shrub to reach into carefully. "+SAFE,
  sections=[{"title":"Identification","body":"A gray, zig-zagging thorny shrub of dry ground, a wild relative of the jujube, with thin sweet fruit around a large stone."},
    {"title":"On the trail","body":"More survival food than delicacy, but a real one where little else grows."}],
  similar=["brasil-bluewood","wolfberry"])

plant("wolfberry", name="Texas Wolfberry", latin="Lycium carolinianum", family="Nightshade",
  abundance="uncommon", type="Shrub", uses=["Fruit"], regions=["West","Central"], months=[9,10,11],
  facts={"what":"Small red berries","how":"Raw or cooked","when":"Fall","where":"Coastal flats and dry South Texas","value":"A wild goji relative"},
  caution="This is the nightshade family: eat ONLY the ripe red berries of correctly identified wolfberry, never leaves or unripe fruit, and be certain of the plant. "+SAFE,
  sections=[{"title":"Identification","body":"A wild cousin of the cultivated goji, with small red berries on a spiny succulent-leaved shrub. Nightshade family means positive ID matters more than usual."},
    {"title":"In the kitchen","body":"The ripe berries are mildly sweet-savory and were a traditional food, eaten fresh or dried."}],
  similar=["ground-cherry","chile-pequin"])

plant("anacahuita", name="Anacahuita", latin="Cordia boissieri", family="Borage",
  abundance="uncommon", type="Shrub", uses=["Fruit"], regions=["West"], months=[6,7,8,9],
  facts={"what":"White-fleshed fruit; showy flowers","how":"Fruit cooked into a preserve","when":"Summer","where":"South Texas, the 'wild olive'","value":"Sugars"},
  caution="The fruit is eaten cooked and in moderation; large amounts of the raw fruit can be purgative. "+SAFE,
  sections=[{"title":"Identification","body":"Big crepe-papery white flowers with yellow throats bloom much of the year on this South Texas shrub, followed by pale olive-like fruit."},
    {"title":"In the kitchen","body":"Traditionally simmered into a sweet preserve; the flowers are also used in folk remedies."}],
  similar=["anacua","brasil-bluewood"])

plant("maypop", name="Maypop", latin="Passiflora incarnata", family="Passionflower",
  abundance="common", type="Vine", uses=["Fruit","Tea"], regions=["East","Central"], months=[7,8,9], flowerMonths=[5,6,7],
  facts={"what":"Egg-sized green fruit; leaves for tea","how":"Ripe pulp raw; dried leaves as calming tea","when":"Late summer","where":"Fence rows, fields, roadsides","value":"Vitamin C; the pulp is fragrant and tart"},
  caution="Eat only the pulp of ripe (yellowed, wrinkling) fruit; green unripe maypops are unpleasant. "+SAFE,
  sections=[{"title":"Identification","body":"The intricate purple-and-white passionflower is unmistakable; the fruit 'pops' underfoot when ripe, hence the name."},
    {"title":"Uses","body":"Scoop the sweet-tart seedy pulp straight from a ripe fruit. The dried leaves make a traditional mild, calming tea."}],
  similar=["muscadine","turks-cap"])

plant("ground-cherry", name="Ground Cherry", latin="Physalis longifolia", family="Nightshade",
  abundance="common", type="Ground", uses=["Fruit"], regions=["East","Central","West"], months=[7,8,9],
  facts={"what":"Small fruit inside a papery husk","how":"Raw when ripe, or into jam and sauce","when":"Summer into fall","where":"Fields, gardens, disturbed ground","value":"Vitamin C"},
  caution="Eat ONLY fruit that is ripe and golden inside a dry, tan husk. The green unripe fruit, leaves, and stems are toxic (nightshade family). "+SAFE,
  sections=[{"title":"Identification","body":"A wild tomatillo: each fruit hangs inside a Chinese-lantern husk. Ripe fruit falls to the ground and yellows; that is your only safe signal."},
    {"title":"In the kitchen","body":"Ripe ground cherries taste of sweet tomato and pineapple, wonderful raw or cooked into a jam."}],
  similar=["wolfberry","chile-pequin"])

plant("wild-strawberry", name="Wild Strawberry", latin="Fragaria virginiana", family="Rose",
  abundance="uncommon", type="Ground", uses=["Fruit"], regions=["East"], months=[4,5],
  facts={"what":"Tiny red strawberries","how":"Raw","when":"Spring","where":"Woodland edges and meadows of far East Texas","value":"Vitamin C, sugars"},
  caution="True wild strawberry has white flowers and red fruit; the harmless 'mock strawberry' has yellow flowers and a bland fruit. Neither is dangerous, but know the difference. "+SAFE,
  sections=[{"title":"Identification","body":"A miniature of the garden berry, low to the ground with white five-petal flowers. The fruit is a fraction of the size and many times the flavor."},
    {"title":"On the trail","body":"Too small and scattered to gather in bulk, but the most intense strawberry you will ever taste, eaten on the spot."}],
  similar=["dewberry","blackberry"])

plant("carolina-buckthorn", name="Carolina Buckthorn", latin="Frangula caroliniana", family="Buckthorn",
  abundance="uncommon", type="Shrub", uses=["Fruit"], regions=["East","Central"], months=[8,9,10],
  facts={"what":"Red-ripening-to-black berries","how":"Ripe black fruit only, in moderation","when":"Late summer to fall","where":"Woodland edges and slopes","value":"Sugars"},
  caution="Eat only fully ripe BLACK fruit and only in small amounts; unripe red berries are purgative. Because buckthorns can disagree with people, this is a taste-and-wait plant. "+SAFE,
  sections=[{"title":"Identification","body":"Glossy strongly-veined leaves and berries that ripen through red to black on the same cluster. Only the black ones are for eating, sparingly."},
    {"title":"On the trail","body":"A modest sweet snack for the cautious; better known to the birds than to foragers."}],
  similar=["rusty-blackhaw","farkleberry"])

# ---- NUTS & SEEDS ----
plant("live-oak-acorn", name="Live Oak Acorn", latin="Quercus virginiana", family="Beech",
  abundance="abundant", type="Tree", uses=["Nuts","Flour"], regions=["East","Central","West"], months=[9,10,11],
  facts={"what":"Acorns, leached of tannin","how":"Ground into flour after leaching","when":"Fall","where":"The iconic spreading live oak, statewide","value":"Starch, fat, calories"},
  caution="Raw acorns are bitter and hard on the gut from tannins; they must be leached in repeated changes of water until no longer bitter before eating. "+SAFE,
  sections=[{"title":"Harvesting","body":"Live oak acorns are among the least bitter and were a Native staple. Gather sound, unwormed nuts as they drop."},
    {"title":"Leaching and flour","body":"Shell, then soak or boil in many changes of water until the bitterness is gone. Dry and grind the result into a rich, nutty flour."}],
  similar=["bur-oak-acorn","pecan"])

plant("bur-oak-acorn", name="Bur Oak Acorn", latin="Quercus macrocarpa", family="Beech",
  abundance="common", type="Tree", uses=["Nuts","Flour"], regions=["Central","East"], months=[9,10],
  facts={"what":"Very large acorns","how":"Leached, then eaten or ground to flour","when":"Fall","where":"River bottoms and prairies","value":"Starch, fat"},
  caution="Leach out the tannins in repeated water changes until no bitterness remains before eating any acorn. "+SAFE,
  sections=[{"title":"Harvesting","body":"Bur oak grows the biggest acorn of any Texas oak, capped in a shaggy fringe. Its size makes shelling and leaching far less tedious."},
    {"title":"Leaching and flour","body":"The lower-tannin acorns of white-oak-group trees like bur oak leach quickly. Grind the sweet result for baking."}],
  similar=["live-oak-acorn","hickory-nut"])

plant("hickory-nut", name="Hickory Nut", latin="Carya ovata", family="Walnut",
  abundance="common", type="Tree", uses=["Nuts"], regions=["East"], months=[9,10,11],
  facts={"what":"Nuts in a splitting husk","how":"Raw, toasted, or simmered for 'kanuchi'","when":"Fall","where":"East Texas woods and bottoms","value":"Fat, protein, minerals"},
  caution="Sweet hickories are excellent; a few relatives are bitter but not dangerous. The shells are hard, so mind your fingers. "+SAFE,
  sections=[{"title":"Harvesting","body":"Shagbark and its kin drop nuts in a four-part husk. Gather early before squirrels clear the ground."},
    {"title":"In the kitchen","body":"Pecan's richer cousin. Traditionally the whole cracked nuts were boiled and strained into a nut milk that flavored breads and hominy."}],
  similar=["pecan","black-walnut"])

plant("chinquapin", name="Chinquapin", latin="Castanea pumila", family="Beech",
  abundance="uncommon", type="Shrub", uses=["Nuts"], regions=["East"], months=[9,10],
  facts={"what":"Small sweet chestnuts","how":"Raw or roasted","when":"Fall","where":"Sandy East Texas woods","value":"Starch, some protein"},
  caution="The spiny burr bites; open it carefully. The nut itself is simply a small sweet chestnut. "+SAFE,
  sections=[{"title":"Harvesting","body":"Each spiny burr holds a single glossy brown nut. Tread the burrs open or wear gloves."},
    {"title":"In the kitchen","body":"A true chestnut in miniature, sweet enough to eat raw and lovely roasted."}],
  similar=["american-beech","hickory-nut"])

plant("pinyon-pine", name="Texas Pinyon", latin="Pinus remota", family="Pine",
  abundance="uncommon", type="Tree", uses=["Nuts","Tea"], regions=["West"], months=[9,10],
  facts={"what":"Pine nuts from the cones; needles for tea","how":"Nuts raw or roasted; needles steeped","when":"Fall for nuts","where":"West Texas hills and the Hill Country's western edge","value":"Fat, protein; vitamin C from needle tea"},
  caution="Pine nuts and needle tea from true pines are safe; simply be sure you have a pinyon and not an unrelated look-alike conifer. "+SAFE,
  sections=[{"title":"Harvesting","body":"Heat opens the cones; the small rich seeds fall out. A good pinyon year is worth the drive to West Texas."},
    {"title":"Uses","body":"The nuts are the classic pine nut of the Southwest. A handful of green needles steeped in hot water makes a piney, vitamin-C tea."}],
  similar=["loblolly-pine","live-oak-acorn"])

plant("american-beech", name="American Beech", latin="Fagus grandifolia", family="Beech",
  abundance="uncommon", type="Tree", uses=["Nuts"], regions=["East"], months=[9,10],
  facts={"what":"Small triangular nuts","how":"Raw or roasted","when":"Fall","where":"Rich woods of far East Texas","value":"Fat, protein"},
  caution="Sweet and good in moderation; very large quantities of raw beechnuts can disagree, so roast and enjoy them as a treat. "+SAFE,
  sections=[{"title":"Harvesting","body":"Smooth gray bark and coppery fall leaves mark the beech. Its little three-sided nuts hide in soft burrs."},
    {"title":"In the kitchen","body":"Fiddly to shell but genuinely delicious, best lightly roasted."}],
  similar=["chinquapin","hickory-nut"])

plant("common-sunflower", name="Common Sunflower", latin="Helianthus annuus", family="Aster",
  abundance="abundant", type="Ground", uses=["Nuts"], regions=["East","Central","West"], months=[8,9,10], flowerMonths=[6,7,8],
  facts={"what":"Seeds; unopened flower buds","how":"Seeds roasted; buds steamed like artichoke","when":"Late summer for seeds","where":"Roadsides, fields, disturbed ground everywhere","value":"Fat, protein"},
  caution="Straightforward and safe; harvest from ground away from sprayed roadsides. "+SAFE,
  sections=[{"title":"Harvesting","body":"Wild sunflowers are smaller than the crop but the seeds are the same food. Cut heads as the backs yellow and the seeds firm up; dry them before shelling."},
    {"title":"In the kitchen","body":"Roast the shelled seeds for snacking, or steam the unopened green buds and eat the base like a tiny artichoke."}],
  similar=["sunchoke","evening-primrose"])

# ---- FLOWERS, TEA & SPICE ----
plant("redbud", name="Eastern Redbud", latin="Cercis canadensis", family="Legume",
  abundance="common", type="Tree", uses=["Raw"], regions=["East","Central"], months=[3,4], flowerMonths=[3],
  facts={"what":"Pink flowers; young green pods","how":"Flowers raw in salads; young pods cooked","when":"Early spring","where":"Woodland edges and yards","value":"Vitamin C; bright and pea-like"},
  caution="Eat the flowers and only the tender young pods; skip old pods and seeds. "+SAFE,
  sections=[{"title":"Identification","body":"In March the bare branches erupt in magenta-pink flowers right off the wood. Unmistakable and cheerful."},
    {"title":"In the kitchen","body":"The tangy-sweet flowers brighten a salad or top a cake; young pods can be sautéed like snow peas."}],
  similar=["black-locust","mimosa"])

plant("black-locust", name="Black Locust", latin="Robinia pseudoacacia", family="Legume",
  abundance="common", type="Tree", uses=["Raw","Cooked"], regions=["East","Central"], months=[4,5], flowerMonths=[4,5],
  facts={"what":"Fragrant white flowers ONLY","how":"Flowers raw or as fritters","when":"Late spring","where":"Roadsides, old fields, woods edges","value":"Nectar-sweet; a fleeting spring treat"},
  caution="Eat ONLY the white flowers. The bark, leaves, seeds, and pods of black locust are toxic. Be sure of the tree and use the blossoms only. "+SAFE,
  sections=[{"title":"Identification","body":"Drooping clusters of sweet-pea-shaped white flowers scent whole roadsides for a week or two in spring. Every other part of the tree is off the menu."},
    {"title":"In the kitchen","body":"The blossoms are honey-sweet raw and classic dipped in batter and fried into fritters."}],
  similar=["redbud","mimosa"])

plant("mimosa", name="Mimosa", latin="Albizia julibrissin", family="Legume",
  abundance="common", type="Tree", uses=["Raw","Tea"], regions=["East","Central"], months=[5,6], flowerMonths=[5,6],
  facts={"what":"Pink powder-puff flowers","how":"Flowers raw as garnish or steeped as tea","when":"Early summer","where":"Yards, roadsides, disturbed ground","value":"Delicate and floral"},
  caution="Use the flowers; skip the pods and seeds. An introduced tree, so gather away from sprayed areas. "+SAFE,
  sections=[{"title":"Identification","body":"Feathery leaves and silky pink 'powder-puff' flowers make this introduced tree easy to know."},
    {"title":"Uses","body":"The sweet flowers garnish salads and desserts, and both flowers and bark have a long history in traditional calming teas."}],
  similar=["redbud","black-locust"])

plant("honey-locust", name="Honey Locust", latin="Gleditsia triacanthos", family="Legume",
  abundance="common", type="Tree", uses=["Flour"], regions=["East","Central"], months=[9,10,11],
  facts={"what":"Sweet pulp inside long pods","how":"Pulp eaten raw or dried and ground","when":"Fall","where":"River bottoms and fence rows","value":"Sugars"},
  caution="Eat the sweet pulp, not the hard seeds. Do not confuse with the toxic black locust: honey locust has long twisted pods with sweet pulp and fierce branched thorns. "+SAFE,
  sections=[{"title":"Identification","body":"Foot-long twisting brown pods and, on wild trees, alarming branched thorns. Inside the pods is a sticky sweet pulp."},
    {"title":"In the kitchen","body":"The honey-sweet pulp can be scraped and eaten or dried and ground into a sweetener, much like mesquite."}],
  similar=["honey-mesquite","kudzu"])

plant("eastern-redcedar", name="Eastern Redcedar", latin="Juniperus virginiana", family="Cypress",
  abundance="abundant", type="Tree", uses=["Spice"], regions=["East","Central"], months=[10,11,12],
  facts={"what":"Blue 'berries' (cones)","how":"A few dried and crushed as a juniper spice","when":"Fall and winter","where":"Old fields and fence rows across the eastern half","value":"Aromatic; used sparingly as seasoning"},
  caution="Use only a few berries as a SEASONING, never as a food or in medicinal quantity; concentrated juniper is hard on the kidneys and unsafe in pregnancy. "+SAFE,
  sections=[{"title":"Identification","body":"A dense evergreen with scaly foliage and waxy blue berries. Crush one: it smells of gin, because juniper is what makes gin."},
    {"title":"Uses","body":"A pinch of crushed dried berries seasons game and stews. This is a spice, not a snack."}],
  similar=["ashe-juniper","redberry-juniper"])

plant("ashe-juniper", name="Ashe Juniper", latin="Juniperus ashei", family="Cypress",
  abundance="abundant", type="Tree", uses=["Spice"], regions=["Central","West"], months=[11,12,1],
  facts={"what":"Blue berries (cones)","how":"A few as a juniper spice","when":"Winter","where":"Hill Country slopes, the 'cedar' of Central Texas","value":"Aromatic seasoning"},
  caution="Seasoning only, and just a few berries; concentrated juniper is unsafe in quantity and in pregnancy. "+SAFE,
  sections=[{"title":"Identification","body":"The shaggy-barked 'mountain cedar' that famously fills Central Texas air with pollen. Its blue berries are the useful part."},
    {"title":"Uses","body":"Use a crushed berry or two to lend a resinous, gin-like note to hearty dishes."}],
  similar=["eastern-redcedar","redberry-juniper"])

plant("redberry-juniper", name="Redberry Juniper", latin="Juniperus pinchotii", family="Cypress",
  abundance="common", type="Tree", uses=["Spice"], regions=["West"], months=[9,10,11],
  facts={"what":"Reddish berries (cones)","how":"A few as seasoning","when":"Fall","where":"West Texas rangeland","value":"Aromatic seasoning"},
  caution="A seasoning in tiny amounts only; not a food, and unsafe in quantity. "+SAFE,
  sections=[{"title":"Identification","body":"Unlike its blue-fruited cousins, this West Texas juniper carries coppery-red berries."},
    {"title":"Uses","body":"Same rule as any juniper: a pinch of crushed berry for aroma, nothing more."}],
  similar=["ashe-juniper","eastern-redcedar"])

plant("beebalm", name="Lemon Beebalm", latin="Monarda citriodora", family="Mint",
  abundance="common", type="Ground", uses=["Tea","Spice"], regions=["Central","East","West"], months=[5,6,7], flowerMonths=[5,6],
  facts={"what":"Leaves and flowers","how":"Fresh or dried as tea and seasoning","when":"Late spring into summer","where":"Prairies, roadsides, open fields","value":"Aromatic; oregano-thyme notes"},
  caution="A well-known safe mint-family herb; simply confirm the square stem and minty aroma. "+SAFE,
  sections=[{"title":"Identification","body":"Whorls of pink-lavender flowers stack up the square stem, and the crushed leaves smell of citrus, oregano, and thyme."},
    {"title":"Uses","body":"A bright herbal tea and a fine wild seasoning for beans and meat; the flowers are edible too."}],
  similar=["mexican-mint-marigold","frostweed"])

plant("american-basswood", name="American Basswood", latin="Tilia americana", family="Mallow",
  abundance="uncommon", type="Tree", uses=["Tea","Raw"], regions=["East"], months=[5,6], flowerMonths=[5,6],
  facts={"what":"Flowers for tea; tender young leaves","how":"Flowers steeped; young leaves raw in salad","when":"Late spring","where":"Rich East Texas woods","value":"Mild and sweet; a calming tea"},
  caution="Use fresh flowers for tea, not old browning ones. Young leaves are a mild salad green. "+SAFE,
  sections=[{"title":"Identification","body":"Big heart-shaped leaves and fragrant pale flowers that hang from a strap-like bract. Also called linden."},
    {"title":"Uses","body":"Linden flower tea is a classic soothing brew, honey-sweet and floral; the tender spring leaves make a pleasant salad."}],
  similar=["redbud","violet"])

plant("mexican-mint-marigold", name="Mexican Mint Marigold", latin="Tagetes lucida", family="Aster",
  abundance="uncommon", type="Ground", uses=["Tea","Spice"], regions=["Central","South" if False else "West"], months=[9,10,11], flowerMonths=[10],
  facts={"what":"Anise-scented leaves; yellow flowers","how":"Fresh or dried as a tarragon substitute and tea","when":"Fall bloom","where":"Gardens and naturalized in Central/South Texas","value":"Aromatic; sweet anise flavor"},
  caution="A well-known culinary herb; confirm the sweet anise scent. "+SAFE,
  sections=[{"title":"Identification","body":"Narrow glossy leaves that smell strongly of anise, topped by small golden marigold flowers in fall."},
    {"title":"Uses","body":"Texas cooks use it as 'Texas tarragon,' and its leaves make a sweet, licorice-like tea."}],
  similar=["beebalm","frostweed"])

plant("frostweed", name="Frostweed", latin="Verbesina virginica", family="Aster",
  abundance="common", type="Ground", uses=["Tea"], regions=["East","Central"], months=[9,10], flowerMonths=[9,10],
  facts={"what":"Leaves for a mild tea","how":"Dried leaves steeped","when":"Fall","where":"Shady woodland edges","value":"A gentle herbal tea"},
  caution="Used as a mild folk tea; a bitter herb best taken occasionally rather than in quantity. "+SAFE,
  sections=[{"title":"Identification","body":"Tall winged stems and white fall flowers; on the first hard freeze the stems split and extrude curls of ice, the 'frost' that names it."},
    {"title":"Uses","body":"The dried leaves make a mild traditional tea; the plant is grown as much for its ribbon-ice spectacle and its butterflies."}],
  similar=["beebalm","mexican-mint-marigold"])

plant("wax-myrtle", name="Wax Myrtle", latin="Morella cerifera", family="Bayberry",
  abundance="common", type="Shrub", uses=["Spice"], regions=["East"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"Aromatic leaves; waxy berries","how":"Leaves as a bay-leaf substitute","when":"Leaves year-round","where":"Wet East Texas woods and coast","value":"Aromatic seasoning"},
  caution="Use the leaves like bay: to flavor a pot, then removed before eating, not chewed. "+SAFE,
  sections=[{"title":"Identification","body":"An evergreen shrub whose crushed leaves smell resinous and clean; the pale berries are coated in fragrant wax once used for candles."},
    {"title":"Uses","body":"A leaf or two flavors soups and stews just like a bay leaf. Fish it out before serving."}],
  similar=["eastern-redcedar","yaupon-holly"])

plant("loblolly-pine", name="Loblolly Pine", latin="Pinus taeda", family="Pine",
  abundance="abundant", type="Tree", uses=["Tea"], regions=["East"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"Green needles for tea; inner bark in survival use","how":"Needles chopped and steeped","when":"Year-round","where":"The dominant pine of East Texas","value":"Vitamin C"},
  caution="True-pine needle tea is safe and vitamin-rich, but pregnant women should avoid pine needle tea, and never use yew or other toxic evergreens: confirm a true pine. "+SAFE,
  sections=[{"title":"Identification","body":"Long needles in bundles of three and big scaly cones. The workhorse pine of the East Texas timber belt."},
    {"title":"Uses","body":"A handful of chopped green needles steeped (not boiled) makes a piney, citrusy tea high in vitamin C."}],
  similar=["pinyon-pine","wax-myrtle"])

plant("kudzu", name="Kudzu", latin="Pueraria montana", family="Legume",
  abundance="common", type="Vine", uses=["Raw","Tea"], regions=["East"], months=[7,8,9], flowerMonths=[8],
  facts={"what":"Grape-scented purple flowers; young leaves; starchy root","how":"Flowers into jelly and tea; young leaves cooked","when":"Late summer flowers","where":"Smothering East Texas roadsides and woods edges","value":"The flowers are fragrant and edible"},
  caution="A safe and famously invasive plant to harvest freely; just gather away from roadside spray. "+SAFE,
  sections=[{"title":"Identification","body":"The vine that ate the South, blanketing everything it climbs. In late summer it hangs clusters of purple flowers that smell of grape soda."},
    {"title":"Uses","body":"The flowers make a startling purple jelly and a fragrant tea; young leaves cook like any green, and the root is a traditional starch."}],
  similar=["greenbrier","muscadine"])

# ---- CACTI & SUCCULENTS ----
plant("strawberry-pitaya", name="Strawberry Pitaya", latin="Echinocereus enneacanthus", family="Cactus",
  abundance="common", type="Cactus", uses=["Fruit"], regions=["West"], months=[6,7],
  facts={"what":"Red fruit tasting of strawberry","how":"Raw, once the spines are removed","when":"Early summer","where":"West Texas desert and brushland","value":"Sugars, vitamin C"},
  caution="Singe or scrub off the spines before handling, exactly as with prickly pear. "+SAFE,
  sections=[{"title":"Identification","body":"A clumping hedgehog cactus whose fruit genuinely tastes of strawberry, one of the best wild fruits of the desert."},
    {"title":"Harvesting","body":"De-spine the fruit with a flame or a stiff brush, then peel. Sweet enough to eat by the handful."}],
  similar=["prickly-pear","tasajillo"])

plant("tasajillo", name="Tasajillo", latin="Cylindropuntia leptocaulis", family="Cactus",
  abundance="common", type="Cactus", uses=["Fruit"], regions=["West","Central"], months=[10,11,12,1],
  facts={"what":"Small red fruit","how":"Raw, de-spined","when":"Fall into winter","where":"Brush country and dry ground","value":"Sugars"},
  caution="This 'Christmas cactus' has vicious, easily-detached spines; de-spine carefully before eating. "+SAFE,
  sections=[{"title":"Identification","body":"A thin, pencil-jointed cholla that lights up with bright red fruit around the holidays, giving it its nickname."},
    {"title":"Harvesting","body":"The fruit is small but persistent through winter. Burn or scrape off every spine before eating."}],
  similar=["prickly-pear","cholla-buds"])

plant("sotol", name="Sotol", latin="Dasylirion texanum", family="Asparagus",
  abundance="common", type="Cactus", uses=["Cooked"], regions=["West"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"The starchy heart, slow-roasted","how":"Pit-roasted, the traditional way","when":"Year-round","where":"West Texas hills and Big Bend country","value":"Starch, sugars"},
  caution="Only the cooked heart is food, and preparing it is a serious pit-roasting project, not a trail snack. The leaves are saw-toothed. "+SAFE,
  sections=[{"title":"Identification","body":"A rosette of slender saw-edged leaves sending up a tall flower stalk, also called desert spoon. A signature plant of the Trans-Pecos."},
    {"title":"Uses","body":"Indigenous peoples pit-roasted the hearts for days into a sweet food, and the same plant is distilled into the spirit sotol."}],
  similar=["agave","yucca"])

plant("agave", name="Agave", latin="Agave americana", family="Asparagus",
  abundance="common", type="Cactus", uses=["Cooked"], regions=["West","Central"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"The heart and flower stalk, cooked","how":"Slow pit-roasted; stalk roasted","when":"Year-round; stalk before it blooms","where":"Rocky West and Central Texas","value":"Starch, sugars"},
  caution="Raw agave is caustic and full of irritating crystals: it is edible ONLY after long cooking. The sap can burn skin. This is a traditional pit-roast food, not something to eat raw. "+SAFE,
  sections=[{"title":"Identification","body":"A giant rosette of thick spine-tipped leaves that sends up a towering flower mast once in its life. Also called the century plant."},
    {"title":"Uses","body":"Pit-roasting for a day or more turns the fibrous heart sweet and molasses-dark; the roasted flower stalk is food too. The plant is the source of agave syrup and, elsewhere, tequila and mezcal."}],
  similar=["sotol","yucca"])

plant("cholla-buds", name="Cholla Buds", latin="Cylindropuntia imbricata", family="Cactus",
  abundance="common", type="Cactus", uses=["Cooked"], regions=["West"], months=[4,5],
  facts={"what":"Unopened flower buds","how":"De-spined and cooked","when":"Spring","where":"West Texas grassland and desert","value":"Calcium, fiber"},
  caution="De-spine the buds thoroughly (roll and singe) before cooking; never eat them raw or spined. "+SAFE,
  sections=[{"title":"Identification","body":"The cane cholla's spiny joints carry fat flower buds in spring. It is the buds, not the fruit, that are the traditional food."},
    {"title":"Uses","body":"Roll the buds to knock off spines, then boil or roast. A Southwestern staple, tangy and rich in calcium."}],
  similar=["tasajillo","prickly-pear"])

plant("yucca", name="Yucca", latin="Yucca", family="Asparagus",
  abundance="abundant", type="Cactus", uses=["Cooked","Raw"], regions=["West","Central"], months=[4,5,6],
  facts={"what":"Flower petals and flower stalk; fruit of some species","how":"Petals raw or cooked; stalk roasted young","when":"Spring bloom","where":"Dry ground statewide","value":"Modest calories; the petals are the easy food"},
  caution="Eat the petals (remove the bitter green centers) and only the young stalk before it hardens. Roots are not food. Confirm you have a yucca, not a look-alike agave. "+SAFE,
  sections=[{"title":"Identification","body":"A rosette of stiff sword-leaves sending up a tall spike of creamy bell flowers. Unlike agave, the leaves are not toothed along the edge."},
    {"title":"Uses","body":"The crunchy petals go raw into salads or blanched into dishes; the tender young flower stalk can be roasted like a vegetable."}],
  similar=["agave","sotol"])

# ---- GREENS & WEEDS ----
plant("sow-thistle", name="Sow Thistle", latin="Sonchus oleraceus", family="Aster",
  abundance="abundant", type="Ground", uses=["Raw","Cooked"], regions=["East","Central","West"], months=[2,3,4,11,12],
  facts={"what":"Young leaves","how":"Raw when young, cooked when older","when":"Cool months","where":"Gardens, lots, roadsides","value":"A mild dandelion-like green"},
  caution="Soft spineless leaves and milky sap; a harmless dandelion relative. Harvest away from sprayed ground. "+SAFE,
  sections=[{"title":"Identification","body":"Looks thistly but the soft edges don't bite. Break a stem and it bleeds white, like its cousin the dandelion."},
    {"title":"In the kitchen","body":"Young leaves are mild and juicy in salad; older ones lose their slight bitterness with a quick cooking."}],
  similar=["dandelion","wild-lettuce"])

plant("wild-lettuce", name="Wild Lettuce", latin="Lactuca canadensis", family="Aster",
  abundance="common", type="Ground", uses=["Cooked","Raw"], regions=["East","Central"], months=[3,4,5],
  facts={"what":"Young basal leaves","how":"Young raw, older cooked","when":"Spring","where":"Fields, roadsides, disturbed ground","value":"A bitter spring green"},
  caution="Eat the young leaves; older plants turn very bitter. A safe wild ancestor of garden lettuce. "+SAFE,
  sections=[{"title":"Identification","body":"A tall lettuce with milky sap and leaves that clasp the stem, often with a row of prickles down the midrib underneath."},
    {"title":"In the kitchen","body":"Young rosette leaves eat like a sharp lettuce; cook the bitterness out of older ones as you would dandelion."}],
  similar=["sow-thistle","dandelion"])

plant("curly-dock", name="Curly Dock", latin="Rumex crispus", family="Buckwheat",
  abundance="abundant", type="Ground", uses=["Cooked"], regions=["East","Central","West"], months=[2,3,4],
  facts={"what":"Young leaves; seeds for flour","how":"Leaves cooked like spinach; seeds ground","when":"Cool season for leaves","where":"Fields, ditches, disturbed ground","value":"Vitamins A and C; iron"},
  caution="Like spinach it is high in oxalates, so cook the leaves and eat in moderation, not by the bowlful. "+SAFE,
  sections=[{"title":"Identification","body":"A rosette of long wavy-edged leaves that sends up a stalk of rusty-brown seeds standing through winter, a roadside landmark."},
    {"title":"In the kitchen","body":"Young leaves cook down tart and lemony; the abundant seeds can be rubbed free and ground into a buckwheat-like flour."}],
  similar=["sheep-sorrel","lambs-quarters"])

plant("sheep-sorrel", name="Sheep Sorrel", latin="Rumex acetosella", family="Buckwheat",
  abundance="common", type="Ground", uses=["Raw"], regions=["East","Central"], months=[3,4,5],
  facts={"what":"Arrow-shaped leaves","how":"Raw as a lemony garnish","when":"Spring","where":"Acid soils, lawns, fields","value":"Vitamin C; sharp and sour"},
  caution="The lemon tang is oxalic acid: a fine garnish and nibble, not a whole salad, and best skipped by those prone to kidney stones. "+SAFE,
  sections=[{"title":"Identification","body":"Small arrowhead leaves with backward-pointing lobes, low in lawns and poor soils. Pleasantly sour when you chew one."},
    {"title":"On the trail","body":"A bright wild lemon: scatter a few leaves over fish or into a salad for a jolt of sourness."}],
  similar=["wood-sorrel","curly-dock"])

plant("amaranth", name="Amaranth", latin="Amaranthus retroflexus", family="Amaranth",
  abundance="abundant", type="Ground", uses=["Cooked","Flour"], regions=["East","Central","West"], months=[5,6,7,8], flowerMonths=[7,8],
  facts={"what":"Young leaves; seeds","how":"Leaves cooked like spinach; seeds as grain","when":"Warm months for greens","where":"Gardens, fields, disturbed rich soil","value":"Protein, vitamins A and C, calcium; seeds are a grain"},
  caution="A safe and nutritious green. Harvest from unsprayed ground, and as with spinach, don't rely on it as your only green day after day. "+SAFE,
  sections=[{"title":"Identification","body":"Also called pigweed: upright, red-rooted, with dense green flower spikes. One of the world's oldest cultivated greens and grains hiding in the garden as a weed."},
    {"title":"In the kitchen","body":"Young leaves cook down like a mild spinach; the tiny seeds thresh out by the thousands and cook into a nutty porridge or grind to flour."}],
  similar=["lambs-quarters","purslane"])

plant("pokeweed", name="Pokeweed", latin="Phytolacca americana", family="Pokeweed",
  abundance="common", type="Ground", uses=["Cooked"], regions=["East","Central"], months=[3,4],
  facts={"what":"Only the youngest spring shoots, thoroughly cooked","how":"Boiled in several changes of water ('poke sallet')","when":"Early spring only","where":"Fence rows, clearings, disturbed ground","value":"A traditional Southern spring green"},
  caution="POISONOUS raw. Only the young green shoots under about 6 inches are used, and only after boiling in at least two or three changes of water. The roots, berries, seeds, and mature purple stalks are toxic and can be fatal. If you are not fully confident, do not attempt this plant. "+SAFE,
  sections=[{"title":"Identification","body":"A big perennial that dies back yearly. In spring it sends up tender green shoots; by summer it is a rank plant with magenta stems and dark berries, all of it then toxic."},
    {"title":"The traditional preparation","body":"'Poke sallet' is an old Southern dish made by boiling the young shoots in several changes of water, discarding each. This detoxifies them, and it is the only safe way they are eaten. Never eat the berries or root."}],
  similar=["amaranth","curly-dock"])

plant("cleavers", name="Cleavers", latin="Galium aparine", family="Madder",
  abundance="common", type="Ground", uses=["Cooked","Tea"], regions=["East","Central"], months=[2,3,4],
  facts={"what":"Young tender growth","how":"Cooked as a potherb; dried as tea","when":"Cool season","where":"Shady moist ground, fence rows","value":"A mild spring green"},
  caution="The clinging hairs soften with cooking; eat it cooked rather than raw. A safe, well-known plant. "+SAFE,
  sections=[{"title":"Identification","body":"A sprawling square-stemmed plant with whorls of narrow leaves and tiny hooks that make it cling to clothing, giving it the nickname 'sticky willy.'"},
    {"title":"Uses","body":"Young growth cooks down into a mild green; the dried plant makes a traditional tea, and the seeds have been roasted as a coffee substitute."}],
  similar=["chickweed","plantain"])

plant("plantain", name="Broadleaf Plantain", latin="Plantago major", family="Plantain",
  abundance="abundant", type="Ground", uses=["Cooked","Raw"], regions=["East","Central","West"], months=[3,4,5,6,7,8,9],
  facts={"what":"Young leaves; seeds","how":"Young leaves raw or cooked; seeds as a psyllium-like fiber","when":"Most of the growing season","where":"Lawns, paths, compacted ground everywhere","value":"Vitamins A, C, K; the seed is a fiber source"},
  caution="A safe, mild, extremely common plant. Take young leaves, and harvest away from sprayed lawns. "+SAFE,
  sections=[{"title":"Identification","body":"A flat rosette of oval leaves with strong parallel veins that string like celery when you tear one, and a slim seed spike up the middle. Not the banana."},
    {"title":"Uses","body":"The youngest leaves are a mild salad green; older ones cook down. The seed is the same family as store-bought psyllium fiber, and the crushed leaf is a famous field poultice for stings."}],
  similar=["dandelion","cleavers"])

plant("peppergrass", name="Peppergrass", latin="Lepidium virginicum", family="Mustard",
  abundance="abundant", type="Ground", uses=["Raw","Spice"], regions=["East","Central","West"], months=[3,4,5,6],
  facts={"what":"Leaves and green seed pods","how":"Raw as a peppery green and seasoning","when":"Spring into summer","where":"Roadsides, fields, disturbed ground","value":"Vitamin C; a free pepper-cress"},
  caution="A safe mustard-family plant; confirm the peppery taste and the tiny round flat pods. "+SAFE,
  sections=[{"title":"Identification","body":"A wiry weed hung with hundreds of tiny round flat green pods up the stem. Chew a leaf or pod: sharp black pepper and cress."},
    {"title":"Uses","body":"The green pods are a wild pepper and caper both; scatter the leaves and pods into salads for free heat."}],
  similar=["shepherds-purse","wild-mustard"])

plant("shepherds-purse", name="Shepherd's Purse", latin="Capsella bursa-pastoris", family="Mustard",
  abundance="common", type="Ground", uses=["Raw","Cooked"], regions=["East","Central"], months=[2,3,4],
  facts={"what":"Young rosette leaves; heart-shaped pods","how":"Young leaves raw or cooked","when":"Cool season","where":"Gardens, lots, roadsides","value":"A peppery mustard green"},
  caution="A safe common mustard; eat the young leaves before the plant turns tough and bitter. "+SAFE,
  sections=[{"title":"Identification","body":"Named for its distinctive little heart- or purse-shaped seed pods marching up the stem. The basal leaves resemble a small dandelion."},
    {"title":"In the kitchen","body":"Young leaves are a peppery green raw or lightly cooked; the plant is a prized potherb across the world."}],
  similar=["peppergrass","bittercress"])

plant("wild-mustard", name="Wild Mustard", latin="Sinapis arvensis", family="Mustard",
  abundance="common", type="Ground", uses=["Cooked","Spice"], regions=["East","Central"], months=[2,3,4], flowerMonths=[3,4],
  facts={"what":"Young leaves; flowers; seeds","how":"Leaves cooked; flowers raw; seeds as mustard","when":"Cool season","where":"Fields and roadsides, often in yellow sheets","value":"Vitamins A and C; the seeds make mustard"},
  caution="A safe mustard-family plant; harvest young leaves away from sprayed fields. "+SAFE,
  sections=[{"title":"Identification","body":"Fields of four-petaled yellow flowers in early spring; every mustard has flowers in a cross of four petals and a peppery bite."},
    {"title":"In the kitchen","body":"Young leaves cook into mustard greens; the bright flowers dress a salad, and the ground seeds are literally mustard."}],
  similar=["peppergrass","shepherds-purse"])

plant("bittercress", name="Hairy Bittercress", latin="Cardamine hirsuta", family="Mustard",
  abundance="common", type="Ground", uses=["Raw"], regions=["East","Central"], months=[1,2,3],
  facts={"what":"Whole young rosette","how":"Raw as a cress","when":"Cool season","where":"Gardens, pots, moist lots","value":"Vitamin C; a peppery cress"},
  caution="A safe, mild mustard; harvest from unsprayed ground. "+SAFE,
  sections=[{"title":"Identification","body":"A small rosette of round-lobed leaflets that fires its ripe seed pods at a touch. One of the first fresh things in a winter garden."},
    {"title":"On the trail","body":"Snip the whole young rosette for a fresh peppery cress; it fades fast once it flowers."}],
  similar=["watercress","shepherds-purse"])

plant("watercress", name="Watercress", latin="Nasturtium officinale", family="Mustard",
  abundance="uncommon", type="Aquatic", uses=["Raw"], regions=["Central","East"], months=[1,2,3,4,10,11,12],
  facts={"what":"Leaves and stems","how":"Raw as the classic peppery salad green","when":"Cool months","where":"Clean, cold, flowing spring water","value":"Vitamins A, C, K; iron"},
  caution="Harvest ONLY from clean, flowing water you know is unpolluted; cress from water near livestock or runoff can carry parasites. When in doubt, cook it. "+SAFE,
  sections=[{"title":"Identification","body":"Rounded compound leaves floating and trailing in cold spring runs, with a sharp peppery bite. Grows right in the water."},
    {"title":"In the kitchen","body":"The original salad cress, brilliant raw. Because it grows in water, source is everything: only clean flowing springs."}],
  similar=["bittercress","peppergrass"])

plant("spiderwort", name="Spiderwort", latin="Tradescantia ohiensis", family="Spiderwort",
  abundance="common", type="Ground", uses=["Raw","Cooked"], regions=["East","Central"], months=[3,4,5,6], flowerMonths=[4,5],
  facts={"what":"Leaves, stems, and flowers","how":"Leaves and stems raw or cooked; flowers as garnish","when":"Spring","where":"Prairies, roadsides, woodland edges","value":"A mild mucilaginous green"},
  caution="A safe, well-known edible; the blue flowers and grass-like leaves are distinctive. "+SAFE,
  sections=[{"title":"Identification","body":"Grassy arching leaves and three-petaled blue-violet flowers that each last a single morning. Break a leaf and it draws a fine mucilage thread."},
    {"title":"In the kitchen","body":"Young leaves and stems eat like a slightly slick green vegetable, raw or cooked; the flowers pretty up a plate."}],
  similar=["dayflower","violet"])

plant("dayflower", name="Dayflower", latin="Commelina erecta", family="Spiderwort",
  abundance="common", type="Ground", uses=["Raw","Cooked"], regions=["East","Central","West"], months=[5,6,7,8], flowerMonths=[6,7],
  facts={"what":"Young leaves, stems, and flowers","how":"Raw or cooked as a mild green","when":"Summer","where":"Fields, yards, disturbed ground","value":"A mild green; the flowers are a garnish"},
  caution="A safe relative of spiderwort; eat young tender growth. "+SAFE,
  sections=[{"title":"Identification","body":"Two vivid blue upper petals over a small white lower one give each flower a Mickey-Mouse look; each bloom lasts just a day."},
    {"title":"In the kitchen","body":"The tender shoots and leaves are a pleasant mild green, and the blue flowers brighten a salad."}],
  similar=["spiderwort","purslane"])

plant("white-clover", name="White Clover", latin="Trifolium repens", family="Legume",
  abundance="abundant", type="Ground", uses=["Raw","Tea"], regions=["East","Central","West"], months=[3,4,5,6], flowerMonths=[4,5,6],
  facts={"what":"Flowers and young leaves","how":"Flowers raw or as tea; leaves cooked","when":"Spring into summer","where":"Lawns, fields, roadsides everywhere","value":"A mild sweet nibble"},
  caution="Eat clover in modest amounts and best cooked or dried for tea, since large quantities of raw clover can cause bloating. Harvest from unsprayed lawns. "+SAFE,
  sections=[{"title":"Identification","body":"The familiar three-leaflet lawn clover with round white flower heads. Truly abundant and easy to know."},
    {"title":"Uses","body":"The sweet flower heads make a pleasant nibble and a mild tea; young leaves are best lightly cooked."}],
  similar=["violet","common-mallow"])

plant("common-mallow", name="Common Mallow", latin="Malva neglecta", family="Mallow",
  abundance="common", type="Ground", uses=["Raw","Cooked"], regions=["East","Central"], months=[3,4,5,6,9,10],
  facts={"what":"Leaves and the round green seed 'cheeses'","how":"Leaves raw or cooked; the mucilage thickens soups","when":"Cool halves of the year","where":"Gardens, lots, sidewalk edges","value":"Vitamins A and C; a natural thickener"},
  caution="A safe, mild, very common plant; harvest away from sprayed ground. "+SAFE,
  sections=[{"title":"Identification","body":"Round scalloped leaves and small pale flowers, with flat button-like green fruits kids have long called 'cheeses.' A wild cousin of okra and hibiscus."},
    {"title":"In the kitchen","body":"Mild leaves for salad or pot, and a mucilage that thickens soups like okra. The green 'cheeses' are a fun raw nibble."}],
  similar=["white-clover","plantain"])

plant("violet", name="Common Blue Violet", latin="Viola sororia", family="Violet",
  abundance="common", type="Ground", uses=["Raw"], regions=["East","Central"], months=[2,3,4], flowerMonths=[2,3,4],
  facts={"what":"Flowers and young leaves","how":"Raw in salads; flowers candied or as syrup","when":"Early spring","where":"Shady lawns, woods edges","value":"Vitamins A and C"},
  caution="Eat the leaves and FLOWERS of true violets only. Skip the roots and seeds, and never confuse with unrelated yellow-flowered plants sometimes called violets. "+SAFE,
  sections=[{"title":"Identification","body":"Heart-shaped leaves and five-petaled blue-purple flowers low in the spring lawn. A gentle, cheerful edible."},
    {"title":"Uses","body":"Toss leaves and flowers into salads, candy the blooms for cakes, or steep them into a jewel-colored violet syrup."}],
  similar=["white-clover","spiderwort"])

plant("greenbrier", name="Greenbrier", latin="Smilax bona-nox", family="Greenbrier",
  abundance="abundant", type="Vine", uses=["Raw","Cooked"], regions=["East","Central"], months=[3,4,5],
  facts={"what":"Tender growing shoot tips and tendrils","how":"Raw like a bean, or cooked as an asparagus","when":"Spring flush","where":"Woods, thickets, fence rows, often a thorny tangle","value":"A crisp spring vegetable"},
  caution="Only the soft new shoot tips are food; the mature thorny vine is not. A safe, well-known trailside vegetable. "+SAFE,
  sections=[{"title":"Identification","body":"A thorny climbing vine that most people meet by snagging a shirt on it. Follow it to the soft, often reddish new growth at the tips."},
    {"title":"In the kitchen","body":"Snap the tender tips off like green beans; they are crisp and mild raw and cook up like asparagus."}],
  similar=["kudzu","muscadine"])

plant("field-garlic", name="Field Garlic", latin="Allium vineale", family="Amaryllis",
  abundance="abundant", type="Ground", uses=["Raw","Cooked"], regions=["East","Central"], months=[1,2,3,4,11,12],
  facts={"what":"Hollow leaves and small bulbs","how":"Anywhere chives or garlic belong","when":"Cool months","where":"Lawns, fields, roadsides","value":"Onion-family flavor"},
  caution="THE ONION RULE HAS NO EXCEPTIONS: if it does not smell strongly of onion or garlic, do not eat it. Toxic look-alikes grow in the same lawns but have no smell. "+SAFE,
  sections=[{"title":"Identification","body":"Round hollow grass-like leaves in a clump, and the giveaway: crush one and the whole plant must reek of garlic. No smell, no eating."},
    {"title":"In the kitchen","body":"The green tops are wild chives and the little bulbs are a sharp garlic; both go into anything savory."}],
  similar=["canada-wild-onion","peppergrass"])

plant("evening-primrose", name="Evening Primrose", latin="Oenothera biennis", family="Evening primrose",
  abundance="common", type="Ground", uses=["Cooked","Raw"], regions=["East","Central","West"], months=[3,4,10,11], flowerMonths=[5,6],
  facts={"what":"First-year root; young leaves; flowers","how":"Root cooked; young leaves cooked; flowers raw","when":"Cool seasons for root and leaves","where":"Fields, roadsides, disturbed ground","value":"Starchy root; a mild green"},
  caution="Eat the first-year root cooked and the young leaves cooked; both are peppery and best not eaten in quantity raw. "+SAFE,
  sections=[{"title":"Identification","body":"A first-year rosette becomes a tall stalk of yellow flowers that open at dusk. The useful root is the fleshy taproot of the first-year plant."},
    {"title":"In the kitchen","body":"The cooked root is peppery and a little nutty, a wild parsnip of sorts; the young leaves cook down and the flowers garnish a plate."}],
  similar=["common-sunflower","dandelion"])

plant("sunchoke", name="Sunchoke", latin="Helianthus tuberosus", family="Aster",
  abundance="uncommon", type="Ground", uses=["Cooked","Raw"], regions=["East","Central"], months=[10,11,12,1], flowerMonths=[9],
  facts={"what":"Knobby underground tubers","how":"Raw, roasted, or boiled like a potato","when":"After the tops die, fall into winter","where":"Moist ground, old fields, roadsides","value":"Inulin, iron, potassium"},
  caution="A safe, choice wild vegetable. Its inulin can cause gas for some people, so start small. "+SAFE,
  sections=[{"title":"Identification","body":"A tall wild sunflower whose real prize is underground: clusters of knobby tubers you dig after the plant dies back. Also called Jerusalem artichoke, though it is neither."},
    {"title":"In the kitchen","body":"Sweet and nutty, crisp raw and creamy roasted, a genuinely excellent vegetable that once rivaled the potato."}],
  similar=["common-sunflower","arrowhead"])

# ---- AQUATIC ----
plant("american-lotus", name="American Lotus", latin="Nelumbo lutea", family="Lotus",
  abundance="uncommon", type="Aquatic", uses=["Cooked","Nuts"], regions=["East"], months=[7,8,9],
  facts={"what":"Seeds; young leaves; tubers","how":"Seeds raw or roasted; tubers and young leaves cooked","when":"Late summer for seeds","where":"Still lakes, oxbows, slow water of East Texas","value":"Starch, protein from the seeds"},
  caution="Harvest only from clean water, and be certain of the plant. A safe and choice water plant when the water is clean. "+SAFE,
  sections=[{"title":"Identification","body":"Huge round leaves standing above the water and pale yellow flowers, followed by the famous shower-head seed pod. The only lotus native to the region."},
    {"title":"In the kitchen","body":"The green seeds are a fresh nutty snack and the ripe ones roast like nuts; the starchy tubers cook like a potato and the unfurling young leaves are a cooked green."}],
  similar=["cattail","arrowhead"])

plant("arrowhead", name="Arrowhead", latin="Sagittaria latifolia", family="Water plantain",
  abundance="uncommon", type="Aquatic", uses=["Cooked"], regions=["East","Central"], months=[10,11,12],
  facts={"what":"Starchy tubers ('duck potato')","how":"Boiled or roasted like a potato","when":"Fall into winter","where":"Marsh edges, pond margins, slow water","value":"Starch"},
  caution="Cook the tubers; they are unpleasant raw. Harvest only from clean water, and confirm the arrowhead-shaped leaves. "+SAFE,
  sections=[{"title":"Identification","body":"Bold arrowhead-shaped leaves standing at the water's edge with three-petaled white flowers. The tubers sit in the mud below, hence 'duck potato.'"},
    {"title":"In the kitchen","body":"Dislodge the tubers with your feet and let them float up. Cooked, they eat like a nutty potato and were a major Indigenous starch."}],
  similar=["american-lotus","cattail"])

plant("chufa", name="Chufa", latin="Cyperus esculentus", family="Sedge",
  abundance="common", type="Ground", uses=["Raw","Nuts"], regions=["East","Central"], months=[9,10,11],
  facts={"what":"Small sweet underground tubers","how":"Raw, roasted, or ground for a nut-milk","when":"Fall","where":"Damp fields, ditches, sandy ground","value":"Starch, sugars, fat"},
  caution="Also called yellow nutsedge, a persistent 'weed' whose tubers are the food. Rinse the soil off well; they are safe and sweet. "+SAFE,
  sections=[{"title":"Identification","body":"A grass-like sedge with a triangular stem; the prize is the cluster of pea-sized tubers on the roots, sweet and almond-like."},
    {"title":"In the kitchen","body":"Eat them raw once washed, roast them, or soak and blend them into horchata-style tiger-nut milk."}],
  similar=["arrowhead","sunchoke"])

# ---- MUSHROOMS ----
plant("chicken-of-the-woods", name="Chicken of the Woods", latin="Laetiporus sulphureus", family="Polypore",
  abundance="seasonal", type="Mushroom", uses=["Cooked"], regions=["East","Central"], months=[5,6,9,10,11],
  facts={"what":"The tender edges of the young bracket, always cooked","how":"Sautéed or simmered thoroughly","when":"Spring and fall on wood","where":"On oaks and other hardwoods, never on the ground","value":"Protein; a meaty texture"},
  caution="Always cook it, and eat a small amount your first time: some people react even to correctly-identified chicken of the woods, and specimens on conifers or certain oaks disagree with more people. Mushrooms demand expert confirmation. "+SAFE,
  sections=[{"title":"Identification","body":"Overlapping shelves of vivid sulphur-yellow and orange growing straight from a tree trunk or log. No gills, a pore surface underneath."},
    {"title":"In the kitchen","body":"The young tender edges really do echo chicken. Take only the soft growing margin, cook it fully, and try a little the first time."}],
  similar=["chanterelle","puffball"])

plant("puffball", name="Giant Puffball", latin="Calvatia gigantea", family="Agaric",
  abundance="seasonal", type="Mushroom", uses=["Cooked"], regions=["East","Central"], months=[9,10,11],
  facts={"what":"The firm white interior, cooked","how":"Sliced and fried","when":"Fall","where":"Meadows, pastures, open ground","value":"A mild, tofu-like mushroom"},
  caution="CUT EVERY PUFFBALL IN HALF before eating. The inside must be pure, uniform white like a marshmallow, with NO gills, stem, or outline of a mushroom-in-egg (that would be a deadly Amanita) and no yellowing (over-ripe and upsetting). Mushrooms demand expert confirmation. "+SAFE,
  sections=[{"title":"Identification","body":"A firm white ball, sometimes as big as a soccer ball, sitting in a field. The test is internal: slice it and the flesh must be solid, even, and marshmallow-white throughout."},
    {"title":"In the kitchen","body":"Slice the young white flesh and fry it; it soaks up butter and flavor like a mild mushroom steak. Discard any that show yellow or green inside."}],
  similar=["chicken-of-the-woods","chanterelle"])

# ---- write files ----
written = 0
missing_photos = []
for p in P:
    slug = p.pop("slug")
    if slug not in CREDITS:
        missing_photos.append(slug)
        continue
    cred = CREDITS[slug]
    p["photos"] = [{
        "src": f"./photos/{slug}.jpg",
        "alt": f"{p['name']} ({p['latin']})",
        "credit": cred["artist"] or "Wikimedia Commons contributor",
        "license": cred["license"],
        "source": "Wikimedia Commons",
    }]
    with open(os.path.join(DEST, f"{slug}.json"), "w") as f:
        json.dump(p, f, indent=2, ensure_ascii=False)
    written += 1

print(f"wrote {written} plant files")
if missing_photos:
    print(f"SKIPPED (no photo yet): {missing_photos}")
