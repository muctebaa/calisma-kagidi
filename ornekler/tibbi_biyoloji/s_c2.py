"""Bölüm 13–17: Cell Membranes and Organelles-2 (cell 2.pdf, Dr. Selma Yılmaz) — organeller, protein trafiği, çekirdek."""
from ortak import E, T

BOLUMLER = [('13', 'Organellere genel bakış; hücre duvarı ve zar', 'Cell 2 (S. Yılmaz)'),
            ('14', 'Lizozom, endozom, otofaji, vakuol; Tay-Sachs', 'Cell 2'),
            ('15', 'Peroksizom; HMP yolu ve G6PD eksikliği', 'Cell 2'),
            ('16', 'ER, ribozom, protein hedefleme, Golgi; I-cell hastalığı', 'Cell 2'),
            ('17', 'Çekirdek ve çekirdekçik; mitokondri ve kloroplasta giriş', 'Cell 2')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM, CHAIN = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM, k.CHAIN

    # ================= 13 =================
    k.h2('13 · Organellere genel bakış')
    add('<p>Hücre sürekli hareket halindedir (dynamic flux): ışık mikroskobunda kromozom ve kesecik taşınmasından hücrenin sürünmesine kadar birçok hareket görülür. Bütün ökaryot hücrelerde bir <b>çekirdek</b> ve sitozolde çok sayıda <b>organel</b> vardır; '
        'her organeli kendine özgü zarı ve <b>içindeki ve zarındaki özgün proteinler</b> tanımlar.</p>')
    add(TIP('🧩 Kaç zar?', '<p><b>Çift zarlı</b> (arada intermembrane space): <b>nucleus, mitochondrion, chloroplast</b>. Diğer bütün organeller <b>tek zarlıdır</b>. <b>Zarsız</b> yapılar: <b>ribosome</b> ve çekirdekteki <b>nucleolus</b>.</p>'))
    add(TABLE(['Organel', 'Yapı', 'Görev'], [
        [E('Nucleus', 'çekirdek'), '<b>nuclear envelope</b> (çift zar) + <b>nuclear pores</b>; zarf ER ile devamlı; içinde kromatin (DNA + protein) ve <b>nucleoli</b>', 'kromozomları barındırır; çekirdekçikte ribozom alt birimleri yapılır; porlar giriş-çıkışı düzenler'],
        [E('Ribosome', 'ribozom'), 'rRNA + proteinden <b>iki alt birim</b>; zarsız; sitozolde serbest ya da ER\'ye bağlı', '<b>protein sentezi</b>'],
        [E('Rough ER', 'granüllü ER'), 'ribozomlu tübül ve keseler; çekirdek zarfıyla devamlı', 'salgı ve diğer proteinlerin sentezi; glikoproteinlere karbonhidrat ekleme; yeni zar üretimi'],
        [E('Smooth ER', 'düz ER'), 'ribozomsuz', '<b>lipit sentezi</b>, karbonhidrat metabolizması, <b>Ca²⁺ depolama</b>, ilaç ve zehirlerin <b>detoksifikasyonu</b>'],
        [E('Golgi apparatus', 'Golgi aygıtı'), 'yassı zar keseleri yığını; <b>polarite</b>: <b>cis</b> ve <b>trans</b> yüzler', 'protein, karbonhidrat ve fosfolipitleri değiştirir; polisakkarit sentezi; ürünleri ayırıp keseciklerle gönderir'],
        [E('Lysosome', 'lizozom'), 'hidrolitik enzim kesesi (<b>hayvan hücresi</b>)', 'yutulan maddeleri, makromolekülleri ve hasarlı organelleri geri dönüşüm için parçalar'],
        [E('Vacuole', 'koful'), 'bitkide büyük zarlı kesecik', 'sindirim, depolama, atık, su dengesi, büyüme, koruma'],
        [E('Mitochondrion', 'mitokondri'), 'çift zar; iç zarda kıvrımlar: <b>cristae</b>', '<b>hücresel solunum</b> (ATP)'],
        [E('Chloroplast', 'kloroplast'), 'iki zar, sıvı <b>stroma</b>; içinde <b>thylakoids</b>, yığınlar halinde <b>grana</b> (bitki)', '<b>fotosentez</b>'],
        [E('Peroxisome', 'peroksizom'), 'tek zarlı özel metabolik bölme', 'hidrojeni oksijene aktarıp <b>H₂O₂</b> üretir, sonra onu suya çevirir']]))
    k.h3('Bitki ve hayvan hücresi; hücre duvarı ve hücre zarı')
    add('<p>Bitki ve mantar hücrelerinde hayvan hücresindeki organellerin çoğu vardır ama <b>lizozom yoktur</b>; yerine lizozomun birçok işini gören <b>büyük merkezi koful</b> vardır. Bitkide ayrıca <b>kloroplast</b> ve zarı güçlendiren <b>sert hücre duvarı</b> bulunur. '
        'Bitki hücre duvarı esas olarak <b>selülozdan</b> yapılır; hücre şeklinin ana belirleyicisidir ve hücreye sertlik verir. '
        'Hayvan hücresinin duvarı yoktur; dokulara güç ve sertlik veren <b>hücre dışı matriks</b> (collagen, glycoproteins vb.) ile çevrilidir.</p>'
        '<p>Hücre duvarı ve zarı benzer işler görür; ama <b>duvar zardan çok daha güçlüdür</b> ve hücreyi aşırı <b>hipotonik</b> (seyreltik) ortamda <b>patlamaktan (lysing)</b> korur. '
        '<b>Plazma zarı</b> ise madde giriş-çıkışını kontrol eder, iç dengeyi korur, hücre-hücre sinyalleşmesinde ve <b>hücre adezyonunda</b> görev alır. Zarlar hücre tipine göre farklılık gösterir (ör. disk şeklindeki <b>eritrosit</b>).</p>')
    add(KAV((T('Double-membrane organelles', 'çift zarlı organeller'), 'nucleus, mitochondrion, chloroplast'),
            (T('Non-membranous', 'zarsız'), 'ribosome, nucleolus'),
            (T('Plant vs animal cell', 'bitki ve hayvan'), 'bitki: duvar (selüloz), kloroplast, merkezi koful, lizozom yok; hayvan: duvar yok, ECM, lizozom var'),
            (T('Cell wall', 'hücre duvarı'), 'zardan güçlü; hipotonik ortamda patlamayı önler; şekil ve sertlik')))
    add(EXAM(
        ('Which organelles are bounded by two bilayer membranes?', ['nucleus, mitochondrion, chloroplast', 'lysosome, peroxisome, Golgi', 'ribosome and nucleolus', 'ER and vacuole'], 'A', 'Diğer bütün organeller tek zarlıdır.'),
        ('Plant cells lack lysosomes; instead they contain:', ['a large central vacuole', 'peroxisomes only', 'centrioles', 'a nucleolus'], 'A', 'Merkezi koful lizozomun birçok işini görür.'),
        ('Which statement about the cell wall is correct?', ['It is weaker than the plasma membrane', 'It protects cells from lysing in extremely hypotonic solutions', 'Animal cells have a cellulose wall', 'It regulates cell–cell signaling only'], 'B', 'Duvar zardan güçlüdür ve hipotonik ortamda patlamayı önler.'),
        ('Synthesis of lipids, Ca²⁺ storage and detoxification of drugs are functions of the:', ['rough ER', 'smooth ER', 'Golgi apparatus', 'nucleolus'], 'B', 'Düz ER.'),
        ('The inner mitochondrial membrane has infoldings called:', ['grana', 'thylakoids', 'cristae', 'cisternae'], 'C', 'Kristalar; kloroplastta tilakoit ve grana.'),
    ))

    # ================= 14 =================
    k.h2('14 · Lizozom, endozom, otofaji ve koful')
    k.h3('Lizozoma madde gelmesinin 3 yolu')
    add(TABLE(['Yol', 'Ne taşınır?', 'Nasıl?'], [
        [E('Endocytic pathway', 'endositik yol'), '<b>çözünür makromoleküller</b>', 'plazma zarındaki <b>coated pits</b> içeri çökerek (invagination) alır → endozom → lizozom'],
        [E('Phagocytic pathway', 'fagositik yol'), '<b>bütün hücreler</b> ve büyük, çözünmeyen parçacıklar (ör. bakteri)', 'plazma zarı parçacığı sarar ve içeri alır'],
        [E('Autophagic pathway', 'otofajik yol'), '<b>eskimiş organeller</b> ve toplu sitoplazma', '<b>autophagy</b> = "kendini yeme": yaşlı organel lizozomda yıkılır']]))
    add('<p><b>Endocytic pathway</b>: plazma zarının bir bölümü, sitozolik yüzü <b>clathrin</b> gibi proteinlerle kaplı bir <b>coated pit</b> halinde içeri çöker ve <b>clathrin-coated vesicle</b> olarak tomurcuklanır. '
        '<b>Endosomes</b>: plazma zarı proteinlerini ve hücre dışından çözünür maddeleri içeri alır, bunları ya zara <b>geri gönderir</b> ya da yıkım için <b>lizozoma</b> ayırır (early endosome → late endosome).</p>')
    add('<p><b>Lysosomes</b>: boyut ve şekilleri değişir, tipik bir hayvan hücresinde <b>birkaç yüz</b> tane olabilir. <b>Asidik</b> lümenli organellerdir; çeşitli <b>hydrolases</b> (lizozomal enzimler) içerir ve <b>hidrolizle</b> makromolekülleri parçalar: '
        'eskimiş zarlar ve organeller, gereksiz bileşenler ve hücrenin içeri aldığı maddeler. Bir şehrin <b>çöp sistemi</b> gibi aşırı ya da hantal makromoleküllerin birikmesini önler. Bazı zar proteinleri buradan plazma zarına geri dönüştürülür.</p>')
    add(TRAP('Tay-Sachs hastalığı (lizozomal enzim eksikliği)', '<p>Sinir hücrelerinde bol bulunan <b>gangliosides</b> adlı glikolipitlerin lizozomda yıkılmasının bir adımını yapan <b>tek bir enzimin</b> kusurundan olur (<b>sfingolipit katabolizması</b>). '
        'Sinir hücreleri, lipitle dolup şişmiş lizozomlarla büyür; etkilenen çocuklar <b>üçüncü yaş gününden önce</b> ölür. Gözde retinada makulada <b>kiraz kırmızısı leke</b> (cherry-red spot) görülür.</p>'))
    k.h3('Koful ve kesecikler (vacuoles and vesicles)')
    add('<p>Kofullar organik moleküllerden fazla suya kadar birçok madde tutabilir; bitki hücrelerinde bir ya da daha çok <b>büyük koful</b> vardır. Koful <b>su, iyon ve besin depolar</b>, makromolekülleri yıkar ve büyüme sırasında <b>hücrenin uzamasında</b> görev alır. '
        'Kofula ozmotik su akışı <b>turgor basıncını</b> oluşturur.</p>')
    add(KAV((T('Three pathways to lysosomes', 'lizozoma 3 yol'), 'endocytic (çözünür makromolekül), phagocytic (bütün hücre, bakteri), autophagic (eski organel)'),
            (T('Clathrin', 'klatrin'), 'coated pit ve kaplı keseciklerin sitozolik yüzünü kaplayan protein'),
            (T('Endosome', 'endozom'), 'içeri alınanı zara geri gönderir ya da lizozoma ayırır'),
            (T('Lysosome', 'lizozom'), 'asidik, hidrolazlarla dolu sindirim kesesi'),
            (T('Autophagy', 'otofaji'), '"kendini yeme": eskimiş organelin lizozomda yıkımı'),
            (T('Tay-Sachs', 'Tay-Sachs'), 'gangliyozit yıkım enzimi kusuru; kiraz kırmızısı leke; ölüm < 3 yaş')))
    add(EXAM(
        ('Worn-out organelles are delivered to lysosomes through the:', ['endocytic pathway', 'phagocytic pathway', 'autophagic pathway', 'secretory pathway'], 'C', 'Otofaji = kendini yeme.'),
        ('Whole cells and other large insoluble particles such as bacteria move to lysosomes through the:', ['phagocytic pathway', 'autophagic pathway', 'endocytic pathway', 'constitutive secretion'], 'A', 'Fagositik yol.'),
        ('The cytosolic face of a coated pit in the endocytic pathway is lined by:', ['actin', 'clathrin', 'collagen', 'catalase'], 'B', 'Klatrin kaplı kesecik.'),
        ('Tay-Sachs disease is caused by a defect in the lysosomal breakdown of:', ['glycogen', 'gangliosides', 'cholesterol', 'collagen'], 'B', 'Sinir hücrelerinde gangliyozit birikir; kiraz kırmızısı leke.'),
        ('The lumen of lysosomes is:', ['basic', 'neutral', 'acidic', 'filled with DNA'], 'C', 'Asidik; hidrolazlar burada çalışır.'),
        ('Osmotic flow of water into plant vacuoles generates:', ['turgor pressure', 'membrane potential', 'ATP', 'H2O2'], 'A', 'Turgor basıncı.'),
    ))

    # ================= 15 =================
    k.h2('15 · Peroksizomlar; HMP yolu ve G6PD eksikliği')
    add('<p><b>Peroxisomes</b>: kabaca küresel küçük organellerdir; <b>eritrositler hariç bütün hayvan hücrelerinde</b> ve birçok bitki hücresinde bulunur. Görevleri: çeşitli molekülleri <b>detoksifiye etmek</b> ve yağ asitlerini parçalayıp biyosentez için <b>asetil grupları</b> üretmek, '
        '<b>ATP üretmeden</b>.</p>')
    add(TABLE(['Enzim', 'Tepkime', 'Not'], [
        ['<b>Oxidases</b> (oksidazlar)', '2 H₂O + O₂ → 2 H₂O₂ (slayt)', 'moleküler oksijenle organik maddeleri oksitler; oluşan <b>hydrogen peroxide (H₂O₂)</b> aşındırıcıdır, <b>nötrofillerde bakterileri öldürür</b>'],
        ['<b>Catalase</b> (katalaz)', '2 H₂O₂ → 2 H₂O + O₂', 'peroksizomda <b>çok bol</b>; H₂O₂\'yi su ve oksijene yıkar'],
        ['<b>Glutathione peroxidase</b>', '2 H₂O₂ → 2 H₂O + O₂ (slayt)', '<b>eritrositte</b> (peroksizom yok) H₂O₂\'yi yıkar']]))
    add(TABLE(['Yağ asidi oksidasyonu', 'Nerede?', 'ATP?'], [
        ['<b>Very long fatty acids (VLFAs)</b>, <b>21 karbondan uzun</b>', '<b>peroksizomda</b> asetil gruplarına kadar kısaltılır, sonra mitokondriye gönderilir', '<b>peroksizomda ATP üretilmez</b>'],
        ['Kısa, orta ve uzun zincirli yağ asitleri', '<b>mitokondride beta-oksidasyon</b>', 'ATP üretilir']]))
    k.h3('HMP (hexose monophosphate) shunt ve G6PD eksikliği')
    add('<p>Hücrenin <b>NADPH</b>\'e ihtiyacı vardır; NADPH\'yi <b>HMP shunt</b> sağlar. NADPH\'nin görevleri: biyosentez için şeker üretmek (nükleotitler için <b>ribose 5-phosphate</b>), '
        '<b>reaktif oksijen türlerine (ROS)</b> karşı korumak için <b>indirgenmiş glutatyon</b> stokunu korumak, <b>polimorfonükleer lökositlerde (PMN) bakteri öldürme</b>.</p>'
        '<p><b>Glucose 6-phosphate dehydrogenase (G6PD) deficiency</b>: Kırmızı kan hücreleri çok oksijen taşıdığı için kendiliğinden <b>ROS</b> üretmeye yatkındır. Peroksitler eritrositte <b>glutathione peroxidase / glutathione reductase</b> sistemiyle hızla yok edilir; '
        'glutatyon redüktazın ihtiyaç duyduğu <b>NADPH</b> eritrositte <b>HMP shunt</b>\'tan gelir. G6PD eksikse oksidan stres sonucu:</p>'
        '<ul><li><b>Hemoglobin denatürasyonu</b>: hemoglobin çöker → <b>Heinz bodies</b></li><li><b>Zar hasarı</b>: zar lipitlerinin peroksidasyonu → zar zayıflar → <b>hemoliz, hemolitik anemi</b></li>'
        '<li><b>Hemoliz krizini tetikleyenler</b>: bazı <b>ilaçlar</b>, <b>bakla (fava beans)</b> yemek (bazı hastalarda), ağır enfeksiyonlar (sıklıkla viral/bakteriyel zatürre) ya da enfeksiyöz hepatit, <b>diyabetik ketoasidoz</b></li></ul>')
    add(KAV((T('Peroxisome', 'peroksizom'), 'detoksifikasyon + VLFA yıkımı; ATP üretmez; eritrositte yok'),
            (T('Catalase', 'katalaz'), '2 H₂O₂ → 2 H₂O + O₂; peroksizomda bol'),
            (T('VLFA', 'çok uzun zincirli yağ asidi'), '> 21 C; peroksizomda asetile kadar kısalır, sonra mitokondri'),
            (T('HMP shunt', 'HMP yolu'), 'NADPH ve riboz 5-fosfat sağlar'),
            (T('G6PD deficiency', 'G6PD eksikliği'), 'NADPH yetersiz → ROS → Heinz cisimcikleri, hemolitik anemi; bakla, ilaç, enfeksiyon tetikler')))
    add(EXAM(
        ('Which cells do NOT contain peroxisomes?', ['hepatocytes', 'erythrocytes', 'neurons', 'fibroblasts'], 'B', 'Eritrositler hariç bütün hayvan hücreleri.'),
        ('The enzyme abundant in peroxisomes that degrades hydrogen peroxide to water and oxygen is:', ['catalase', 'oxidase', 'hydrolase', 'ATP synthase'], 'A', 'Katalaz.'),
        ('Very long fatty acids (over 21 carbons) are first oxidized in:', ['mitochondria', 'peroxisomes', 'lysosomes', 'the Golgi'], 'B', 'Peroksizomda asetile kadar kısalır; ATP üretilmez.'),
        ('In erythrocytes, the NADPH required by glutathione reductase is supplied by the:', ['Krebs cycle', 'HMP shunt', 'electron transport chain', 'urea cycle'], 'B', 'HMP yolu.'),
        ('In G6PD deficiency, hemoglobin denaturation produces:', ['Heinz bodies', 'Barr bodies', 'inclusion bodies of I-cell', 'lipid rafts'], 'A', 'Heinz cisimcikleri; zar hasarı → hemolitik anemi.'),
        ('Which of the following can trigger a hemolytic crisis in G6PD deficiency?', ['ingestion of fava beans', 'drinking water', 'vitamin C deficiency only', 'exercise only'], 'A', 'İlaçlar, bakla, enfeksiyonlar, diyabetik ketoasidoz.'),
    ))

    # ================= 16 =================
    k.h2('16 · ER, ribozomlar, protein hedefleme ve Golgi')
    k.h3('Endoplazmik retikulum (ER)')
    add('<p>Ökaryot hücredeki <b>en büyük zar</b> genellikle <b>endoplasmic reticulum</b>\'u çevreler: <b>cisternae</b> denen kapalı, yassı, zarla çevrili keselerden oluşan geniş bir ağ. Hücredeki bütün zar dokusunun yaklaşık <b>yarısını</b> oluşturur; '
        'zar ve protein sentezinin yeridir. Bir yol ağı gibidir: ürünler üretilir ve yollarla gereken yere taşınır.</p>')
    add(TABLE(['', 'Görev'], [
        [E('Smooth ER', 'düz ER'), '<b>lipit sentezler</b>, bazı hidrofobik bileşikleri <b>detoksifiye eder</b>'],
        [E('Rough ER', 'granüllü ER'), '<b>salgı proteinleri</b>, <b>lizozomal proteinler</b> ve bazı zarların sentezi, işlenmesi ve ayrılması']]))
    add('<p><b>Ribosomes</b>: <b>zarsızdır</b>, <b>RNA ve proteinden</b> yapılır; <b>protein sentezi</b> yeridir (amino asitler polipeptide bağlanır). Sitoplazmada serbest ya da granüllü ER\'ye ve çekirdeğe bağlı olabilir. '
        'Çekirdek için "işçilik" yapar: DNA planlarının kopyası olan RNA ile amino asitleri bir araya getirip proteini kurar.</p>')
    k.h3('Protein hedefleme: serbest mi, bağlı ribozom mu?')
    add('<p>Ökaryot çekirdek genlerinin <b>bütün çevirisi sitoplazmadaki serbest ribozomlarda başlar</b>; ama yapılan protein başka bir yere ait olabilir. Proteinin nereye gideceğini <b>sinyaller</b> belirler:</p>')
    add(TABLE(['', E('Bound ribosomes', 'ER\'ye bağlı ribozomlar'), E('Free ribosomes', 'serbest ribozomlar')], [
        ['Ne zaman?', 'proteinde <b>N-terminal hidrofobik sinyal dizisi (leader sequence)</b> varsa ribozom ER\'ye bağlanır', 'proteinde leader sequence <b>yoksa</b> ribozom serbest kalır'],
        ['Hangi proteinler?', '<b>salgılanan</b>, <b>plazma zarı</b> ve <b>lizozomal</b> proteinler', 'sitozolde kalan proteinler; etiket varsa <b>çekirdek, mitokondri ya da peroksizoma</b> gider'],
        ['Yol', 'ER lümeni → Golgi → salgı / zar / lizozom', 'sitozol (ya da etiketine göre organel)']]))
    add(CHAIN([('Ribosome + mRNA', 'sinyal peptidi çıkar'), ('SRP', 'sinyali tanır'), ('SRP receptor', 'ER zarında'), ('Translocation complex', 'protein ER lümenine'), ('Signal peptide', 'kesilir'), ('ER lumen', 'glikozilasyon')],
              title='Proteinlerin ER\'ye hedeflenmesi (sinyal mekanizması)', note='SRP = signal recognition particle (sinyal tanıma parçacığı). Şema bu kağıt için çizildi.'))
    add(CHAIN([('Rough ER', 'sentez + glikozilasyon'), ('Transport vesicle', 'ribozomsuz kesecik'), ('Golgi: cis → medial → trans', 'işleme + ayırma'), ('Trans Golgi network', 'yönlendirme'), ('Lysosome', 'mannose-6-phosphate etiketli'), ('Secretion', 'constitutive ya da regulated')],
              title='Bağlı ribozomda yapılan proteinin yolculuğu', note='Lizozoma gidecek enzimler Golgi\'de mannoz-6-fosfat etiketi alır.'))
    k.h3('Golgi aygıtı ve kesecikler')
    add('<p>Golgi, granüllü ER\'de yapılan <b>salgı, lizozom ve zar proteinlerini işler ve ayırır</b>; bir <b>postane</b> gibi ER ve ribozomlarda yapılan ürünleri hücrenin geri kalanına gönderir. '
        'Protein sentezlendikten hemen sonra çoğu, RER\'den tomurcuklanan <b>ribozomla kaplı olmayan</b> küçük <b>transport vesicles</b> ile Golgi\'ye gider. Golgi sisternaları <b>üç bölge</b>: <b>cis, medial, trans</b>; bir dizi işleme bölmesi gibi düzenlenmiştir.</p>')
    add(TABLE(['Golgi\'deki işlemler', 'Anlamı'], [
        ['<b>Glycosylation</b>', 'karbonhidrat ekleme (olgun glikoproteinlerdeki karmaşık şekerler; mannoz kalıntılarının kesilmesi = trimming)'],
        ['<b>Sulfation</b>', 'kükürt (sülfat) ekleme'],
        ['<b>Phosphorylation</b>', 'fosfat ekleme (ör. lizozomal enzimlerde mannoz fosforilasyonu)'],
        ['<b>Proteolysis</b>', 'peptit bağlarının kesilmesi'],
        ['<b>Sorting</b>', 'salgı ve zar proteinlerini son hedeflerine ayırma']]))
    add('<p><b>Secretory vesicles</b> salgı proteinlerini depolar ve plazma zarıyla kaynaşıp içeriğini dışarı bırakır. Hücreden salgı <b>iki şekilde</b> olur: <b>constitutive</b> (sürekli) ya da <b>regulated</b> (sinyalle düzenlenen). '
        'Örnek: sıçan hipofizinde hormon salgılayan hücre: RER ribozomlarında yapılan hormon kesecikle Golgi\'ye, oradan plazma zarına gider.</p>')
    add(TRAP('I-cell disease: mannoz fosforilasyonu bozulursa', '<p>Lizozomal enzimler Golgi\'ye vardığında oligosakkarit zincirlerindeki belirli <b>mannoz kalıntıları fosforillenir</b> (<b>mannose-6-phosphate</b> etiketi). Bu, enzimleri <b>salgı yolundan çıkarıp lizozoma yönlendiren kritik olaydır</b>. '
        'Bu fosforilasyonu bozan genetik kusurlar <b>I-cell disease</b> yapar (<b>otozomal çekinik</b>): lizozomal enzimler <b>hücre dışına salınır</b>, hücrede <b>inclusion bodies</b> birikir. '
        'Bulgular: kaba yüz görünümü, diş eti hiperplazisi, büyük dil, kraniyofasiyal anomaliler, eklem hareketsizliği, çarpık ayak, pençe el, skolyoz, <b>ağır psikomotor gerilik</b>, yavaş büyüme; kalp-solunum yetmezliğiyle ölüm genellikle ilk 10 yılda (slaytın bir yerinde <b>5–8 yaş</b>).</p>'))
    add(KAV((T('Signal (leader) sequence', 'sinyal dizisi'), 'N-terminal hidrofobik dizi → ribozom ER\'ye bağlanır'),
            (T('Bound ribosome products', 'bağlı ribozom ürünleri'), 'salgı, plazma zarı, lizozom proteinleri'),
            (T('Free ribosome products', 'serbest ribozom ürünleri'), 'sitozol; etiketle çekirdek, mitokondri, peroksizom'),
            (T('SRP', 'sinyal tanıma parçacığı'), 'sinyal peptidini tanıyıp ribozomu ER\'deki SRP reseptörüne getirir'),
            (T('Golgi regions', 'Golgi bölgeleri'), 'cis, medial, trans'),
            (T('Mannose-6-phosphate', 'mannoz-6-fosfat'), 'Golgi\'de lizozomal enzim etiketi'),
            (T('I-cell disease', 'I-hücre hastalığı'), 'M6P etiketi yok → enzimler dışarı salınır, inclusion bodies; otozomal çekinik'),
            (T('Secretion types', 'salgı tipleri'), 'constitutive (sürekli), regulated (düzenli)')))
    add(EXAM(
        ('Ribosomes bind to the endoplasmic reticulum when the protein they are synthesizing contains:', ['a C-terminal KDEL sequence', 'an N-terminal hydrophobic signal (leader) sequence', 'a mannose-6-phosphate tag', 'a nuclear localization signal only'], 'B', 'N-terminal hidrofobik sinyal dizisi.'),
        ('Which proteins are synthesized on ER-bound ribosomes?', ['cytosolic enzymes', 'secreted, plasma membrane and lysosomal proteins', 'mitochondrial matrix proteins only', 'histones'], 'B', 'Salgı, plazma zarı ve lizozom proteinleri.'),
        ('Proteins synthesized on free ribosomes remain in the cytosol unless they contain a tag directing them to the:', ['Golgi, lysosome, plasma membrane', 'nucleus, mitochondria, or peroxisomes', 'ER lumen', 'extracellular space'], 'B', 'Serbest ribozom ürünleri.'),
        ('Lysosomal enzymes are directed to lysosomes by:', ['phosphorylation of mannose residues in the Golgi (mannose-6-phosphate)', 'sulfation in the ER', 'ubiquitination in the cytosol', 'a nuclear pore signal'], 'A', 'M6P etiketi.'),
        ('In I-cell disease:', ['lysosomal enzymes are released into the extracellular space and inclusion bodies accumulate', 'gangliosides accumulate in neurons with a cherry-red spot', 'hemoglobin forms Heinz bodies', 'cholesterol is absent from membranes'], 'A', 'Fosforilasyon kusuru; otozomal çekinik.'),
        ('The three defined regions of the Golgi stack are:', ['cis, medial, trans', 'outer, inner, matrix', 'rough, smooth, transitional', 'early, late, recycling'], 'A', 'Cis, medial, trans.'),
        ('Proteins secreted from the cell are released in two ways:', ['active and passive', 'constitutive and regulated', 'endocytic and phagocytic', 'symport and antiport'], 'B', 'Sürekli ve düzenli salgı.'),
        ('Which process in the Golgi refers to cleavage of peptide bonds?', ['glycosylation', 'sulfation', 'phosphorylation', 'proteolysis'], 'D', 'Proteoliz.'),
    ))

    # ================= 17 =================
    k.h2('17 · Çekirdek, çekirdekçik; mitokondri ve kloroplasta giriş')
    add(TABLE(['Çekirdeğin parçası', 'Özellik'], [
        [E('Nuclear envelope', 'çekirdek zarfı'), '<b>çift zar</b> (her biri fosfolipit çift katmanı, birçok protein içerir); iç ve dış zar çok sayıda <b>nuclear pore</b>\'da kaynaşır (çekirdek–sitozol madde geçişi); <b>iç zar</b> çekirdeği tanımlar; <b>dış zar granüllü ER ile devamlıdır</b>'],
        [E('Chromosomes / chromatin', 'kromozom / kromatin'), 'DNA + proteinler; kromozomlar <b>doğrusal</b>; çekirdek kromatinle dolu'],
        [E('Nucleolus', 'çekirdekçik'), 'çekirdeğin <b>zarla çevrili olmayan</b> alt bölmesi; hücrenin <b>rRNA</b>\'sının çoğu burada yapılır'],
        [E('Heterochromatin', 'heterokromatin'), 'çekirdekçik dışında koyu boyanan bölgeler']]))
    add('<p>Çekirdeğin görevleri: kalıtsal bilgiyi taşır ve protein sentezi yoluyla hücrenin işlerini sürekli etkiler ("<b>control center</b>", hücrenin "beyni"); ökaryotta DNA\'yı <b>yalıtır</b>; bölünen hücrelerde <b>mRNA ve tRNA sentezi</b> yeridir; '
        'DNA\'yı plan olarak kullanıp protein üretimini yönetir. Hayvan hücresinde <b>en büyük organeldir</b>.</p>')
    k.h3('Mitokondri (ayrıntısı Bölüm 18\'de)')
    add('<p>Mitokondriler bitki ve hayvan hücrelerinde bulunur, <b>hücresel solunum</b> yeridir. Çoğu ökaryot hücrede çok sayıdadır (sitoplazma hacminin <b>%25</b>\'ine kadar); büyüklükte yalnız <b>çekirdek, koful ve kloroplast</b> onu geçer. '
        '<b>Çift zarla</b> çevrilidir ve glikoz ile yağ asitlerini oksitleyerek <b>ATP</b> üretir; <b>kendi DNA\'sı</b> vardır.</p>')
    add(TABLE(['', E('Outer membrane', 'dış zar'), E('Inner membrane', 'iç zar')], [
        ['Bileşim', '<b>yarı lipit, yarı protein</b>', '<b>%20 lipit, %80 protein</b>'],
        ['Geçirgenlik', '<b>çok geçirgen</b> (10.000 daltona kadar)', '<b>çok daha az geçirgen</b>'],
        ['Şekil', 'düz', 'çok kıvrımlı: <b>cristae</b>, merkezdeki <b>matrix</b>\'e uzanır; yüzey alanını artırır']]))
    add('<p>İç zardaki ve matriksteki enzimler şeker ve lipit oksidasyonunun son evrelerini <b>ATP sentezine bağlı</b> olarak yapar. <b>Acetyl-CoA</b>\'nın ana görevi asetil grubunu <b>sitrik asit döngüsüne (Krebs)</b> taşımaktır. '
        '<b>Apoptozda</b>: proapoptotik proteinler mitokondri zarına girip <b>por</b> açar; <b>cytochrome c</b> zarlar arası boşluktan sitozole çıkar ve hücreyi apoptotik ölüme götüren biyokimyasal kaskadı başlatır. '
        'Mitokondri genlerindeki (<b>37 gen</b>) mutasyonlar hastalık yapabilir; ama mitokondri proteinlerinin <b>çoğu çekirdek DNA\'sında</b> kodlanır. Mitokondriler bakteriler gibi <b>bölünerek (fission)</b> çoğalır; '
        'yutulmuş bakterilerden geldiği düşünülür; çoğu çok hücreli canlıda <b>mtDNA anneden</b> kalıtılır.</p>')
    k.h3('Kloroplast')
    add('<p>Kloroplastlar yalnız <b>bitki hücrelerinde</b> (ve yeşil alglerde) bulunur; kofullar dışında bitki hücresinin <b>en büyük ve en karakteristik</b> organelidir. <b>Fotosentez</b>: CO₂, su ve güneş ışığıyla <b>glikoz</b> şeklinde enerji üretir (bitkiyi yiyen heterotroflar için de). '
        'Çift zarlıdır; içteki zarlı keseler (<b>thylakoids</b>) yığınlar (<b>grana</b>) halinde <b>stroma</b> içinde durur.</p>')
    add(TIP('🔗 Mitokondri ve kloroplastın ortak yanları', '<ul><li>ATP oluşturma mekanizmaları benzer</li><li>Hücre içinde sık sık yer değiştirir</li><li><b>Kendi DNA\'ları</b> vardır; bu DNA bazı kilit proteinleri kodlar ve bunlar organelin <b>kendi ribozomlarında</b> yapılır; ama proteinlerin çoğu çekirdek DNA\'sında kodlanıp sitozolde sentezlenir</li></ul>'))
    add('<p><b>Hücre iskeleti</b> (ayrıntısı ilgili bölümde): zarları destekleyen, hücreye şekil ve düzen veren, hareket ve bölünmede (mitoz) görev alan lif ağları. Üç lif sistemi: <b>intermediate filaments</b>, <b>microtubules</b>, <b>microfilaments</b>; üçü de şekil ve harekete katkıda bulunur.</p>')
    add(KAV((T('Nuclear envelope', 'çekirdek zarfı'), 'çift zar + porlar; dış zar RER ile devamlı'),
            (T('Nucleolus', 'çekirdekçik'), 'zarsız; rRNA sentezi'),
            (T('Mitochondrial membranes', 'mitokondri zarları'), 'dış: yarı lipit yarı protein, çok geçirgen · iç: %20 lipit %80 protein, az geçirgen, kristalar'),
            (T('Cytochrome c', 'sitokrom c'), 'apoptozda zarlar arası boşluktan sitozole çıkar → kaskad'),
            (T('mtDNA', 'mitokondri DNA'), '37 gen; anneden kalıtılır; proteinlerin çoğu yine de çekirdek DNA\'sında'),
            (T('Thylakoids / grana / stroma', 'tilakoit / grana / stroma'), 'kloroplastın iç yapısı')))
    add(EXAM(
        ('The outer nuclear membrane is continuous with the:', ['Golgi apparatus', 'rough endoplasmic reticulum', 'plasma membrane', 'mitochondrial membrane'], 'B', 'Dış çekirdek zarı RER ile devamlı.'),
        ('Most of the cell\'s ribosomal RNA is synthesized in the:', ['nucleolus', 'cytosol', 'Golgi', 'mitochondrial matrix'], 'A', 'Çekirdekçik; zarla çevrili değildir.'),
        ('The inner mitochondrial membrane is composed of approximately:', ['50% lipid, 50% protein', '20% lipid, 80% protein', '80% lipid, 20% protein', '100% lipid'], 'B', 'İç zar protein açısından zengin ve az geçirgen.'),
        ('During apoptosis, which protein leaves the intermembrane space of mitochondria and enters the cytosol?', ['catalase', 'cytochrome c', 'clathrin', 'actin'], 'B', 'Sitokrom c kaskadı başlatır.'),
        ('In most multicellular organisms, mitochondrial DNA is inherited:', ['paternally', 'maternally', 'from both parents equally', 'not inherited'], 'B', 'Anneden.'),
        ('Mitochondria replicate by:', ['mitosis', 'meiosis', 'fission, as do bacteria', 'budding from the ER'], 'C', 'Bakteriler gibi bölünme.'),
        ('The outer mitochondrial membrane is highly permeable to molecules up to about:', ['100 daltons', '10,000 daltons', '1,000,000 daltons', 'it is impermeable'], 'B', '10.000 dalton.'),
    ))
