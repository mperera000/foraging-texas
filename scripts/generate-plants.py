#!/usr/bin/env python3
"""One-time generator: writes src/content/plants/*.json from the authored dataset below.
Photo credits come from the Wikimedia Commons fetch (scripts/credits_by_slug.json).
Content is original wording for the redesign concept; facts are field-guide level and
every entry defers to the safety rule: never eat on this site's word alone."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEST = os.path.join(ROOT, "src", "content", "plants")
CREDITS = json.load(open(os.path.join(HERE, "credits_by_slug.json")))

P = []
def plant(slug, **kw): kw["slug"] = slug; P.append(kw); return kw

plant("mustang-grape", name="Mustang Grape", latin="Vitis mustangensis", family="Grape",
  abundance="common", type="Vine", uses=["Fruit"], regions=["Central","East"], months=[6,7,8],
  facts={"what":"Ripe purple grapes; young leaves","how":"Jelly, juice, country wine; raw only in small amounts",
    "when":"Fruit June to August","where":"Fence lines, creek bottoms, woodland edges","value":"Sugars, vitamin C"},
  caution="Raw juice is harsh with acid and can irritate skin and mouth; wear gloves for big harvests. Confirm the felty white underside of the leaf, since peppervine, which sickens, shares the habit.",
  sections=[{"title":"Harvesting","body":"Look for low-hanging clusters on fence lines in high summer, and take only what the vine gives easily. A single healthy mustang vine can carry pounds of fruit, so there is no need to strip any one plant."},
    {"title":"In the kitchen","body":"The acid that makes these grapes rough raw is exactly what makes them shine as jelly and wine. Cook, strain, and sweeten, and you get a deep purple preserve that tastes like a Texas summer."}],
  similar=["dewberry","beautyberry"])

plant("prickly-pear", name="Prickly Pear", latin="Opuntia engelmannii", family="Cactus",
  abundance="abundant", type="Cactus", uses=["Fruit","Cooked"], regions=["West","Central"], months=[7,8,9],
  flowerMonths=[4,5],
  facts={"what":"Red fruit (tunas); young pads (nopales) in spring","how":"Fruit raw, juiced, or as jelly; pads grilled or boiled",
    "when":"Tunas July to September, pads in spring","where":"Dry ground statewide, thickest in the west","value":"Sugars, fiber, vitamin C"},
  caution="The hair-fine glochids are worse than the big spines. Tongs, thick gloves, and a flame to singe them off are not optional.",
  sections=[{"title":"Harvesting","body":"Twist tunas off with tongs into a bucket and never touch them bare-handed until they are singed or peeled. For nopales, take bright young pads in spring and slice off every eye."},
    {"title":"In the kitchen","body":"Tunas peel into a magenta fruit that juices beautifully; strain the seeds. Nopales grill like a vegetable and pair naturally with eggs, onion, and chile."}],
  similar=["chile-pequin","agarita"])

plant("chanterelle", name="Chanterelle", latin="Cantharellus texensis", family="Chanterelle",
  abundance="seasonal", type="Mushroom", uses=["Cooked"], regions=["East"], months=[6,7,8],
  facts={"what":"The whole fruiting body, cooked","how":"Sautéed; never raw","when":"Summer, one to two weeks after soaking rains",
    "where":"Oak woods in East Texas, on soil, never on wood","value":"Flavor; some B vitamins"},
  caution="The jack-o'-lantern mushroom is the dangerous double: it grows in clusters ON wood and has true gills. Chanterelles grow from soil with blunt false ridges. Mushrooms demand expert confirmation; when in doubt, throw it out.",
  sections=[{"title":"Harvesting","body":"Hunt oak woods a week after summer rain. Cut or pinch at the base, brush off the leaf litter, and carry them in a basket so the woods get their spores back."},
    {"title":"In the kitchen","body":"Dry-sauté first to drive off water, then add butter. The apricot smell survives cooking and makes these the East Texas prize."}],
  similar=["sassafras","beautyberry"])

plant("agarita", name="Agarita", latin="Mahonia trifoliolata", family="Barberry",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["Central","West"], months=[4,5],
  flowerMonths=[2,3],
  facts={"what":"Red berries; flowers","how":"Jelly, syrup, raw, wine","when":"Flowers February to March, fruit April to May",
    "where":"Dry brushland, rocky slopes, Hill Country and west","value":"Vitamin C, sugars"},
  caution="Stiff spines on every leaf tip. Wear gloves, or better, use the sheet trick.",
  sections=[{"title":"Harvesting","body":"Nobody picks agarita berries one at a time. Spread a sheet under the bush, tap the branches with a stick, and let the ripe fruit fall. Winnow out the leaves and you can gather a jelly batch in twenty minutes."},
    {"title":"In the kitchen","body":"The berries are tart and bright, closer to a currant than a blueberry. Classic uses are jelly and syrup; the strained juice also ferments into a pale country wine."},
    {"title":"Identification notes","body":"Three-part leaves, each leaflet tipped with holly-like spines, blue-green reading gray at a distance. With red berries present there is no dangerous look-alike in Texas."}],
  similar=["yaupon-holly","prickly-pear"])

plant("dewberry", name="Dewberry", latin="Rubus trivialis", family="Rose",
  abundance="abundant", type="Vine", uses=["Fruit"], regions=["East","Central"], months=[4,5,6],
  flowerMonths=[3],
  facts={"what":"Black berries; leaves for tea","how":"Raw by the handful, cobbler, jam","when":"April to early June",
    "where":"Sunny ditches, fence rows, old fields","value":"Sugars, vitamin C, fiber"},
  caution="Low trailing canes are thorny, and so are the chiggers that share the patch. Tuck pant legs in and wash up after.",
  sections=[{"title":"Harvesting","body":"Dewberries run along the ground, not up canes like blackberries, and ripen weeks earlier. Pick dead-black fruit that pulls free without a tug; red ones will only teach you patience."},
    {"title":"In the kitchen","body":"The first quart rarely makes it home. Those that do want a cobbler, or a jam loose enough to remember the fruit."}],
  similar=["mustang-grape","beautyberry"])

plant("yaupon-holly", name="Yaupon Holly", latin="Ilex vomitoria", family="Holly",
  abundance="abundant", type="Shrub", uses=["Tea"], regions=["East","Central"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"Leaves and young twigs, dried or roasted, for tea","how":"Roast and steep like green or black tea",
    "when":"Year-round","where":"Understory thickets across the eastern half of Texas","value":"Caffeine, the only native North American source"},
  caution="The leaves are the tea; the red berries are not food and will upset your stomach. Do not confuse with Chinese privet: yaupon leaves are small, leathery, and scalloped, privet leaves are smooth-edged.",
  sections=[{"title":"Harvesting","body":"Strip a colander of leaves from a healthy thicket, wash, and roast on a sheet pan until they go toasty brown. The plant regrows so fast that ranchers curse it."},
    {"title":"In the cup","body":"Roasted yaupon steeps into something between green tea and yerba mate, no bitterness even oversteeped. It kept Native Texans and early settlers caffeinated for centuries."}],
  similar=["sassafras","agarita"])

plant("wood-sorrel", name="Wood Sorrel", latin="Oxalis stricta", family="Wood sorrel",
  abundance="abundant", type="Ground", uses=["Raw"], regions=["East","Central","West"], months=[3,4,5,6,7],
  facts={"what":"Leaves, flowers, green seed pods","how":"Raw as a trail nibble or salad lemon-note","when":"Spring into summer, fading in high heat",
    "where":"Lawns, beds, woodland edges, everywhere","value":"Vitamin C; bright oxalic tang"},
  caution="The lemon tang is oxalic acid: fine as a garnish and nibble, unwise as a whole salad bowl, and worth skipping if you have kidney stone history.",
  sections=[{"title":"Identification","body":"Three perfect hearts to a leaf, folding along their midline in strong sun, with small five-petal yellow flowers. Clover has ovals; sorrel has hearts."},
    {"title":"On the trail","body":"This is the classic first forage: safe to recognize, bright to taste, growing in every yard. The little pickle-shaped pods pop pleasantly."}],
  similar=["henbit","chickweed"])

plant("beautyberry", name="American Beautyberry", latin="Callicarpa americana", family="Mint",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["East"], months=[8,9,10],
  facts={"what":"Clusters of shocking purple berries","how":"Jelly is the classic; raw only a taste at a time","when":"August through October",
    "where":"Piney woods understory, stream banks","value":"Modest sugars; famous color"},
  caution="Raw berries are mealy and best in small amounts; the payoff is the jelly. The crushed leaves are a folk mosquito rub, not a food.",
  sections=[{"title":"Harvesting","body":"The purple is so loud you can spot a bush from a moving car in September. Strip clusters into a bag; ten minutes fills a jelly batch."},
    {"title":"In the kitchen","body":"Beautyberry jelly comes out rose-colored and delicate, closer to floral than fruity, and it is the East Texas answer to agarita."}],
  similar=["dewberry","turks-cap"])

plant("pecan", name="Pecan", latin="Carya illinoinensis", family="Walnut",
  abundance="common", type="Tree", uses=["Nuts"], regions=["Central","East"], months=[10,11,12],
  facts={"what":"Nuts after husks split","how":"Raw, toasted, pie","when":"October into December","where":"River bottoms statewide; the state tree",
    "value":"Fat, protein, minerals"},
  caution="Street-tree and roadside nuts pick up whatever the ground holds; favor clean ground. Mind ownership: many Texas pecans stand on private land.",
  sections=[{"title":"Harvesting","body":"Wait for the husks to split and shake or gather from the ground within a few days of falling, before weevils and squirrels take the crop."},
    {"title":"Storing","body":"In-shell pecans keep for months somewhere cool; shelled meats go rancid at room temperature, so freeze what you will not eat by spring."}],
  similar=["black-walnut","hackberry"])

plant("henbit", name="Henbit", latin="Lamium amplexicaule", family="Mint",
  abundance="abundant", type="Ground", uses=["Raw","Cooked"], regions=["East","Central","West"], months=[1,2,3,4],
  facts={"what":"Leaves, stems, purple flowers","how":"Raw in salads or wilted like spinach","when":"The cool months, January to April",
    "where":"Every winter lawn and fallow bed in Texas","value":"Greens when little else grows"},
  caution="Unsprayed ground only; winter lawns are heavily treated. Henbit is not a true dead-nettle stinger and has no dangerous look-alike, but confirm the square stem and clasping scalloped leaves.",
  sections=[{"title":"Identification","body":"A mint-family winter annual: square stems, scalloped leaves clasping the stem in tiers, tiny orchid-like purple flowers. It carpets bare winter ground."},
    {"title":"In the kitchen","body":"Mild, slightly grassy, one of the first fresh greens of the year. Toss young tops raw, or wilt handfuls into eggs and soups."}],
  similar=["chickweed","wood-sorrel"])

plant("sassafras", name="Sassafras", latin="Sassafras albidum", family="Laurel",
  abundance="common", type="Tree", uses=["Tea","Spice"], regions=["East"], months=[1,2,3,4,5,6,7,8,9,10,11,12],
  facts={"what":"Young leaves (filé); root bark for traditional tea","how":"Dry and grind leaves; steep root bark",
    "when":"Leaves spring to fall; roots year-round","where":"East Texas woods and fence rows","value":"Flavor and tradition more than nutrition"},
  caution="Root tea contains safrole, which the FDA flags in quantity; treat it as an occasional tradition, not a daily drink. The mitten-shaped leaves make ID easy.",
  sections=[{"title":"Identification","body":"One tree, three leaf shapes on the same branch: oval, mitten, and three-lobed. Scratch a twig and it smells of root beer, because this is where root beer began."},
    {"title":"Filé","body":"Dry young leaves, grind, and sift: that is filé, the gumbo thickener. A single small tree supplies a kitchen for a year."}],
  similar=["yaupon-holly","black-walnut"])

plant("elderberry", name="Elderberry", latin="Sambucus canadensis", family="Moschatel",
  abundance="common", type="Shrub", uses=["Fruit"], regions=["East","Central"], months=[6,7],
  flowerMonths=[4,5],
  facts={"what":"Ripe black berries, cooked; flower clusters","how":"Syrup, jelly, fritters from flowers; never raw in quantity",
    "when":"Flowers late spring, fruit June and July","where":"Ditches and creek banks with wet feet","value":"Anthocyanins; folk cold syrup"},
  caution="Cook the berries: raw fruit, and all stems, leaves, and unripe berries, carry cyanide-producing compounds. Strip berries fully from stems. Learn the shrub confidently in flower before trusting yourself in fruit.",
  sections=[{"title":"Harvesting","body":"Snip whole umbels of fully black berries and freeze them; frozen berries rattle off their stems in seconds, which beats an hour of picking."},
    {"title":"In the kitchen","body":"Simmered and strained, elderberries make the syrup half of Texas keeps in the fridge by November. The flowers, dipped in batter, fry into lacy fritters."}],
  similar=["beautyberry","dewberry"])

plant("texas-persimmon", name="Texas Persimmon", latin="Diospyros texana", family="Ebony",
  abundance="common", type="Tree", uses=["Fruit"], regions=["Central","West"], months=[8,9],
  facts={"what":"Small black fruit, dead ripe only","how":"Raw, or pulped for puddings and quick breads","when":"August and September",
    "where":"Rocky Hill Country slopes; smooth gray peeling bark","value":"Sugars, fiber"},
  caution="Underripe fruit is an astringent ambush that dries your whole mouth; wait until the fruit is black, soft, and practically falling. The big seeds want a food mill.",
  sections=[{"title":"Harvesting","body":"Shake a branch over a sheet and take only what falls. If it resists, it is not ready, and it will punish you for rushing."},
    {"title":"In the kitchen","body":"Ripe pulp tastes of dates and molasses. Run fruit through a food mill to shed the seeds, then bake it into breads or freeze it flat."}],
  similar=["hackberry","honey-mesquite"])

plant("honey-mesquite", name="Honey Mesquite", latin="Prosopis glandulosa", family="Legume",
  abundance="abundant", type="Tree", uses=["Flour"], regions=["West","Central"], months=[6,7,8,9],
  facts={"what":"Whole dry pods (not the seeds alone)","how":"Grind dry pods into sweet flour; simmer for syrup","when":"June through September",
    "where":"Everywhere ranchers wish it wasn't","value":"Natural sugars, protein, fiber; gluten-free flour"},
  caution="Harvest pods straight off the tree, dry and unblemished; ground-collected pods mold fast, and moldy pods are unsafe. Taste one first, sweetness varies tree to tree.",
  sections=[{"title":"Harvesting","body":"Pick straw-colored pods that snap cleanly, from the branch rather than the dirt. Dry them brittle in a low oven or a hot truck dashboard, which is the traditional West Texas dehydrator."},
    {"title":"Mesquite flour","body":"Blitz brittle pods, sift, repeat. The flour is sweet with a cocoa-coffee edge and swaps for a quarter of the flour in pancakes and cornbread."}],
  similar=["texas-persimmon","prickly-pear"])

plant("cattail", name="Cattail", latin="Typha latifolia", family="Cattail",
  abundance="common", type="Aquatic", uses=["Cooked","Flour"], regions=["East","Central","West"], months=[3,4,5,6],
  facts={"what":"Spring shoots; early-summer pollen; rhizome starch","how":"Shoots raw or steamed; pollen as flour boost","when":"Shoots March to May, pollen May and June",
    "where":"Ditches, tank edges, any standing fresh water","value":"Starch, some protein from pollen"},
  caution="Cattails filter their water, pollutants included, so harvest only from clean water you would trust. Before flower spikes appear, blue-flag iris shoots can fool a beginner: iris is flat-fanned and toxic, cattail is round-stemmed.",
  sections=[{"title":"Harvesting","body":"Grip a young shoot low and pull; the white base slides free like a leek. For pollen, bend a flowering head into a bag and tap: a minute of drumming yields golden tablespoons."},
    {"title":"In the kitchen","body":"The shoot hearts taste of cucumber and leek, good raw or barely steamed. Pollen folds into pancake batter for color and a corn-silk sweetness."}],
  similar=["canada-wild-onion","purslane"])

plant("chickweed", name="Chickweed", latin="Stellaria media", family="Pink",
  abundance="common", type="Ground", uses=["Raw"], regions=["East","Central"], months=[1,2,3,4],
  facts={"what":"Tender tops, leaves, and starry flowers","how":"Raw, by the bowl, or pesto","when":"Cool season, January to April",
    "where":"Shaded beds, damp lawns, winter gardens","value":"Green freshness in deep winter"},
  caution="Confirm the single line of hairs running up one side of the stem and the absence of milky sap; scarlet pimpernel, the look-alike, has square-ish stems, orange flowers, and no hair line.",
  sections=[{"title":"Identification","body":"A sprawling mat of small oval leaves with white flowers so deeply split their five petals look like ten. Stretch a stem gently: the skin breaks but an elastic inner core holds."},
    {"title":"In the kitchen","body":"Chickweed eats like sprouts, mild and juicy. Scissor-harvest the top few inches and it regrows for weeks."}],
  similar=["henbit","wood-sorrel"])

plant("dandelion", name="Dandelion", latin="Taraxacum officinale", family="Aster",
  abundance="abundant", type="Ground", uses=["Raw","Cooked","Tea"], regions=["East","Central","West"], months=[1,2,3,4,11,12],
  facts={"what":"Leaves, flowers, roots: the whole plant","how":"Young leaves raw, older cooked; flowers for fritters; roots roasted for tea",
    "when":"Cool months in Texas, November through April","where":"Lawns and disturbed ground everywhere","value":"Vitamins A and K, minerals; classic bitter green"},
  caution="The only real hazard is the lawn itself: harvest nowhere herbicides are sprayed. Texas false dandelions are look-alikes but harmless.",
  sections=[{"title":"Identification","body":"A basal rosette of backward-toothed leaves, one hollow milky stem per flower, never branched. Everything similar in a Texas lawn is at worst just less tasty."},
    {"title":"In the kitchen","body":"Pick young leaves before flowering for salads; wilt older ones with bacon and vinegar the way generations of grandmothers settled the bitterness argument."}],
  similar=["henbit","chickweed"])

plant("purslane", name="Purslane", latin="Portulaca oleracea", family="Purslane",
  abundance="abundant", type="Ground", uses=["Raw","Cooked"], regions=["East","Central","West"], months=[6,7,8,9],
  facts={"what":"Succulent stems and paddle leaves","how":"Raw for crunch, or cooked into eggs and stews (verdolagas)","when":"The hot months, June to September",
    "where":"Sidewalk cracks, gardens, bare summer dirt","value":"Omega-3s, unusually rich for a green"},
  caution="The look-alike is prostrate spurge: snap a stem, and milky white sap means spurge, drop it. Purslane bleeds clear.",
  sections=[{"title":"Identification","body":"Fat, smooth, reddish stems hugging the ground with rubbery paddle leaves. It thrives in July heat that kills lettuce at forty paces."},
    {"title":"In the kitchen","body":"Lemony crunch raw; silky when cooked. Across the border it is verdolagas, simmered with pork and tomatillo, which is the best argument for it."}],
  similar=["wood-sorrel","lambs-quarters"])

plant("lambs-quarters", name="Lamb's Quarters", latin="Chenopodium album", family="Amaranth",
  abundance="common", type="Ground", uses=["Cooked","Raw"], regions=["East","Central","West"], months=[4,5,6,7,8],
  facts={"what":"Young leaves and growing tips","how":"Cooked like spinach; young leaves raw in moderation","when":"April through August",
    "where":"Gardens, field edges, disturbed rich soil","value":"Protein-rich green; vitamins A and C, calcium"},
  caution="Like spinach it carries oxalates, so cook mature leaves and vary your greens. Confirm the white dusty coating on new growth; nightshade seedlings share ground but lack it.",
  sections=[{"title":"Identification","body":"Goosefoot-shaped leaves with a white mealy dust on the newest growth that beads water like wax. Rub it: the dust is the fingerprint."},
    {"title":"In the kitchen","body":"This is the wild spinach that out-spinaches spinach: steamed, creamed, or folded into anything that welcomes a deep green leaf."}],
  similar=["purslane","dandelion"])

plant("canada-wild-onion", name="Canada Wild Onion", latin="Allium canadense", family="Amaryllis",
  abundance="common", type="Ground", uses=["Raw","Cooked"], regions=["East","Central"], months=[2,3,4,5],
  facts={"what":"Bulbs, greens, and spring bulblet heads","how":"Anywhere an onion or chive belongs","when":"February through May",
    "where":"Lawns, meadows, open woods","value":"Onion-family flavor and compounds"},
  caution="THE RULE HAS NO EXCEPTIONS: no onion smell, no eating. Crow poison mimics it leaf for leaf and bulb for bulb but has no odor, and it grows in the same lawns.",
  sections=[{"title":"Identification","body":"Grassy leaves from a small bulb, and the unmistakable test: crush a leaf and the whole plant must announce itself as onion. Silence means crow poison; leave it."},
    {"title":"In the kitchen","body":"The greens are wild chives, the bulbs are shallots in miniature, and the little aerial bulblets pickle into perfect cocktail onions."}],
  similar=["cattail","henbit"])

plant("turks-cap", name="Turk's Cap", latin="Malvaviscus arboreus var. drummondii", family="Mallow",
  abundance="common", type="Shrub", uses=["Fruit","Tea"], regions=["Central","East"], months=[5,6,7,8,9,10,11],
  facts={"what":"Red flowers, marble-sized red fruit, young leaves","how":"Flowers and fruit raw or as tea; fruit cooks into syrup",
    "when":"May through November, one of the longest seasons going","where":"Shady understory, yards, creek banks","value":"Nectar sugars; gentle hibiscus-family tea"},
  caution="No meaningful look-alike when flowering: nothing else here makes that never-opening red turban of a bloom. Fruit is mild and a little mealy, better cooked than grazed.",
  sections=[{"title":"Identification","body":"A shade-loving mallow with soft maple-ish leaves and red flowers that stay furled like a wrapped turban, hummingbird-designed."},
    {"title":"Uses","body":"Flowers steep into a pale hibiscus-style tea. The little red fruits taste faintly of apple and do their best work as syrup or jelly."}],
  similar=["beautyberry","chile-pequin"])

plant("flameleaf-sumac", name="Flameleaf Sumac", latin="Rhus lanceolata", family="Cashew",
  abundance="common", type="Shrub", uses=["Tea","Spice"], regions=["Central","West"], months=[8,9,10],
  facts={"what":"Fuzzy red berry clusters","how":"Cold-steep for sumac-ade; dry and grind for the spice","when":"August through October",
    "where":"Fence rows and rocky hillsides; scarlet fall foliage","value":"Vitamin C tang, malic acid"},
  caution="Cashew family: those with strong cashew or mango allergies should be careful. Poison sumac has WHITE berries and lives in swamps, not on Texas hillsides; red upright clusters are the safe signature.",
  sections=[{"title":"Harvesting","body":"Snip whole red cones on a dry day and taste first: rain washes the tang off, and it returns after a few dry days. Sour is what you want."},
    {"title":"Sumac-ade","body":"Swish clusters in cold water until it turns pink lemonade, strain through cloth, sweeten. Heat turns it bitter, so keep it cold."}],
  similar=["agarita","turks-cap"])

plant("black-walnut", name="Black Walnut", latin="Juglans nigra", family="Walnut",
  abundance="common", type="Tree", uses=["Nuts"], regions=["East","Central"], months=[9,10,11],
  facts={"what":"Nuts inside green tennis-ball husks","how":"Raw or baked; strong, wine-dark flavor","when":"September through November",
    "where":"Creek and river bottoms","value":"Fat, protein; assertive flavor"},
  caution="Husks stain hands, clothes, and driveways a permanent brown; glove up. The shells are famously hard, so think vise or hammer, not nutcracker.",
  sections=[{"title":"Harvesting","body":"Gather green balls off the ground early, before the husk blackens into dye. Stomp-roll the husks off, wash the nuts, and cure them in mesh for two weeks."},
    {"title":"In the kitchen","body":"Half the people who meet black walnut love it forever; it is pecan's loud cousin, best where it can lead, in ice cream, fudge, and banana bread."}],
  similar=["pecan","sassafras"])

plant("chile-pequin", name="Chile Pequin", latin="Capsicum annuum var. glabriusculum", family="Nightshade",
  abundance="common", type="Shrub", uses=["Spice"], regions=["Central","East"], months=[8,9,10,11,12],
  facts={"what":"Tiny oval chiles, green ripening red","how":"Fresh in salsas, dried and crushed, or vinegar-pickled","when":"August into winter",
    "where":"Under trees and fence lines where birds perch","value":"Serious heat; vitamins A and C"},
  caution="It is genuinely hot, several times a jalapeño, and the oils linger on fingers. It is also the parent of a nightshade family with inedible members: confirm the tiny upright red-when-ripe fruit on a knee-high shrub.",
  sections=[{"title":"Identification","body":"Texas's native chile: a shin-to-knee-high shrub in dappled shade, dotted with upright pea-sized fruit. Birds plant it under every fence-line tree."},
    {"title":"In the kitchen","body":"One or two fruits wake up a whole pot of beans. Dry a jar in autumn and you have crushed red pepper with a smoky wild edge all year."}],
  similar=["turks-cap","prickly-pear"])

plant("hackberry", name="Sugar Hackberry", latin="Celtis laevigata", family="Hemp",
  abundance="abundant", type="Tree", uses=["Fruit"], regions=["East","Central","West"], months=[9,10,11,12],
  facts={"what":"Pea-sized orange-red berries, eaten whole","how":"Crunch whole (thin sweet skin over a crunchy nut) or blend into bars","when":"September into winter, hanging on the twig",
    "where":"Every fence line and vacant lot in Texas","value":"Sugar, fat, and protein in one package, a true trail food"},
  caution="The berry is mostly seed; eat it like a crunchy snack, not a mouthful of soft fruit, or blend and strain. Warty gray bark is the tree's fingerprint.",
  sections=[{"title":"Identification","body":"The tree everyone has and nobody planted: gray bark studded with corky warts, sandpaper leaves, and winter twigs beaded with orange berries."},
    {"title":"On the trail","body":"Hackberries are candy that crunches. Native Texans pounded them whole into cakes, sugar, fat, and protein in one wild bar."}],
  similar=["texas-persimmon","pecan"])

# ---- write files ----
os.makedirs(DEST, exist_ok=True)
written = 0
for p in P:
    slug = p.pop("slug")
    cred = CREDITS[slug]
    p["photos"] = [{
        "src": f"./photos/{slug}.jpg",
        "alt": f"{p['name']} ({p['latin']})",
        "credit": cred["artist"],
        "license": cred["license"],
        "source": "Wikimedia Commons",
    }]
    with open(os.path.join(DEST, f"{slug}.json"), "w") as f:
        json.dump(p, f, indent=2, ensure_ascii=False)
    written += 1
print(f"wrote {written} plant files to {DEST}")
