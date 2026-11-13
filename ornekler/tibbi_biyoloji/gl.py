# İngilizce sorulardaki kelimeler için sözlük (cevap kutusunda yeşil çip olur). Bölüm yazdıkça genişler.
import re
GL = {
'tight junction': 'sıkı bağlantı', 'adherens junction': 'yapışma bağlantısı', 'desmosome': 'desmozom', 'hemidesmosome': 'hemidesmozom', 'gap junction': 'aralık bağlantısı', 'connexin': 'konneksin', 'cadherins': 'kaderinler', 'cadherin': 'kaderin', 'catenin': 'katenin', 'selectins': 'selektinler', 'selectin': 'selektin', 'integrins': 'integrinler', 'integrin': 'integrin', 'intermediate filaments': 'ara filamentler', 'actin': 'aktin', 'microtubules': 'mikrotübüller', 'microtubule': 'mikrotübül', 'tubulin': 'tubulin', 'kinesins': 'kinezinler', 'dynein': 'dinein', 'myosin': 'miyozin', 'fibronectin': 'fibronektin', 'laminin': 'laminin', 'fibrillin': 'fibrilin', 'elastin': 'elastin', 'proteoglycan': 'proteoglikan', 'glycosaminoglycan': 'glikozaminoglikan', 'hyaluronic acid': 'hiyalüronik asit', 'cartilage': 'kıkırdak', 'vitamin': 'vitamin', 'scurvy': 'skorbüt', 'diameter': 'çap', 'filament': 'lif', 'lysosome': 'lizozom', 'lysosomes': 'lizozomlar', 'peroxisomes': 'peroksizomlar', 'catalase': 'katalaz', 'endoplasmic reticulum': 'endoplazmik retikulum', 'golgi': 'Golgi', 'signal sequence': 'sinyal dizisi', 'secretion': 'salgı', 'transport': 'taşıma', 'diffusion': 'difüzyon', 'facilitated diffusion': 'kolaylaştırılmış difüzyon', 'active transport': 'aktif taşıma', 'gradient': 'gradyan', 'concentration': 'derişim', 'pump': 'pompa', 'channel': 'kanal', 'channels': 'kanallar', 'carrier': 'taşıyıcı', 'symporters': 'simporterler', 'glucose': 'glikoz', 'osmosis': 'ozmoz', 'phagocytosis': 'fagositoz', 'pinocytosis': 'pinositoz', 'endocytosis': 'endositoz', 'vesicle': 'kesecik', 'fluidity': 'akışkanlık', 'decreased': 'azalmış', 'permeable': 'geçirgen', 'intermembrane space': 'zarlar arası boşluk', 'inner membrane': 'iç zar', 'inherited': 'kalıtılır', 'metastasis': 'metastaz', 'leukocyte': 'lökosit', 'leukocytes': 'lökositler', 'endothelial': 'endotel', 'platelets': 'trombositler', 'venom': 'zehir', 'sphingolipids': 'sfingolipitler', 'glycolipids': 'glikolipitler', 'peripheral': 'periferal', 'integral': 'integral', 'anchored': 'bağlı', 'sequence': 'dizi', 'muscle': 'kas', 'contraction': 'kasılma', 
# genel soru kelimeleri
'which of the following': 'aşağıdakilerden hangisi', 'is not': 'değildir', 'true': 'doğru', 'false': 'yanlış', 'correct': 'doğru',
'incorrect': 'yanlış', 'except': 'hariç', 'all of the above': 'hepsi', 'none of the above': 'hiçbiri', 'mainly': 'çoğunlukla',
'most abundant': 'en bol', 'responsible for': '…dan sorumlu', 'known as': '… olarak bilinen', 'found in': '…da bulunan',
'characterized by': '… ile tanımlanan', 'consists of': '…dan oluşur', 'called': 'denir', 'refers to': '… anlamına gelir',
'function': 'işlev', 'structure': 'yapı', 'property': 'özellik', 'feature': 'özellik', 'example': 'örnek', 'statement': 'ifade',
'discovered': 'keşfetti', 'described': 'tanımladı', 'proposed': 'öne sürdü', 'proved': 'kanıtladı', 'developed': 'geliştirdi',
'scientist': 'bilim insanı', 'theory': 'kuram', 'law': 'yasa', 'ratio': 'oran', 'experiment': 'deney',
# hücre ve yaşam
'cell': 'hücre', 'cells': 'hücreler', 'cell theory': 'hücre kuramı', 'living': 'canlı', 'organism': 'organizma', 'organisms': 'organizmalar',
'unicellular': 'tek hücreli', 'multicellular': 'çok hücreli', 'single-celled': 'tek hücreli', 'tissue': 'doku', 'organ': 'organ',
'unit of life': 'yaşamın birimi', 'reproduction': 'üreme', 'growth': 'büyüme', 'development': 'gelişim', 'regulation': 'düzenleme',
'energy processing': 'enerji işleme', 'response': 'yanıt', 'environment': 'çevre', 'evolutionary adaptation': 'evrimsel uyum', 'order': 'düzen',
'pre-existing': 'önceden var olan', 'division': 'bölünme', 'hereditary': 'kalıtsal', 'inheritance': 'kalıtım', 'gene': 'gen', 'genes': 'genler',
'allele': 'alel', 'alleles': 'aleller', 'chromosome': 'kromozom', 'chromosomes': 'kromozomlar', 'chromatin': 'kromatin', 'nucleus': 'çekirdek',
'nuclein': 'nüklein', 'enzyme': 'enzim', 'mutation': 'mutasyon', 'mutations': 'mutasyonlar', 'radiation': 'radyasyon', 'microscope': 'mikroskop',
'compound microscope': 'bileşik mikroskop', 'ultracentrifuge': 'ultrasantrifüj', 'transforming principle': 'dönüştürücü ilke', 'double helix': 'çift sarmal',
'adaptor molecule': 'adaptör molekül', 'natural selection': 'doğal seçilim', 'common ancestor': 'ortak ata', 'evolution': 'evrim',
'endosymbiotic': 'endosimbiyotik', 'engulfed': 'yuttu', 'mitochondria': 'mitokondriler', 'mitochondrion': 'mitokondri', 'chloroplast': 'kloroplast',
'chloroplasts': 'kloroplastlar', 'phospholipids': 'fosfolipitler', 'phospholipid': 'fosfolipit', 'bilayer': 'çift katman', 'membrane': 'zar',
'plasma membrane': 'plazma zarı', 'cell membrane': 'hücre zarı', 'hydrophilic': 'suyu seven', 'hydrophobic': 'sudan kaçan', 'lipophilic': 'yağı seven',
'domain': 'üst alem (domain)', 'domains': 'üst alemler', 'kingdom': 'alem', 'kingdoms': 'alemler', 'classification': 'sınıflandırma',
'prokaryotic': 'prokaryotik', 'eukaryotic': 'ökaryotik', 'prokaryote': 'prokaryot', 'prokaryotes': 'prokaryotlar', 'eukaryote': 'ökaryot',
'eukaryotes': 'ökaryotlar', 'archaea': 'arkeler', 'bacteria': 'bakteriler', 'nucleoid': 'nükleoit', 'plasmid': 'plazmit', 'plasmids': 'plazmitler',
'cell wall': 'hücre duvarı', 'peptidoglycan': 'peptidoglikan', 'cholesterol': 'kolesterol', 'ribosomes': 'ribozomlar', 'ribosome': 'ribozom',
'cytoplasm': 'sitoplazma', 'cytosol': 'sitozol', 'cytoskeleton': 'hücre iskeleti', 'organelles': 'organeller', 'organelle': 'organel',
'membrane-bound': 'zarla çevrili', 'lack': 'yoksun olmak', 'contain': 'içermek', 'flagella': 'kamçılar', 'flagellum': 'kamçı', 'cilia': 'siller',
'rotate': 'döner', 'glycocalyx': 'glikokaliks', 'capsule': 'kapsül', 'periplasm': 'periplazma', 'outer membrane': 'dış zar',
'lipopolysaccharides': 'lipopolisakkaritler', 'halophiles': 'halofiller (tuz seven)', 'methanogens': 'metanojenler', 'thermoacidophiles': 'termoasidofiller',
'methane': 'metan', 'extreme': 'aşırı', 'virus': 'virüs', 'viruses': 'virüsler', 'host cell': 'konak hücre', 'parasites': 'parazitler',
'capsid': 'kapsit', 'protein coat': 'protein kılıf', 'envelope': 'zarf', 'bacteriophage': 'bakteriyofaj', 'bacteriophages': 'bakteriyofajlar',
'zygote': 'zigot', 'egg': 'yumurta', 'sperm': 'sperm', 'stem cells': 'kök hücreler', 'embryonic stem cells': 'embriyonik kök hücreler',
'plasticity': 'plastisite (esneklik)', 'differentiate': 'farklılaşmak', 'polarity': 'polarite (kutupluluk)', 'cell types': 'hücre tipleri',
'autotrophs': 'ototroflar', 'heterotrophs': 'heterotroflar', 'producers': 'üreticiler', 'consumers': 'tüketiciler', 'decomposers': 'ayrıştırıcılar',
'organotrophs': 'organotroflar', 'inorganotrophs': 'inorganotroflar', 'chemoautotrophic': 'kemoototrof', 'phototrophic': 'fototrof', 'sunlight': 'güneş ışığı',
'energy': 'enerji', 'currency': 'para birimi', 'hydrolysis': 'hidroliz', 'water': 'su', 'polar': 'kutuplu', 'hydrogen bonds': 'hidrojen bağları',
'solvent': 'çözücü', 'macromolecules': 'makromoleküller', 'polymers': 'polimerler', 'monomers': 'monomerler', 'proteins': 'proteinler',
'nucleic acids': 'nükleik asitler', 'polysaccharides': 'polisakkaritler', 'lipids': 'lipitler', 'amino acids': 'amino asitler',
'nucleotides': 'nükleotitler', 'genome': 'genom', 'karyotype': 'karyotip', 'apoptosis': 'apoptoz', 'programmed cell death': 'programlı hücre ölümü',
'extracellular matrix': 'hücre dışı matriks', 'collagen': 'kolajen', 'signal': 'sinyal', 'hormone': 'hormon', 'neurotransmitters': 'nörotransmitterler',
}


def gloss(text):
    low = re.sub(r'<[^>]+>', ' ', text).lower()
    out, kapali = [], ''
    for w in sorted(GL, key=len, reverse=True):
        if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', low) and w not in kapali:
            out.append((w, GL[w])); kapali += ' ' + w
    return out
