#!/usr/bin/env python3
"""Lauren Burns Interiors, static site generator.
Run:  python3 build.py   (writes HTML into ./site)
Add projects by appending to PROJECTS below and rebuilding.
"""
import os
import sys
import urllib.request

try:
    from PIL import Image
except ImportError:
    Image = None

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
IMG_DIR = "images"
MAX_IMAGE_DIMENSION = 1920
JPEG_QUALITY = 82

def wix_src(img_id, ext="jpg"):
    """Original Wix CDN URL (used only when fetching assets)."""
    return f"https://static.wixstatic.com/media/{img_id}~mv2.{ext}"

def normalize_ext(ext):
    ext = ext.lower()
    return "jpg" if ext == "jpeg" else ext

def img(img_id, depth=0, ext="jpg"):
    """Relative path to a locally hosted image."""
    prefix = "../" * depth
    return f"{prefix}{IMG_DIR}/{img_id}.{normalize_ext(ext)}"

def parse_image(entry):
    if len(entry) == 2:
        return entry[0], entry[1], "jpg"
    return entry[0], entry[1], normalize_ext(entry[2])

def thumb_src(pr, depth=0):
    iid, _, ext = parse_image(pr["images"][0])
    return img(iid, depth, ext)

# ---------------------------------------------------------------- projects
PROJECTS = [
    {
        "slug": "custom-luxury", "title": "Custom Luxury", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Layered blues and tailored millwork give this residence a quietly grand register, classic forms, modern restraint.",
        "images": [
            ("0b75c1_d48f5e242e774d4ca6cdac93cfe24637", "g-w"),
            ("lochinvar_241016_1883w", "g-w"),
            ("lochinvar_241016_2265w", "g-w"),
            ("lochinvar_241016_1892w", "g-t"),
            ("lochinvar_241016_1940w", "g-w"),
            ("lochinvar_241016_1914w", "g-w"),
            ("lochinvar_241016_1920w", "g-h"),
            ("lochinvar_241016_1988w", "g-w"),
            ("lochinvar_241016_2068w", "g-w"),
            ("lochinvar_241016_2104w", "g-t"),
            ("lochinvar_241016_2166w", "g-h"),
            ("lochinvar_241016_2234w", "g-w"),
            ("lochinvar_241016_2258w", "g-t"),
            ("lochinvar_241016_2303w", "g-w"),
            ("lochinvar_241016_2333w", "g-h"),
            ("lochinvar_241016_2347w", "g-w"),
            ("lochinvar_241016_2373w", "g-h"),
        ],
    },
    {
        "slug": "bold-earthy", "title": "Bold & Earthy", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Grounded tones, natural texture, and confident contrast, a home that feels rooted and unmistakably lived-in.",
        "images": [
            ("0b75c1_a97310e5504d41d69c3f35d83c08957f", "g-h"),
            ("0b75c1_9db3879aa591458b8cec814d76fe20a5", "g-w"),
            ("0b75c1_4b851c81be954ff0bc8e5b1c5eb6ba55", "g-t"),
            ("0b75c1_80a1df6a5aed4a6b8fb140edef9e9235", "g-h"),
            ("0b75c1_7a5a79ecfbed472592db07ed69f61240", "g-w"),
            ("0b75c1_648d15f238cc4814bb06efd001aa37c2", "g-t"),
            ("0b75c1_ca413155dbc64a488b8d7ea5e03b5f6b", "g-h"),
            ("0b75c1_9bc4b429b111482db613983ce265d0ce", "g-h"),
        ],
    },
    {
        "slug": "organic-sophistication", "title": "Organic Sophistication", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Soft neutrals and organic materials in easy conversation, sophistication without a hint of effort.",
        "images": [
            ("0b75c1_fee480971fe84e58b260f842b8c03450", "g-w"),
            ("0b75c1_ca4e7cecf0934ed2b3c1cdbd0f4c5c93", "g-t"),
            ("0b75c1_d2d737c0626c4616ade8c45b02b27f48", "g-s"),
            ("0b75c1_7316658382084d91b7301653f83d1bf0", "g-s"),
            ("0b75c1_871d9aee1a54462892fc87beda60ca3c", "g-s"),
            ("0b75c1_584e30f55ba1422ebacb1ca515d78dc0", "g-w"),
        ],
    },
    {
        "slug": "sophisticated-chic", "title": "Sophisticated Chic", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Polished finishes and a disciplined palette, chic that reads as timeless rather than trend.",
        "images": [
            ("0b75c1_34df603a7fc84393b0f12c51d26a4f42", "g-s"),
            ("0b75c1_3e288df7304f4d94ad9f14a47f7f5bb2", "g-s"),
            ("0b75c1_cd65cb5515ba4c269336360197b6e0b6", "g-s"),
            ("0b75c1_951bfcb6e57f4df9a129a0a0c60bd18b", "g-s"),
            ("0b75c1_69b48635031d45babb53d8bc25c17981", "g-s"),
            ("0b75c1_319100a495c04bec8e94a036b90349fb", "g-s"),
            ("0b75c1_dc364636e38d4e978e8517c50a45da52", "g-s"),
            ("0b75c1_09dc4cfd1d164e8b86cad7dc6c092ad5", "g-s"),
            ("0b75c1_4c0329764cbf4cccb1b676fa5607fbe0", "g-s"),
            ("0b75c1_92f92e7dedbb4fb38f2113501f384d6d", "g-s"),
            ("0b75c1_5b832bd7c9d54404804ddf716a8bea95", "g-s"),
            ("0b75c1_e655539cefd949edb167527fbd7b4547", "g-s"),
        ],
    },
    {
        "slug": "beach-serenity", "title": "Beach Serenity", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Soft coastal palettes and relaxed furnishings create an easy, sun-washed retreat by the water.",
        "images": [
            ("0b75c1_7a83ba69f68747bf8ade1cf08d139c23", "g-w"),
            ("beachhouse_230523_225", "g-w"),
            ("beachhouse_230523_081", "g-w"),
            ("beachhouse_230523_091", "g-h"),
            ("beachhouse_230523_039", "g-w"),
            ("beachhouse_230523_237", "g-w"),
            ("beachhouse_230523_001", "g-h"),
            ("beachhouse_230523_023", "g-h"),
        ],
    },
    {
        "slug": "modern-masculine", "title": "Modern Masculine", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Dark wood, veined marble, and floor-to-ceiling views, modern lines set against a wooded backdrop.",
        "images": [
            ("masc_260209_268w", "g-w"),
            ("masc_260209_170w", "g-w"),
            ("masc_260209_202w", "g-w"),
            ("masc_260209_257w", "g-w"),
            ("masc_260209_280w", "g-w"),
            ("masc_260209_288w", "g-w"),
            ("masc_260209_307w", "g-w"),
            ("masc_260209_309w", "g-h"),
            ("masc_260209_315w", "g-w"),
            ("masc_260209_292w", "g-w"),
            ("masc_260209_325_2w", "g-w"),
            ("masc_260209_337w", "g-t"),
        ],
    },
    {
        "slug": "kitchen-refresh", "title": "Kitchen Refresh", "type": "residential",
        "cat": "Private Residential",
        "blurb": "A thoughtful kitchen update, new finishes, improved flow, and details that make everyday cooking feel effortless.",
        "images": [
            ("0b75c1_d3a63e0e3dbc4de492078a743df39282", "g-s"),
            ("0b75c1_676ec7713c544b529b0d51b30c4c7aea", "g-s"),
            ("0b75c1_290c055250354148b727096c55085c80", "g-s"),
            ("0b75c1_e0a7f2884e3c494dac0d93b99c9b1f13", "g-s"),
            ("0b75c1_223d948238024272af5346c5199abc8a", "g-s"),
            ("0b75c1_a34ac371433b43fd960241c18d6d93f1", "g-s"),
            ("0b75c1_afdff7c4014b4ba096759e2ffd2aa4ba", "g-s"),
            ("0b75c1_ab7f84847212458cb57e47f0e55e06ca", "g-s"),
            ("0b75c1_1eb28ea8716d4fe4a6ca3e85e7c3959a", "g-s"),
            ("0b75c1_e105b4a490d040d29cc1c921fc2a9bdf", "g-s"),
        ],
    },
    {
        "slug": "cozy-and-classic", "title": "Cozy & Classic", "type": "residential",
        "cat": "Private Residential",
        "blurb": "Traditional details and layered comfort combine for a home that feels welcoming, polished, and timeless.",
        "images": [
            ("0b75c1_320d427f58e6470c9f4938ca1a832a38", "g-h"),
            ("0b75c1_c8fe9ef7bb404fb090c9fccee373ab85", "g-t"),
            ("0b75c1_b172ec7ab5d44ffd9797e858ec841e36", "g-w"),
            ("0b75c1_53bdbfa00d76477fb6e7a4da0e9f8bf4", "g-h"),
            ("0b75c1_8eabd51d7c0c4b48959b7ca447c6888a", "g-h"),
            ("0b75c1_6f44a95d7eb044f2b84b98cbbd910f0b", "g-t"),
            ("0b75c1_d14a56d355de4038bdb5ca95406ce190", "g-w"),
            ("0b75c1_3252a1ceee80484db3429622285d3c6e", "g-h"),
            ("0b75c1_4137756485ab4cfca1547d9c96159d3a", "g-h"),
            ("0b75c1_b84d351f0d2f46e7a0cd2db5fb04711a", "g-h"),
            ("0b75c1_3cc4ca0d81204f38bac8e6d9f8fed405", "g-t"),
            ("0b75c1_0a402f462d4d45a9a3ebb28eb5cd9a09", "g-w"),
            ("0b75c1_1503814c71344d73a29895f0c7c3aed3", "g-t"),
            ("0b75c1_8f9378f82e6d4bf4a64bdad4713204e3", "g-w"),
            ("0b75c1_d62975470e4541939453e828735aea0c", "g-t"),
            ("0b75c1_2fc2e6f164204980b629f94674084cc0", "g-w"),
            ("0b75c1_cda92924cb8a45d8a88c043917d9c69c", "g-t"),
            ("0b75c1_67f0f65a2dc340668cb55aae233cfe68", "g-t"),
        ],
    },
    {
        "slug": "wake-plastic-surgery", "title": "Wake Plastic Surgery", "type": "commercial",
        "cat": "Cary, NC",
        "blurb": "A refined clinical environment designed to feel calm, welcoming, and tailored to the patient experience.",
        "images": [
            ("0b75c1_f6fcaa68d13d4b06a6831fba401dcecc", "g-s"),
            ("0b75c1_de73f01886e9420b80a82b3dfefa6064", "g-s"),
            ("0b75c1_2300359013ce461d9dd5929221772621", "g-s"),
            ("0b75c1_3d3adcc52cc84c34bc0a580ebbb3caa8", "g-s"),
            ("0b75c1_a4b0cbf00ef04fb5b3287e1c48d35ee4", "g-s"),
            ("0b75c1_291efff2ebda417f81cc71f685ca04c9", "g-s"),
            ("0b75c1_0c8c4541bd9440ba9f90d2871104e755", "g-s"),
            ("0b75c1_3504cbff0a7b4e23af5f24b95fe016bf", "g-s"),
            ("0b75c1_4a5f498adf824a209d589a35a2c0ef29", "g-s"),
            ("0b75c1_198f99c8a12b4064bd249a1aa5128987", "g-s"),
            ("0b75c1_0c5a51a6288e4251965f069e0376c8bd", "g-s"),
            ("0b75c1_aa2e476fc94a480797edd8359d8af772", "g-s"),
            ("0b75c1_89267c96ee004e2bb52a1df584799b28", "g-s"),
            ("0b75c1_cf4f5704d8e14a34bbc2528cbd48fbe7", "g-s"),
            ("0b75c1_eed762755cf3469ab093c2c4cc3b7256", "g-s"),
            ("0b75c1_ce6b1492bcd94fbfb168b8f6a4037c11", "g-s"),
            ("0b75c1_d70a8a41808d4b87b73322221a11d3c3", "g-s"),
        ],
    },
    {
        "slug": "trex", "title": "Trex", "type": "commercial",
        "cat": "Los Angeles, CA",
        "blurb": "Prop styling for Trex through Karma Agency. Photography by Catherine Nguyen.",
        "images": [
            ("0b75c1_24a500c9a74846899bb02f0032002389", "g-s", "jpg"),
            ("0b75c1_3a64b5cc36584091a08082c66131c4c9", "g-s", "jpg"),
            ("0b75c1_f41f61e939fd40e7b6779d7ca6d6ea89", "g-s", "jpg"),
            ("0b75c1_f628815c10d644248b88ac57d2e7d373", "g-s", "jpg"),
            ("0b75c1_9abb33e0a6df4d348fdfe50b714f2e85", "g-s", "jpg"),
        ],
    },
    {
        "slug": "halo-hair-boutique", "title": "Halo Hair Boutique", "type": "commercial",
        "cat": "Cary, NC",
        "blurb": "A light-filled salon boutique designed for ease, style, and the everyday rhythm of a busy studio.",
        "images": [
            ("0b75c1_74897023de6a4e058a6ca6c169b14eb7", "g-t"),
            ("0b75c1_eef328a57e65400bae803430fcf25f58", "g-t"),
            ("0b75c1_4747e6cd9c56469c9e017aa6002aac71", "g-t"),
            ("0b75c1_4c29ddebf5854f849c41fe1a51b8cbb5", "g-s"),
            ("0b75c1_f817b57d2d934a8c8e0d04e828d97371", "g-s"),
            ("0b75c1_1173253c80184b79b42f521c5c39e63c", "g-w"),
            ("0b75c1_8c6e98ccaf26405686fbce28d45fb666", "g-t"),
        ],
    },
    {
        "slug": "zest-sushi", "title": "Zest Sushi & Small Plates", "type": "commercial",
        "cat": "Cary, NC",
        "blurb": "Warm wood tones and layered texture bring intimate energy to this Cary dining destination.",
        "images": [
            ("0b75c1_b164b4af0ea04dd0820bb66ae8de3736", "g-t", "jpg"),
            ("0b75c1_4c501a9d61d6441ebca9c24eb6a42972", "g-t", "jpg"),
            ("0b75c1_f597a99668484d279f9f1e8219660b2f", "g-t", "jpg"),
            ("0b75c1_0d23b92e4cb64385ac13772a7d298e76", "g-t", "jpg"),
        ],
    },
    {
        "slug": "ssi-strategy", "title": "SSI Strategy", "type": "commercial",
        "cat": "Parsippany, NJ",
        "blurb": "A professional headquarters with a confident palette and purposeful space planning.",
        "images": [
            ("0b75c1_5f343a32cc5847979d2f23417f947833", "g-w"),
            ("0b75c1_caa7dd77cfce4b4e98f80aee306b783f", "g-t", "png"),
            ("0b75c1_f090b49e581f4c8bb5c2487c70843232", "g-w", "jpg"),
            ("0b75c1_331aa00cb91641a7b78790bbff354aee", "g-w"),
            ("0b75c1_4ea1b3e727c74020a3c67d3b405bb3f9", "g-w"),
        ],
    },
]

HERO_SLIDES = [
    ("0b75c1_a97310e5504d41d69c3f35d83c08957f", "Bold & Earthy", "Private Residential"),
    ("0b75c1_d48f5e242e774d4ca6cdac93cfe24637", "Custom Luxury", "Private Residential"),
    ("0b75c1_fee480971fe84e58b260f842b8c03450", "Organic Sophistication", "Private Residential"),
]

HERO_SLIDES_MOBILE = [
    ("lochinvar_241016_2104w", "Custom Luxury", "Private Residential"),
    ("masc_260209_337w", "Modern Masculine", "Private Residential"),
    ("0b75c1_6f44a95d7eb044f2b84b98cbbd910f0b", "Cozy & Classic", "Private Residential"),
    ("lochinvar_241016_1892w", "Cozy & Classic", "Private Residential"),
]

SERVICES = [
    ("New Construction & Finish Selections",
     "From foundation to final detail, we guide every finish decision with intention and cohesion. We streamline the selection process for builders and homeowners alike. From countertops and cabinetry to tile, lighting, flooring, exterior materials, paint, and stains, every selection is organized and submitted on schedule for a seamless build."),
    ("Renovation & Remodel Design",
     "Redesigning a kitchen, bath, or entire home? We collaborate closely with you and your general contractor to ensure thoughtful design, clear communication, and timely execution. From space planning and renderings to finish selections and project coordination, we manage the design process from start to completion."),
    ("Full Furnishings & Styling",
     "A fully realized home, thoughtfully layered. This service includes space planning, furniture selection, custom pieces, textiles, lighting, and accessories that are curated, procured, and installed to create a polished, livable result that feels both elevated and personal."),
    ("Space Planning, Furniture & Procurement",
     "Ideal for clients seeking professional guidance without full-scale renovation. We develop detailed floor plans, layouts, and design direction, then handle sourcing and procurement to ensure everything fits beautifully from both a functional and aesthetic standpoint."),
    ("Virtual & National Design",
     "Not located in North Carolina? We work with clients nationwide through virtual consultations, digital presentations, and mailed samples. Using photos, measurements, and collaborative meetings, we deliver a complete design experience wherever you are."),
]

TEAM = [
    ("Lauren Burns", "Owner & Principal Designer", "0b75c1_a254cabfc36d4db7bd16f7b004497910", "jpg",
     "Lauren Burns designs spaces that are timeless with a masterful mix of styles, from traditional to contemporary. Lauren loves turning spaces that need an overhaul into layered, sophisticated and usable living spaces for clients. She owns her client\u2019s desires for the home, combines them with her passion for design and creates spaces they are proud to live in, spaces that feel effortlessly chic and purposeful. By layering textures, along with mixing new with vintage pieces, she creates signature interiors with sophisticated simplicity. Accompanied by over 10 years of experience in the interior design industry, Lauren uses her expertise to turn her creative vision into your reality."),
    ("Daniela McShane", "Design Coordinator", "0b75c1_e81a52b91d594af0934736df6c80d7f8", "jpg",
     "Daniela is the touchpoint for all new client discovery calls and contracts, and assists with project management for our clients throughout the entire design process. Detail oriented and always thinking outside the box when needed, Daniela ensures our clients have a seamless design experience. Her kind personality and attention to detail are something clients comment on often."),
    ("Taylor Weller", "Design Assistant", "0b75c1_3c5ad5204ba94cca921e382830e0d4d6", "jpg",
     "Taylor assists Lauren with presentation prep and behind-the-scenes coordination to help bring each project to life, supporting the team with her talent for organization and strong attention to detail. Her background in digital marketing and her eye for design make her a valuable asset, and her thoughtful communication keeps our brand voice consistent and authentic across every platform."),
]

AWARDS = [
    ("2026", "Influential Women of Wake, Lauren Burns"),
    ("2026", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2026", "5 West Magazine Diamond Awards, Best Interior Design Firm, Gold"),
    ("2025", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2024", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2023", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2022", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2021", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2020", "Cary Magazine Maggy Awards, Best Interior Design Firm, Winner"),
    ("2016", "Triangle Downtowner Magazine, Best of Downtowner Award"),
    ("2016", "Triangle Downtowner Magazine, Reader Favorites Award"),
]

FEATURES = [
    ("2026", "Midtown Magazine, Curated Comfort"),
    ("2025", "Home Design & Decor Magazine, Kitchen & Bath"),
    ("2025", "Home Design & Decor Magazine, Interior Designers of the Carolinas"),
    ("2024", "Home Design & Decor Magazine, Interior Designers of the Carolinas"),
    ("2022", "Home Design & Decor Magazine, Design Board"),
    ("2022", "Ngala Trading Product Catalogue, Fall 2022\u2013Winter 2023"),
    ("2021", "Home Design & Decor Magazine, Designers at Home, Cover Feature"),
    ("2021", "Voyage Raleigh, Exploring Life & Business with Lauren Burns"),
    ("2021", "Voyage Raleigh, @highpointmarket Instagram Takeover"),
    ("2019", "Cary Lifestyle, A Very Cary Christmas"),
    ("2019", "Cary Lifestyle, Mid-Century Modern Meets Industrial Sleek"),
    ("2019", "Cary Lifestyle, Women Blazing Trails in Cary"),
    ("2019", "Charlotte Observer, Designer Spotlight"),
    ("2019", "Raleigh News & Observer, Designer Spotlight"),
    ("2018", "Walter Magazine, Story of a House"),
    ("2017", "Walter Magazine, Story of a House"),
    ("2017", "Cary Magazine, A Fresh Perspective"),
    ("2016", "Karen Saks, Designer of the Month"),
    ("2015", "Cary Magazine, Hanging Out At Home"),
]

PHONE = "(919) 818-5683"
IG = "https://instagram.com/laurenburnsinteriors"
FB = "https://www.facebook.com/laurenburnsinteriors"
CUSTOM_DOMAIN = "www.laurenburnsinteriors.com"

def all_images():
    """Every (img_id, ext) pair referenced by the site."""
    seen = {}
    for pr in PROJECTS:
        for entry in pr["images"]:
            iid, _, ext = parse_image(entry)
            seen[iid] = ext
    for img_id, _, _ in HERO_SLIDES:
        seen.setdefault(img_id, "jpg")
    for img_id, _, _ in HERO_SLIDES_MOBILE:
        seen.setdefault(img_id, "jpg")
    for _, _, img_id, ext, _ in TEAM:
        seen[img_id] = normalize_ext(ext)
    for img_id in (
        "0b75c1_d48f5e242e774d4ca6cdac93cfe24637",
        "0b75c1_69b48635031d45babb53d8bc25c17981",
        "0b75c1_dced07394c8f41e78ac4e3596ea79e6e",
        "0b75c1_1e63287e8dec446483d7d2666a35d121",
    ):
        seen.setdefault(img_id, "jpg")
    return list(seen.items())

def download_images():
    img_root = os.path.join(OUT, IMG_DIR)
    os.makedirs(img_root, exist_ok=True)
    for img_id, ext in all_images():
        ext = normalize_ext(ext)
        dest = os.path.join(img_root, f"{img_id}.{ext}")
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print("skip", f"{img_id}.{ext}")
            stale = os.path.join(img_root, f"{img_id}.jpeg")
            if ext == "jpg" and os.path.exists(stale):
                os.remove(stale)
            continue
        url = wix_src(img_id, ext)
        print("fetch", url)
        urllib.request.urlretrieve(url, dest)
    print("downloaded", len(all_images()), "images into", img_root)

def _image_has_alpha(im):
    if im.mode in ("RGBA", "LA"):
        return True
    if im.mode == "P":
        return "transparency" in im.info
    return False

def _resize_image(im, max_dim):
    w, h = im.size
    if max(w, h) <= max_dim:
        return im
    if w >= h:
        new_w = max_dim
        new_h = int(h * max_dim / w)
    else:
        new_h = max_dim
        new_w = int(w * max_dim / h)
    return im.resize((new_w, new_h), Image.Resampling.LANCZOS)

def compress_images():
    if Image is None:
        raise SystemExit("Pillow is required for image compression. Install with: pip3 install Pillow")

    img_root = os.path.join(OUT, IMG_DIR)
    if not os.path.isdir(img_root):
        print("no images directory:", img_root)
        return

    before = 0
    after = 0
    converted = 0
    optimized = 0

    for name in sorted(os.listdir(img_root)):
        path = os.path.join(img_root, name)
        if not os.path.isfile(path):
            continue
        ext = name.rsplit(".", 1)[-1].lower()
        if ext not in {"jpg", "jpeg", "png", "webp"}:
            continue

        before += os.path.getsize(path)
        stem = name.rsplit(".", 1)[0]
        is_logo = stem == "logo"
        max_dim = 512 if is_logo else MAX_IMAGE_DIMENSION

        with Image.open(path) as im:
            im = _resize_image(im, max_dim)
            has_alpha = _image_has_alpha(im)

            if is_logo or (ext == "png" and has_alpha):
                if im.mode not in ("RGBA", "RGB"):
                    im = im.convert("RGBA" if has_alpha else "RGB")
                im.save(path, format="PNG", optimize=True, compress_level=9)
            elif ext in {"jpg", "jpeg"} or ext == "png":
                rgb = im.convert("RGB")
                jpg_path = os.path.join(img_root, f"{stem}.jpg")
                rgb.save(
                    jpg_path,
                    format="JPEG",
                    quality=JPEG_QUALITY,
                    optimize=True,
                    progressive=True,
                )
                if path != jpg_path and os.path.exists(path):
                    os.remove(path)
                    converted += 1
                path = jpg_path
            elif ext == "webp":
                rgb = im.convert("RGB") if not has_alpha else im
                rgb.save(path, format="WEBP", quality=JPEG_QUALITY, method=6)

        after += os.path.getsize(path)
        optimized += 1

    saved = before - after
    pct = (saved / before * 100) if before else 0
    print(
        f"compressed {optimized} images: "
        f"{before / 1024 / 1024:.1f}MB -> {after / 1024 / 1024:.1f}MB "
        f"({pct:.0f}% smaller, {converted} converted to JPEG)"
    )

# ---------------------------------------------------------------- chrome
def brand_block(depth=0, footer=False):
    p = "../" * depth
    logo_src = img("logo", depth, "png")
    text = f"""    <span class="brand-text">
      <span class="brand-name">Lauren Burns</span>
      <span class="brand-sub">Interiors</span>
    </span>"""
    logo = f'<img class="brand-logo" src="{logo_src}" alt="" width="52" height="52">'
    if footer:
        return f"""    <div class="footer-brand">
      {logo}
{text}
    </div>"""
    return f"""  <a class="brand" href="{p}index.html" aria-label="Lauren Burns Interiors home">
    {logo}
{text}
  </a>"""

def nav(active, depth=0):
    p = "../" * depth
    items = [("Portfolio", f"{p}portfolio.html"), ("About", f"{p}about.html"),
             ("Services", f"{p}services.html"), ("Press", f"{p}press.html"),
             ("Inquire", f"{p}contact.html")]
    def link(label, href):
        active_cls = ' class="active"' if label == active else ""
        return f'      <li><a href="{href}"{active_cls}>{label}</a></li>'
    lis = "\n".join(link(label, href) for label, href in items)
    return f"""<header class="nav">
{brand_block(depth)}
  <nav aria-label="Primary">
    <button class="menu-btn" aria-expanded="false">Menu</button>
    <ul class="nav-links">
{lis}
    </ul>
  </nav>
</header>"""

def footer(depth=0):
    p = "../" * depth
    return f"""<footer class="footer">
  <div class="footer-grid">
    <div>
{brand_block(depth, footer=True)}
    </div>
    <div>
      <h4>Studio</h4>
      <ul>
        <li><a href="{p}portfolio.html">Portfolio</a></li>
        <li><a href="{p}about.html">About</a></li>
        <li><a href="{p}services.html">Services</a></li>
      </ul>
    </div>
    <div>
      <h4>Connect</h4>
      <ul>
        <li><a href="{p}contact.html">Inquire</a></li>
        <li><a href="{IG}">Instagram</a></li>
        <li><a href="{FB}">Facebook</a></li>
        <li><a href="tel:+19198185683">{PHONE}</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2026 Lauren Burns Interiors. All rights reserved.</span>
    <span>Photography by <a href="http://www.catherinenguyen.com/">Catherine Nguyen Photography</a></span>
  </div>
</footer>"""

def _read(rel):
    with open(os.path.join(OUT, rel)) as f:
        return f.read()

FORMSPREE_FORM_ID = "mbdnrbko"
FORMSPREE_SCRIPT = f"""<script>
  window.formspree = window.formspree || function () {{ (formspree.q = formspree.q || []).push(arguments); }};
  formspree('initForm', {{
    formElement: '#inquiry-form',
    formId: '{FORMSPREE_FORM_ID}',
    useDefaultStyles: false,
    onSuccess: function (ctx) {{
      var el = ctx.form.querySelector('[data-fs-success]');
      if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}
  }});
</script>
<script src="https://unpkg.com/@formspree/ajax@1" defer></script>"""

def page(title, desc, body, active="", depth=0, extra_script=""):
    css = _read("css/styles.css")
    js = _read("js/main.js")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Manrope:wght@300;400;500&family=Open+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
{nav(active, depth)}
<main>
{body}
</main>
{footer(depth)}
<script>
{js}
</script>
{extra_script}
</body>
</html>"""

# ---------------------------------------------------------------- pages
def build_index():
    def hero_slides(slides):
        return "\n".join(
            f'    <div class="hero-slide{" on" if i == 0 else ""}" data-title="{t}" data-cat="{c}" '
            f'style="background-image:url(\'{img(img_id)}\')" role="img" aria-label="{t} interior by Lauren Burns Interiors"></div>'
            for i, (img_id, t, c) in enumerate(slides))

    featured = "\n".join(f"""    <a class="card reveal" href="projects/{pr['slug']}.html">
      <div class="frame"><img src="{thumb_src(pr)}" alt="{pr['title']}, interior design by Lauren Burns Interiors" loading="lazy"></div>
      <div class="meta">
        <span class="eyebrow">{pr['cat']}</span>
        <span class="display-md">{pr['title']}</span>
      </div>
    </a>""" for pr in PROJECTS if pr["type"] == "residential")

    body = f"""<section class="hero">
  <div class="hero-slides hero-slides--desktop">
{hero_slides(HERO_SLIDES)}
  </div>
  <div class="hero-slides hero-slides--mobile">
{hero_slides(HERO_SLIDES_MOBILE)}
  </div>
  <div class="hero-caption">
    <span class="eyebrow" data-hero-cat>{HERO_SLIDES[0][2]}</span>
    <h1 class="display-xl" data-hero-title>{HERO_SLIDES[0][1]}</h1>
    <div class="hero-rule"></div>
  </div>
</section>

<section class="section">
  <div class="wrap-narrow statement reveal">
    <span class="eyebrow">Lauren Burns Interiors</span>
    <p class="lede">Timeless interiors, elevated living, layered, sophisticated spaces shaped around the way you live.</p>
    <a class="btn" href="about.html">About the Studio</a>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="panels reveal">
      <a class="panel" href="portfolio.html">
        <div class="bg" style="background-image:url('{img('0b75c1_d48f5e242e774d4ca6cdac93cfe24637')}')"></div>
        <div class="panel-label"><span class="eyebrow">Portfolio</span><span class="display-md">Residential Design</span></div>
      </a>
      <a class="panel" href="services.html">
        <div class="bg" style="background-image:url('{img('0b75c1_69b48635031d45babb53d8bc25c17981')}')"></div>
        <div class="panel-label"><span class="eyebrow">Services</span><span class="display-md">How We Work</span></div>
      </a>
      <a class="panel" href="contact.html">
        <div class="bg" style="background-image:url('{img('0b75c1_1e63287e8dec446483d7d2666a35d121')}')"></div>
        <div class="panel-label"><span class="eyebrow">Inquire</span><span class="display-md">Begin a Project</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:3rem; display:flex; justify-content:space-between; align-items:baseline; gap:1rem; flex-wrap:wrap;">
      <h2 class="display-lg">Selected Work</h2>
      <a class="eyebrow" href="portfolio.html" style="color:var(--bone-dim);">View Full Portfolio &rarr;</a>
    </div>
    <div class="grid-projects">
{featured}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap-narrow statement reveal">
    <span class="eyebrow">Recognition</span>
    <p class="lede">Voted Best Interior Design Firm, Cary Magazine Maggy Awards, six consecutive years.</p>
    <a class="btn" href="press.html">Press &amp; Awards</a>
  </div>
</section>"""
    return page("Lauren Burns Interiors | Interior Design | Raleigh, NC",
                "Lauren Burns Interiors designs timeless, layered, sophisticated living spaces, residential and commercial interior design in Raleigh, NC and nationwide.",
                body, active="")

def build_portfolio():
    cards = "\n".join(f"""    <a class="card reveal" href="projects/{pr['slug']}.html" data-type="{pr['type']}">
      <div class="frame"><img src="{thumb_src(pr)}" alt="{pr['title']}, interior design by Lauren Burns Interiors" loading="lazy"></div>
      <div class="meta">
        <span class="eyebrow">{pr['cat']}</span>
        <span class="display-md">{pr['title']}</span>
      </div>
    </a>""" for pr in PROJECTS)
    body = f"""<section class="page-hero">
  <div class="bg" style="background-image:url('{img('0b75c1_9db3879aa591458b8cec814d76fe20a5')}')"></div>
  <div class="hero-caption">
    <span class="eyebrow">Portfolio</span>
    <h1 class="display-xl">Your Home, Our Vision</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <p class="lede reveal" style="max-width:46ch; margin-bottom:2.5rem;">Residential and commercial spaces designed with intention, from private homes to salons, restaurants, and professional offices.</p>
    <div class="portfolio-filters reveal" role="tablist" aria-label="Filter portfolio">
      <button class="portfolio-filter on" type="button" data-filter="all" role="tab" aria-selected="true">All</button>
      <button class="portfolio-filter" type="button" data-filter="residential" role="tab" aria-selected="false">Residential</button>
      <button class="portfolio-filter" type="button" data-filter="commercial" role="tab" aria-selected="false">Commercial</button>
    </div>
    <div class="grid-projects">
{cards}
    </div>
  </div>
</section>"""
    return page("Portfolio | Lauren Burns Interiors",
                "Residential and commercial interior design portfolio by Lauren Burns Interiors, Raleigh, NC.",
                body, active="Portfolio")

def build_project(pr):
    figs = "\n".join(
        f'    <figure class="{cls} reveal"><img src="{img(iid, depth=1, ext=ext)}" alt="{pr["title"]}, interior detail" loading="lazy"></figure>'
        for iid, cls, ext in (parse_image(entry) for entry in pr["images"]))
    peers = [p for p in PROJECTS if p["type"] == pr["type"]]
    nxt = peers[(peers.index(pr) + 1) % len(peers)]
    hero_iid, _, hero_ext = parse_image(pr["images"][0])
    body = f"""<section class="page-hero">
  <div class="bg" style="background-image:url('{img(hero_iid, depth=1, ext=hero_ext)}')"></div>
  <div class="hero-caption">
    <span class="eyebrow">{pr['cat']}</span>
    <h1 class="display-xl">{pr['title']}</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="gallery">
{figs}
    </div>
  </div>
</section>
<section class="section tight">
  <div class="wrap-narrow statement reveal">
    <span class="eyebrow">Next Project</span>
    <a class="display-lg" href="{nxt['slug']}.html">{nxt['title']}</a>
  </div>
</section>"""
    return page(f"{pr['title']} | Lauren Burns Interiors",
                f"{pr['title']}, {pr['blurb']}", body, active="Portfolio", depth=1)

def build_about():
    rows = "\n".join(f"""    <div class="team-row reveal">
      <div class="portrait"><img src="{img(img_id, ext=ext)}" alt="{name}, {role}" loading="lazy"></div>
      <div>
        <span class="eyebrow">{role}</span>
        <h2 class="display-md" style="margin:0.5rem 0 1.2rem;">{name}</h2>
        <p class="muted">{bio}</p>
      </div>
    </div>""" for name, role, img_id, ext, bio in TEAM)
    body = f"""<section class="page-hero">
  <div class="bg" style="background-image:url('{img('0b75c1_9db3879aa591458b8cec814d76fe20a5')}')"></div>
  <div class="hero-caption">
    <span class="eyebrow">About</span>
    <h1 class="display-xl">The Studio</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap-narrow">
    <p class="lede reveal" style="margin-bottom:1.5rem;">Great design results from collaboration, the union that occurs when a client&rsquo;s dreams and a designer&rsquo;s skill come together.</p>
    <p class="muted reveal">Lauren Burns Interiors is a full-service interior design firm specializing in residential and commercial design. Our approach is fresh, innovative, and personal, helping you create an inviting, timeless, and functional environment. Whether your dream is a custom-designed home or a creatively remodeled kitchen, we bring the expertise and vision to bring your living spaces to life.</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap">
{rows}
  </div>
</section>"""
    return page("About | Lauren Burns Interiors",
                "Meet the team behind Lauren Burns Interiors, full-service residential and commercial interior design in Raleigh, NC.",
                body, active="About")

def build_services():
    rows = "\n".join(f"""    <div class="service-row reveal">
      <h3 class="display-md">{name}</h3>
      <p class="muted">{desc}</p>
    </div>""" for name, desc in SERVICES)
    body = f"""<section class="page-hero">
  <div class="bg" style="background-image:url('{img('0b75c1_dced07394c8f41e78ac4e3596ea79e6e')}')"></div>
  <div class="hero-caption">
    <span class="eyebrow">Services</span>
    <h1 class="display-xl">How We Work</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <p class="lede reveal" style="max-width:46ch; margin-bottom:4rem;">From new construction to full furnishings, every engagement is guided by intention, cohesion, and clear communication.</p>
{rows}
  </div>
</section>
<section class="section tight">
  <div class="wrap-narrow statement reveal">
    <span class="eyebrow">Ready to begin?</span>
    <p class="lede">Tell us about your project.</p>
    <a class="btn" href="contact.html">Inquire</a>
  </div>
</section>"""
    return page("Services | Lauren Burns Interiors",
                "Interior design services by Lauren Burns Interiors: new construction, renovation and remodel design, full furnishings and styling, space planning, and virtual design nationwide.",
                body, active="Services")

def build_press():
    aw = "\n".join(f'      <li class="reveal"><span class="award-year">{y}</span><span>{t}</span></li>' for y, t in AWARDS)
    ft = "\n".join(f'      <li class="reveal"><span class="award-year">{y}</span><span>{t}</span></li>' for y, t in FEATURES)
    body = f"""<section class="page-hero plain">
  <div class="hero-caption">
    <span class="eyebrow">Press</span>
    <h1 class="display-xl">Awards</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap-narrow">
    <h2 class="display-lg reveal" style="margin-bottom:2.5rem;">Awards</h2>
    <ul class="award-list">
{aw}
    </ul>
  </div>
</section>
<section class="section tight">
  <div class="wrap-narrow">
    <h2 class="display-lg reveal" style="margin-bottom:2.5rem;">Publications &amp; Features</h2>
    <ul class="award-list">
{ft}
    </ul>
  </div>
</section>"""
    return page("Press | Lauren Burns Interiors",
                "Awards and press for Lauren Burns Interiors, Best Interior Design Firm, Cary Magazine Maggy Awards, and features in publications across the Carolinas.",
                body, active="Press")

def build_contact():
    body = f"""<section class="page-hero">
  <div class="bg" style="background-image:url('{img('0b75c1_1e63287e8dec446483d7d2666a35d121')}')"></div>
  <div class="hero-caption">
    <span class="eyebrow">Inquire</span>
    <h1 class="display-xl">Ready to Elevate Your&nbsp;Space?</h1>
    <div class="hero-rule"></div>
  </div>
</section>
<section class="section">
  <div class="wrap-narrow">
    <p class="lede reveal" style="margin-bottom:3.5rem;">Tell us about your project and we will be in touch shortly.</p>
    <form id="inquiry-form" class="form-grid reveal" name="inquiry" action="https://formspree.io/f/{FORMSPREE_FORM_ID}" method="POST">
      <input type="hidden" name="_subject" value="New inquiry — Lauren Burns Interiors">
      <label><span>First Name</span><input type="text" name="first-name" autocomplete="given-name" data-fs-field required><span class="field-error" data-fs-error="first-name"></span></label>
      <label><span>Last Name</span><input type="text" name="last-name" autocomplete="family-name" data-fs-field required><span class="field-error" data-fs-error="last-name"></span></label>
      <label><span>Email</span><input type="email" name="email" autocomplete="email" data-fs-field required><span class="field-error" data-fs-error="email"></span></label>
      <label><span>Phone</span><input type="tel" name="phone" autocomplete="tel" data-fs-field></label>
      <label class="full"><span>Address</span><input type="text" name="address" autocomplete="street-address" data-fs-field></label>
      <label><span>Desired Start Date</span><input type="text" name="start-date" data-fs-field></label>
      <label><span>Project Type</span>
        <select name="project-type" data-fs-field>
          <option>New Construction</option>
          <option>Renovation &amp; Remodel</option>
          <option>Full Furnishing &amp; Styling</option>
          <option>Space Planning &amp; Procurement</option>
          <option>Virtual / National Design</option>
          <option>Commercial</option>
        </select>
      </label>
      <label class="full"><span>Which rooms are included in your project?</span><input type="text" name="rooms" data-fs-field></label>
      <label class="full"><span>Describe what we can help you with</span><textarea name="message" data-fs-field required></textarea><span class="field-error" data-fs-error="message"></span></label>
      <label class="full"><span>How did you hear about us?</span><input type="text" name="referral" data-fs-field></label>
      <div class="full form-submit-wrap">
        <button class="btn btn-submit" type="submit" data-fs-submit-btn>Submit Inquiry</button>
        <div class="form-status" data-fs-success></div>
        <div class="form-status form-status-error" data-fs-error></div>
      </div>
    </form>
    <p class="muted reveal contact-phone-note" style="margin-top:3rem; font-size:0.9rem;">Prefer to Call or Text?<br class="contact-phone-break"> You can reach us at <a href="tel:+19198185683" style="color:var(--bone);">(919) 818 - 5683</a>.</p>
  </div>
</section>"""
    return page("Inquire | Lauren Burns Interiors",
                "Start a project with Lauren Burns Interiors, residential and commercial interior design in Raleigh, NC and nationwide.",
                body, active="Inquire", extra_script=FORMSPREE_SCRIPT)

# ---------------------------------------------------------------- write
def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)

def write_cname():
    full = os.path.join(OUT, "CNAME")
    with open(full, "w") as f:
        f.write(CUSTOM_DOMAIN + "\n")
    print("wrote", "CNAME")

if __name__ == "__main__":
    if "--fetch-images" in sys.argv:
        download_images()
        sys.exit(0)
    if "--compress-images" in sys.argv:
        compress_images()
        sys.exit(0)
    download_images()
    write("index.html", build_index())
    write("portfolio.html", build_portfolio())
    write("about.html", build_about())
    write("services.html", build_services())
    write("press.html", build_press())
    write("contact.html", build_contact())
    for pr in PROJECTS:
        write(f"projects/{pr['slug']}.html", build_project(pr))
    write_cname()
    print("done,", len(PROJECTS) + 6, "pages")
