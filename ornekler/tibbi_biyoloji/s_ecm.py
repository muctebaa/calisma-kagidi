"""Bölüm 27–28: Extracellular Matrix (Prof. Dr. A. Kevser Özden, 45 slayt; metin katmanından)."""
from ortak import E, T

BOLUMLER = [('27', 'Hücre dışı matriks: görevleri, kolajen, elastik lifler, laminin, fibronektin, MMP', 'ECM (A. K. Özden)'),
            ('28', 'Proteoglikanlar ve glikozaminoglikanlar (GAG), hiyalüronik asit, agrekan', 'ECM')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM

    # ================= 27 =================
    k.h2('27 · Hücre dışı matriks (Extracellular Matrix, ECM)')
    add('<p>Çok hücreli canlının özellikleri: <b>iş bölümü</b>, <b>özelleşme</b>, <b>doku ve organlar</b>, <b>hücreler arası iletişim</b>. Hücre–hücre etkileşimleri: fiziksel temas, hücre adezyon molekülleri, hücre–ECM bağlantıları, hücre yüzey molekülleri (desmozom, gap junction). '
        '<b>Hücre zarı sınır değildir</b>: hücreyi saran ve koruyan <b>etkin matriks</b> ECM\'dir.</p>')
    add(TABLE(['ECM\'nin görevleri'], [['<b>Mekanik destek</b>'], ['<b>Embriyonik gelişim</b>'], ['<b>Hücre göçü</b>'], ['<b>Büyüme faktörlerini yönlendirme</b> (doku onarımı)'],
                                       ['Bileşimi bulunduğu dokuya göre <b>değişir</b>'], ['Hücre işlerini düzenler (<b>hücre dışı sinyaller</b>)']]))
    add(TABLE(['ECM bileşeni (protein + karbonhidrat)', 'Örnek'], [
        ['I. Çözünmeyen, su tutmayan bileşenler: <b>lif yapan</b> yapısal proteinler', '<b>collagen</b>, <b>elastin</b>'],
        ['II. Çözünen, kolay su tutan bileşenler', '<b>proteoglycans</b>: hiyalüronik asit ve diğerleri'],
        ['III. <b>Adhesive glycoproteins</b> (yapıştırıcı glikoproteinler)', '<b>fibronectin</b>, <b>fibrillin</b>, <b>laminin</b>, osteonectin, vitronectin']]))
    add('<p>Protein ve glikoprotein bileşenler karmaşık üç boyutlu yapılar (konformasyon) oluşturur, ECM\'nin <b>sağlam ve esnek</b> yapısını kurar; mutant formları hastalıklara yol açar.</p>')
    k.h3('Kolajen (Collagen)')
    add('<p><b>Vücuttaki en bol proteindir</b>; <b>bağ dokusunun ana bileşenidir</b>. <b>Fibroblastlar</b> ve bazı epitel hücreleri tarafından sentezlenip ECM\'ye salgılanır. Sentezi, bir hidroksilazın kofaktörü olarak <b>C vitamini</b> gerektirir. '
        'Sağlam <b>üçlü sarmal</b> yapı (kolajen lifleri) oluşturur. Tipleri: <b>lifli (fibrous)</b>, <b>tabaka oluşturan (layer forming)</b>, <b>bağlayıcı</b> (lifli kolajeni kararlı kılar), <b>transmembran</b>.</p>')
    add(TABLE(['Lifli kolajen', 'Özellik'], [
        ['Birim', '<b>300 nm</b> üçlü sarmal'], ['Zincirler', '<b>iki α1 + bir α2</b> zinciri'], ['Bileşim', '<b>glisin ve lizin</b> yüksek'],
        ['Hidroksilasyon', 'üçlü sarmal için <b>lizin hidroksilasyonu</b> şart; bunun için <b>C vitamini</b> gerekir'], ['Kararlılık', 'kovalent bağlar'],
        ['Mikroskop', 'tipik <b>çizgili görünüm</b>, aralık <b>67 nm</b>']]))
    add(TABLE(['Kolajen tipi', 'Nerede?'], [
        ['<b>Tip I</b>', 'deri, tendon, damarlar, <b>kemik</b>, sklera, dentin'], ['<b>Tip II</b>', '<b>kıkırdak</b>'],
        ['<b>Tip IV</b>', '<b>bazal membran</b> (epitel ve endotel); tabaka oluşturan kolajen: korneada Descemet zarı, böbrekte Bowman kapsülü'], ['<b>Tip XII</b>', 'ligament, diş minesi vb.']]))
    add(TRAP('Kolajen hastalıkları', '<p><b>Scurvy</b> (skorbüt): lizinler <b>lizin hidroksilaz</b> ile hidroksillenir; bu enzim <b>C vitaminini kofaktör</b> olarak kullanır → C vitamini eksikliğinde kolajen bozulur (dişeti kanaması). '
        '<b>Ehlers-Danlos sendromu</b>: kolajen kusuru. Kolajenle ilgili otoimmün hastalıklar: <b>sistemik lupus eritematozus</b>, <b>romatoid artrit</b>.</p>'))
    k.h3('Elastik lifler, laminin, fibronektin')
    add(TABLE(['Bileşen', 'Özellik'], [
        [E('Elastic fibers', 'elastik lifler'), 'bütün vücutta, en çok <b>deride</b>; <b>fibrilin ve elastinden</b> oluşur; <b>yalnız fibroblastlar</b> sentezler; sentezi <b>ergenlikte tamamlanır</b>'],
        [E('Fibrillin', 'fibrilin'), 'bazal laminada, düzlemsel yapı; <b>fibrilin-1 mutasyonu → Marfan sendromu</b>'],
        [E('Elastin', 'elastin'), 'çoğunlukla bağ dokusu ECM\'sinde; fibroblastlar yapar; <b>hidrofobik bölümleri halkalarla</b> esneklik verir: <b>ELASTICITY</b>'],
        [E('Laminin', 'laminin'), '<b>haç şeklinde</b>; ECM bileşenlerini birleştirir; <b>embriyonun ana proteinlerinden</b>; <b>bazal laminanın yapıştırıcı molekülü</b>; <b>üç polipeptit</b> asimetrik sarılır, <b>disülfit bağlarıyla</b> bağlanır'],
        [E('Fibronectin', 'fibronektin'), '<b>glikoprotein</b>; hücrelere <b>RGD</b> dizisiyle bağlanır (hücredeki <b>integrin</b> RGD\'yi tanır), sonra <b>focal adhesion kinase</b> ile hücre içine sinyal verir']]))
    k.h3('Matriks proteinlerinin sentezi ve yıkımı')
    add('<p>Matriks proteinleri özellikle <b>fibroblastlarca</b> sentezlenip ECM\'ye salgılanır; yine hücrelerden salgılanan enzimlerle yıkılır: <b>cysteine proteases</b>, <b>acid proteases</b> (katepsinler), <b>serine proteases</b> (<b>tPA, uPA</b>: plazminojen aktivatörleri), <b>matrix metalloproteases (MMPs)</b>. '
        '<b>MMP\'ler</b> aktif bölgelerinde <b>çinko</b> bulunan, ECM ve bazal membran bileşenlerini yıkan enzimlerdir; doku yenilenmesi, morfogenez, hasarlı doku onarımı ve gelişimde görev alır. '
        'MMP\'ler <b>kanser ilerlemesinde</b> de rol oynar: <b>tümör invazyonu, anjiyogenez, metastaz</b>; tümör hücreleri, makrofajlar ve inflamasyon hücreleri MMP salgılar. Sistein, serin ve asit proteazlar da tümör metastazında görevlidir.</p>')
    add(KAV((T('ECM', 'hücre dışı matriks'), 'hücreyi saran etkin matriks; destek, gelişim, göç, büyüme faktörü, sinyal'),
            (T('Collagen', 'kolajen'), 'en bol protein; üçlü sarmal (2 α1 + 1 α2); glisin, lizin; C vitamini; 67 nm çizgi'),
            (T('Collagen types', 'kolajen tipleri'), 'I: deri, kemik, tendon · II: kıkırdak · IV: bazal membran · XII: ligament'),
            (T('Scurvy', 'skorbüt'), 'C vitamini eksikliği → lizin hidroksilaz çalışmaz'),
            (T('Fibrillin-1', 'fibrilin-1'), 'mutasyonu Marfan sendromu'),
            (T('Laminin', 'laminin'), 'haç şekli, 3 polipeptit, bazal laminanın yapıştırıcısı'),
            (T('Fibronectin', 'fibronektin'), 'glikoprotein; RGD ile integrine bağlanır'),
            (T('MMPs', 'matriks metalloproteazlar'), 'çinkolu, ECM yıkar; doku onarımı ve metastaz')))
    add(EXAM(
        ('The most abundant protein in the body is:', ['elastin', 'collagen', 'fibronectin', 'albumin'], 'B', 'Bağ dokusunun ana bileşeni.'),
        ('Collagen synthesis requires which vitamin as a cofactor of a hydroxylase?', ['vitamin A', 'vitamin C', 'vitamin D', 'vitamin K'], 'B', 'Eksikliği skorbüt.'),
        ('A fibrous collagen unit is a triple helix composed of:', ['three α1 chains', 'two α1 and one α2 chains', 'one α1 and two α2 chains', 'two β chains'], 'B', '300 nm, 67 nm çizgilenme.'),
        ('Type II collagen is found mainly in:', ['skin', 'cartilage', 'basal membrane', 'ligament'], 'B', 'Tip IV bazal membran; tip I deri, kemik.'),
        ('A mutation in fibrillin-1 causes:', ['scurvy', 'Marfan syndrome', 'Ehlers-Danlos syndrome', 'Tay-Sachs disease'], 'B', 'Marfan.'),
        ('Elastic fibers are composed of:', ['collagen and laminin', 'fibrillin and elastin', 'actin and myosin', 'keratin and vimentin'], 'B', 'Yalnız fibroblastlar sentezler; ergenlikte tamamlanır.'),
        ('Fibronectin binds cells through its ___ sequence, which is recognized by integrins.', ['KDEL', 'RGD', 'NPA', 'PIA'], 'B', 'Sonra FAK ile sinyal.'),
        ('Matrix metalloproteases contain ___ in their active site.', ['iron', 'zinc', 'copper', 'magnesium'], 'B', 'Çinko; doku yenilenmesi ve metastaz.'),
        ('Which ECM protein has a cross-like structure and is the adhesive molecule of the basal lamina?', ['laminin', 'elastin', 'collagen type I', 'aggrecan'], 'A', 'Üç polipeptit, disülfit bağları.'),
    ))

    # ================= 28 =================
    k.h2('28 · Proteoglikanlar ve glikozaminoglikanlar (GAG)')
    add('<p><b>Proteoglycans</b> (mukopolisakkaritler) ECM\'nin <b>çözünen ve su tutan</b> molekülleridir: <b>protein + GAG</b> (glikozaminoglikan). GAG\'lar <b>tekrarlanan disakkarit birimlerinden</b> oluşur ve proteoglikanlar GAG kısmına göre gruplanır. '
        'Disakkaritin bir şekeri <b>amino şeker</b> (D-glukozamin ya da D-galaktozamin, genelde N-asetilli: GlcNAc, GalNAc), diğeri <b>asidik şeker</b>dir (D-glukuronik asit ya da onun C-5 epimeri L-iduronik asit; keratan sülfatta bunun yerine galaktoz).</p>')
    add(TIP('🦴 GAG neden kıkırdak için mükemmel?', '<p>Disakkaritlerden biri hep <b>sülfat grubu</b> taşır → <b>bol negatif yük</b> → <b>yüksek su tutma kapasitesi</b> → <b>yüksek viskozite</b>. Bu yüzden GAG "<b>kıkırdak için mükemmel bileşendir</b>".</p>'))
    add(TABLE(['GAG', 'Disakkarit birimi', 'Nerede?'], [
        ['<b>Hyaluronic acid</b> (hyaluronan)', 'D-glukuronik asit + N-asetilglukozamin', '<b>gözün vitröz sıvısı</b>, eklemlerde <b>sinovyal sıvı</b>, kıkırdak ECM\'si; embriyonun ECM\'si'],
        ['<b>Chondroitin sulphate</b>', 'D-glukuronik asit + N-asetilgalaktozamin', '<b>kıkırdak</b>, kalp kapakları'],
        ['<b>Dermatan sulphate</b>', 'D-glukuronik / L-iduronik asit + N-asetilgalaktozamin', '<b>deri</b>, damarlar, kalp kapakları'],
        ['<b>Heparin / heparan sulphate</b>', 'D-glukuronik / L-iduronik asit + D-glukozamin', '<b>bazal membranlar</b>, hücre yüzeyleri, <b>mast hücreleri</b>'],
        ['<b>Keratan sulphate</b>', 'D-galaktoz + N-asetilglukozamin', 'kondroitin sülfatla agregat yapar: <b>kornea</b>, kemik, kıkırdak']]))
    add(TRAP('Hiyalüronik asit neden farklı?', '<p><b>En yaygın</b> GAG\'dır; <b>proteine bağlı değildir</b> (proteoglikan değildir); <b>sülfat grubu yoktur</b>; <b>en yüksek su tutma</b> kapasitesine sahiptir; <b>kayganlaştırır</b> ve kuvvete direnç sağlar; '
        'embriyonun ECM\'sini doldurur; yarayı kayganlaştırarak <b>yara iyileşmesine</b> katılır; <b>hyaluronidase</b> ile yıkılır; küçük olduğu için <b>enjekte edilebilir</b>. Fibroblastlar sentezler.</p>'))
    add(TABLE(['Proteoglikan', 'Özellik'], [
        ['<b>Aggrecan</b> (agregat yapan)', 'kolajen lifleri ve proteoglikanlarla agregat oluşturur; <b>vücudun en büyük moleküllerinden</b>; çekirdek protein ~250.000, GAG kısmı ~<b>2 milyon dalton</b>; <b>kıkırdağa jöle kıvamı</b> verir'],
        ['Agregat yapmayanlar', 'ör. bazal laminada 20.000–40.000\'lik çekirdek proteine bağlı <b>heparan sülfat</b>; <b>tip IV kolajen</b>, laminin, nidogen, perlecan ile bazal laminaya bağlanır'],
        ['<b>Syndecan</b> (hücre yüzeyi proteoglikanı)', 'en önemlisi; hücre dışı kısmı <b>kolajen ve fibronektine</b>, sitoplazmik kısmı <b>hücre iskeleti ve sinyal</b> elemanlarına bağlanır']]))
    add('<p>Proteoglikanların da bir <b>turnover</b>\'ı (sentez/yıkım döngüsü) vardır: hiyalüronik asit fibroblastlarca sentezlenir, <b>hyaluronidase</b> ile yıkılır.</p>')
    add(KAV((T('Proteoglycan', 'proteoglikan'), 'protein + GAG; çözünür, su tutar'),
            (T('GAG', 'glikozaminoglikan'), 'tekrarlanan disakkarit; sülfat → negatif yük → su tutma, viskozite'),
            (T('Hyaluronic acid', 'hiyalüronik asit'), 'en yaygın; proteinsiz, sülfatsız; en yüksek su tutma; vitröz, sinovyal sıvı'),
            (T('Heparan sulphate', 'heparan sülfat'), 'bazal membran, hücre yüzeyi, mast hücresi'),
            (T('Aggrecan', 'agrekan'), 'kıkırdakta dev agregat; jöle kıvamı'),
            (T('Syndecan', 'sindekan'), 'hücre yüzeyi proteoglikanı; kolajen/fibronektin ↔ hücre iskeleti')))
    add(EXAM(
        ('Which glycosaminoglycan is NOT bound to a protein and does NOT contain a sulphate group?', ['chondroitin sulphate', 'heparan sulphate', 'hyaluronic acid', 'keratan sulphate'], 'C', 'En yüksek su tutma kapasitesi.'),
        ('Why are GAGs ideal components of cartilage?', ['they are hydrophobic', 'abundant negative charge gives high water absorbing capacity and viscosity', 'they contain no sugars', 'they form gap junctions'], 'B', 'Sülfat → negatif yük.'),
        ('Hyaluronic acid is found in the:', ['vitreous humor of the eye and synovial fluid', 'mitochondrial matrix', 'nucleolus', 'myelin sheath'], 'A', 'Ayrıca kıkırdak ECM\'si.'),
        ('Heparin and heparan sulphate are found in:', ['basal membranes, cell surfaces and mast cells', 'only in cornea', 'muscle sarcomeres', 'red blood cells only'], 'A', 'Bazal membran.'),
        ('Which proteoglycan forms huge aggregates and gives cartilage a jelly-like texture?', ['syndecan', 'aggrecan', 'perlecan', 'decorin'], 'B', 'GAG kısmı ~2 milyon dalton.'),
        ('The major cell surface proteoglycan that binds collagen and fibronectin is:', ['syndecan', 'aggrecan', 'laminin', 'fibrillin'], 'A', 'Sitoplazmik kısmı hücre iskeletine bağlanır.'),
        ('Hyaluronic acid is degraded by:', ['collagenase', 'hyaluronidase', 'catalase', 'lysozyme'], 'B', 'Fibroblastlar sentezler.'),
        ('Keratan sulphate contains ___ instead of a uronic acid.', ['galactose', 'glucose', 'iduronic acid', 'ribose'], 'A', 'D-galaktoz + N-asetilglukozamin.'),
    ))
