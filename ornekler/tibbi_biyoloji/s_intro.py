"""Bölüm 1–9: Introduction to Molecular Cell Biology (Dr. Selma Yılmaz) — tıbbı biyoloji.pdf, 126 sayfa."""
from ortak import E, T


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM, EZBER = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM, k.EZBER

    # ================= 1 =================
    k.h2('1 · Hücre ve yaşam: Molecular Cell Biology ne çalışır?')
    add('<p>' + E('Molecular Cell Biology', 'moleküler hücre biyolojisi') + ' birçok alanı birleştiren bir bilimdir: biyokimya, biyofizik, moleküler biyoloji, mikroskopi, genetik, fizyoloji, bilgisayar bilimi ve gelişim biyolojisi. '
        'Konusu hücrelerin <b>doğumu, yaşamı ve ölümüdür</b>; hücrelerin <b>benzerliği ve çeşitliliği</b> (unity and diversity) ile başlar. Ders kitapları: Lodish, Weaver, Lippincott, Alberts.</p>')
    k.h3('Canlılığı tanımlayan yetenekler (What do cells do?)')
    add(TABLE(['Özellik (slayt)', 'Türkçesi'], [
        [T('Order', 'düzen'), 'canlı düzenli bir yapıdır'],
        [T('Evolutionary adaptation', 'evrimsel uyum'), 'çevreye uyum sağlar'],
        [T('Response to the environment', 'çevreye yanıt'), 'uyarılara cevap verir'],
        [T('Reproduction', 'üreme'), 'çoğalır'],
        [T('Growth and development', 'büyüme ve gelişme'), 'büyür, gelişir'],
        [T('Energy processing', 'enerji işleme'), 'enerji alır ve dönüştürür'],
        [T('Regulation', 'düzenleme'), 'iç ortamını düzenler']]))
    add('<p>Tek hücreli canlılar bile bu özelliklerin <b>hepsini</b> gösterir; bu yüzden <b>hücre yaşamın temel birimidir</b> (the cell is the fundamental unit of life). '
        'Canlı olmak sadece düzen değil, düşman bir ortamda <b>düzen kurabilme ve koruyabilme</b> yeteneğidir: bunun için bir <b>plan</b>, planı uygulayacak bir <b>yönetim (will)</b> ve içeriden ve dışarıdan gelen bir <b>enerji</b> gerekir.</p>')
    add('<p><b>Hücre nedir?</b> Hücreler, yoğun bir kimyasal sulu çözeltiyle dolu, <b>zarla çevrili küçük bölmelerdir</b> (small membrane-bounded compartments filled with a concentrated aqueous solution of chemicals). '
        'En basit canlılar ikiye bölünerek çoğalan tek hücrelerdir; insan gibi gelişmiş canlılar ise özel işleri yapan hücre gruplarından oluşan <b>"hücresel şehirler"</b> gibidir. '
        'Hücreleri çalışmamızın amacı: <b>molekülerden nasıl yapıldıklarını</b> ve <b>insan gibi karmaşık bir organizmayı oluşturmak için nasıl işbirliği yaptıklarını</b> anlamaktır.</p>')
    k.h3('Modern hücre kuramı (Modern Cell Theory)')
    add(TABLE(['Madde', 'Açıklama'], [
        ['1', 'Bütün canlılar hücrelerden oluşur (all known living things are made up of cells).'],
        ['2', 'Hücre canlıların <b>yapısal ve işlevsel birimidir</b> (structural & functional unit).'],
        ['3', 'Hücreler <b>önceden var olan hücrelerin bölünmesiyle</b> oluşur (from pre-existing cells by division).'],
        ['4', 'Hücreler kalıtsal bilgiyi (<b>DNA</b>) taşır ve bölünmede bir sonraki hücreye aktarır.'],
        ['5', 'Hücrelerin kimyasal bileşimi temelde aynıdır: sadece <b>altı element</b> → <b>C, H, O, N, P, S</b>.'],
        ['6', 'Yaşamın enerji akışı (metabolizma ve biyokimya) hücrelerin <b>içinde</b> gerçekleşir.']]))
    add('<p>Klasik kuramın üç ilkesi ve sahipleri: <b>1)</b> Bütün canlılar bir ya da daha çok hücreden oluşur, <b>2)</b> hücre yaşamın temel birimidir (<b>1838–1839, Schleiden ve Schwann</b>); '
        '<b>3)</b> <i>Omnis cellula e cellula</i>: bütün hücreler başka hücrelerden gelir (<b>1858, Virchow</b>). Birleşik hücre kuramı (unified cell theory) da aynı üç ilkeyi söyler.</p>')
    k.h3('Hücreler ne iş yapar? (The Work of Cells: 7 madde)')
    add(TABLE(['#', 'İş', 'Nasıl?'], [
        ['1', 'Dış ortamdan ayrılır', E('Plasma membrane', 'plazma zarı') + ' ile'],
        ['2', 'Enerji üretir', E('ATP') + ': kimyasal enerjinin evrensel "para birimi"'],
        ['3', 'Kendi dış ortamını ve "yapıştırıcısını" üretir', E('Extracellular matrix', 'hücre dışı matriks') + ' proteinleri (ör. <b>collagen</b>), hücre yapışma molekülleri, gap junctions'],
        ['4', 'Şekil değiştirir ve hareket eder', E('Cytoskeletal filaments', 'hücre iskeleti lifleri') + ': üç tip protein lifi'],
        ['5', 'Bilgi algılar ve gönderir, gen ifadesini düzenler', 'sinyaller: küçük kimyasallar, gazlar, proteinler, ışık, mekanik hareket'],
        ['6', 'Büyür ve bölünür', E('Mitosis') + ' ve ' + E('meiosis') + '; ökaryot hücre döngüsü <b>4 evre</b>, <b>10–20 saat</b>'],
        ['7', 'Ölür', E('Apoptosis', 'programlı hücre ölümü') + ': ölen hücre kendini yok edecek proteinleri <b>kendisi üretir</b>']]))
    add(KAV((T('Cell', 'hücre'), 'Yoğun sulu kimyasal çözeltiyle dolu, zarla çevrili küçük bölme; yaşamın temel birimi'),
            (T('Six elements', 'altı element'), 'C, H, O, N, P, S: DNA, RNA ve proteinleri oluşturur'),
            (T('Omnis cellula e cellula', 'her hücre bir hücreden'), 'Virchow, 1858'),
            (T('Apoptosis', 'apoptoz'), 'Programlı hücre ölümü: hücre kendi yıkım proteinlerini üretir')))
    add(EXAM(
        ('Which of the following is NOT listed among the properties that define life?', ['Reproduction', 'Energy processing', 'Crystallization', 'Response to the environment'], 'C', 'Slayttaki 7 özellik: order, evolutionary adaptation, response to environment, reproduction, growth & development, energy processing, regulation. Kristalleşme (crystallization) canlılık özelliği değildir.'),
        ('According to the modern cell theory, cells are basically the same in chemical composition and are composed of just six elements. Which set is correct?', ['C, H, O, N, P, S', 'C, H, O, N, Fe, Ca', 'C, H, O, Na, K, Cl', 'C, H, N, Mg, P, S'], 'A', 'Altı element: karbon, hidrojen, oksijen, azot, fosfor, kükürt.'),
        ('"Omnis cellula e cellula" (all cells come from other cells) was stated by:', ['Schleiden', 'Schwann', 'Virchow', 'Hooke'], 'C', 'Rudolf Virchow, 1858.'),
        ('In programmed cell death (apoptosis):', ['the cell is always destroyed by bacteria', 'the dying cell produces proteins necessary for its own destruction', 'the cell divides into two daughter cells', 'the cell wall breaks down'], 'B', 'Apoptozda ölen hücre kendi yıkımı için gerekli proteinleri kendisi üretir.'),
        ('Which of the following is a major component of the extracellular matrix in most tissues?', ['Collagen', 'Hemoglobin', 'Glycogen', 'Insulin'], 'A', 'Slayt: Collagen is a major component of the extracellular matrix.'),
    ))

    # ================= 2 =================
    k.h2('2 · Hücre biyolojisinin tarihi: mikroskoptan DNA\'ya')
    add('<p>"<i>Science is, in essence, organized curiosity.</i>" (Bilim, özünde düzenli merakdır.) Bu bölüm sınavda en çok <b>"kim, ne zaman, ne buldu?"</b> diye sorulur; hoca tekrar sorularında da Leeuwenhoek, Schleiden, Schwann, Virchow, Garrod, Beadle ve Tatum\'un çalışmalarını soruyor.</p>')
    add(TABLE(['Yıl', 'Kim', 'Ne yaptı?'], [
        ['1500\'lerin sonu', 'Avrupa', 'ilk mercekler (kumaş kalitesine bakmak için)'],
        ['<b>1595</b>', '<b>Zacharias Jansen</b> (1585–1632), Hollandalı gözlükçü', 'ilk optik teleskop ve ilk gerçek <b>compound microscope</b> (bileşik mikroskop); babası Hans Jansen ile; üç iç içe tüp'],
        ['<b>1655</b> (slayt)', '<b>Robert Hooke</b>', 'mantarda (cork) ilk <b>"cells" (cellula)</b> tanımı <i>(genel bilgi: Micrographia 1665)</i>'],
        ['<b>1674</b>', '<b>Anton van Leeuwenhoek</b> (1632–1723), "<b>father of microbiology</b>"', 'el yapımı mikroskopla gölet suyunda <b>ilk canlı hücreler</b> (alg, Spirogyra); <b>animalcules</b> (küçük hayvancıklar), protistler, bakteri, sperm, kan hücreleri, nematod, rotifer; Royal Society\'ye mektuplar (kas lifi, kılcallarda kan akışı)'],
        ['1735', '<b>Carl Linnaeus</b> (1707–1778)', 'biyolojik sınıflandırma (iki alem: bitki, hayvan)'],
        ['1827', '<b>Karl von Baer</b>', 'memelilerin annenin yumurtalığından gelen <b>yumurtadan</b> geliştiğini buldu'],
        ['<b>1833</b>', '<b>Robert Brown</b>', 'orkide hücrelerinde <b>çekirdeği</b> (nucleus) tanımladı'],
        ['<b>1838</b>', '<b>Matthias Schleiden</b> (1804–1881), Alman hukukçu ve botanikçi', '<b>bütün bitkiler hücrelerden oluşur</b>'],
        ['<b>1839</b>', '<b>Schleiden ve Theodor Schwann</b> (1810–1882)', '<b>hücre kuramını</b> oluşturdular; Schwann: bütün hayvanlar hücrelerden oluşur, "<b>founder of modern histology</b>", Schwann hücreleri, pepsin'],
        ['<b>1858</b>', '<b>Rudolf Virchow</b> (1821–1902), "<b>father of modern pathology</b>"', '<b>Omnis cellula e cellula</b>; lösemi hücreleri, sosyal tıp ("Medicine is a social science…")'],
        ['1858 / 1859', '<b>Darwin</b> (1809–1882) ve <b>Wallace</b> (1823–1913)', '1858 Linnean Society\'de ortak sunum; 1859 <b>"The Origin of Species by Means of Natural Selection"</b>; Galápagos ispinozları: "survival of the fittest"'],
        ['<b>1865</b>', '<b>Gregor Mendel</b> (1822–1884), "<b>Father of Genetics</b>"', 'kalıtsal <b>"factors"</b> (bugün <b>genes</b>), <b>alleles</b>, kalıtım yasaları; bezelye: mor baskın, beyaz çekinik; F1 hep mor, F2\'de <b>3:1</b>'],
        ['<b>1869</b>', '<b>Friedrich Miescher</b>', 'akyuvar çekirdeklerinden <b>"nuclein"</b> (ana bileşeni <b>DNA</b>)'],
        ['<b>1879</b>', '<b>Walther Flemming</b> (1843–1905)', 'anilin boyalarıyla <b>chromatin</b>; kromozomlar ("renkli cisimler"), mitoz; kitap "Zellsubstanz, Kern und Zelltheilung" (1882)'],
        ['<b>1898</b>', '<b>Camillo Golgi</b>', '<b>Golgi apparatus</b>\'u tanımladı'],
        ['<b>1902</b>', '<b>Sutton ve Boveri</b>', 'bağımsız olarak <b>kromozom kalıtım kuramı</b>'],
        ['<b>1902</b>', '<b>Archibald Garrod</b> (1857–1936)', '<b>alkaptonüri</b> çekinik kalıtılır; "kusurlu gen → kusurlu enzim"; "one gene–one enzyme" fikrinin öncüsü'],
        ['<b>1910 / 1915</b>', '<b>Thomas Morgan</b> (1866–1945)', '1910 meyve sineği (<b>Drosophila melanogaster</b>) ile kromozom kuramının ilk kesin kanıtı; 1915 "The Mechanism of Mendelian Heredity": <b>kromozomlar genleri taşır</b>; Nobel 1933'],
        ['1920\'ler', '<b>Lewis Stadler</b> (1896–1954)', 'mısır ve arpada radyasyonun mutasyon etkisi'],
        ['<b>1925</b>', '<b>Theodor Svedberg</b> (1884–1974)', '<b>ultracentrifuge</b> (~10⁶ g); boyut, ağırlık, yoğunluk; Nobel Kimya <b>1926</b>'],
        ['<b>1928</b>', '<b>Frederick Griffith</b> (1879–1941)', 'bakteriyel <b>transformation</b>: "transforming principle"'],
        ['<b>1944</b>', '<b>Oswald Avery</b>, MacLeod, McCarty', '<b>genler DNA\'dan yapılmıştır</b>; kalıtsal özelliği DNA taşır'],
        ['<b>1946</b>', '<b>Hermann J. Muller</b> (1890–1967)', 'Drosophila\'da <b>radyasyonla mutasyon</b> (mutagenesis); Nobel 1946; nükleer serpinti uyarıları'],
        ['<b>1953</b>', '<b>Watson ve Crick</b> (Franklin ve Wilkins\'in verileriyle)', 'DNA\'nın <b>çift sarmal</b> yapısı; Franklin\'in X-ışını kırınımındaki "X" sarmalı gösterir; Watson, Crick, Wilkins Nobel <b>1962</b>'],
        ['<b>1957</b>', '<b>Hoagland ve Zamecnik</b>', 'amino asitler zincire girmeden önce <b>ATP ile aktive edilir</b> → <b>tRNA</b> (adaptor molecule); biyokimya ile moleküler biyolojiyi bağladı'],
        ['<b>1958</b>', '<b>George Beadle ve Edward Tatum</b>', '<b>"one gene – one enzyme"</b>: bir gen bir enzimin üretiminden sorumludur (kanıtladılar)']], ))
    add(TRAP('Benzer isimler, karışan yıllar', '<ul>'
        '<li><b>1838</b> Schleiden = bitkiler · <b>1839</b> Schleiden + Schwann = hücre kuramı (hayvanlar Schwann) · <b>1858</b> Virchow = her hücre hücreden.</li>'
        '<li><b>1902 Garrod</b> fikri ilk söyledi (öncü) · <b>1958 Beadle & Tatum</b> kanıtladı: one gene–one enzyme.</li>'
        '<li><b>1928 Griffith</b> = transformasyon (ilke bilinmiyor) · <b>1944 Avery</b> = o ilkenin <b>DNA</b> olduğunu gösterdi.</li>'
        '<li><b>1869 Miescher</b> = nuclein (DNA\'yı buldu) · <b>1953 Watson & Crick</b> = yapısını (çift sarmal) buldu.</li>'
        '<li><b>Leeuwenhoek</b> = "father of microbiology" · <b>Virchow</b> = "father of pathology" · <b>Mendel</b> = "father of genetics" · <b>Schwann</b> = "founder of histology".</li>'
        '<li>Slaytta Hooke için <b>1655</b> yazıyor (yaygın kaynaklarda 1665). Sınavda slayttaki yıl esas alınır.</li></ul>'))
    k.h3('Mikroskop ve diğer araçlar')
    add('<p><b>Electron microscope</b> (elektron mikroskobu), ışık mikroskobundan daha yüksek <b>büyütme</b> (magnification), <b>çözünürlük</b> (resolution) ve ayrıntı verir. '
        'Işık mikroskobu teknikleri: <b>brightfield</b> (boyasız/boyalı), <b>phase-contrast</b>, <b>differential-interference-contrast (Nomarski)</b>, <b>fluorescence</b>, <b>confocal</b>. '
        'Ayrıca <b>X-ray diffraction</b> (DNA yapısı) ve <b>ultracentrifuge</b> (hücre bileşenlerini ayırma: doku öğütülüp "organic soup" yapılır, santrifüjlenir) kullanılır.</p>'
        '<p>20. yüzyıl ortasında moleküler hücre biyolojisi hızla büyüdü; hücreler canlı dışında tutulup çoğaltılabildi. Yardım eden gelişmeler: <b>steril hücre kültürü</b>, <b>elektron mikroskopisi</b>, <b>transfection</b> yöntemleri, denizanasında <b>green fluorescent protein (GFP)</b> keşfi, <b>small interfering RNA (siRNA)</b>.</p>')
    add(KAV((T('Leeuwenhoek', 'Levenhuk'), '1674, ilk canlı hücreler, animalcules, father of microbiology'),
            (T('Schleiden & Schwann', 'Şlayden ve Şvan'), '1838–1839 hücre kuramı (bitki / hayvan)'),
            (T('Virchow', 'Virşov'), '1858 Omnis cellula e cellula; father of pathology'),
            (T('Garrod', 'Garrod'), '1902 alkaptonüri; kusurlu gen → kusurlu enzim'),
            (T('Beadle & Tatum', 'Bidl ve Teytım'), '1958 one gene – one enzyme'),
            (T('Avery, MacLeod, McCarty', ''), '1944 genler DNA\'dan yapılmıştır'),
            (T('Hoagland & Zamecnik', ''), '1957 amino asit aktivasyonu (ATP) → tRNA')))
    add(EXAM(
        ('Who is known as "the father of microbiology" and first described living cells (animalcules) using a handcrafted microscope?', ['Robert Hooke', 'Anton van Leeuwenhoek', 'Robert Brown', 'Zacharias Jansen'], 'B', 'Leeuwenhoek, 1674: gölet suyunda alg (Spirogyra), animalcules.'),
        ('The nucleus was first described in orchid cells by:', ['Robert Brown (1833)', 'Matthias Schleiden (1838)', 'Walther Flemming (1879)', 'Camillo Golgi (1898)'], 'A', 'Robert Brown 1833.'),
        ('Which scientist identified "nuclein" in the nuclei of white blood cells in 1869?', ['Oswald Avery', 'Friedrich Miescher', 'Frederick Griffith', 'Gregor Mendel'], 'B', 'Miescher: nuclein = DNA ana bileşeni.'),
        ('Archibald Garrod (1902) is known for:', ['developing the ultracentrifuge', 'showing that alkaptonuria is inherited and a defective gene gives rise to a defective enzyme', 'discovering the double helix', 'formulating the cell theory'], 'B', 'Garrod alkaptonüriyi çekinik özellik olarak tanımladı ve one gene–one enzyme fikrinin öncüsü oldu.'),
        ('Which experiment first proved that "genes are made of DNA"?', ['Griffith, 1928', 'Avery, MacLeod and McCarty, 1944', 'Watson and Crick, 1953', 'Beadle and Tatum, 1958'], 'B', 'Griffith transformasyonu gösterdi ama ilkeyi tanımlamadı; Avery ve arkadaşları ilkenin DNA olduğunu 1944\'te kanıtladı.'),
        ('Thomas Morgan provided the first definitive evidence for the chromosome theory of inheritance using:', ['garden pea', 'Escherichia coli', 'Drosophila melanogaster', 'maize'], 'C', 'Morgan 1910, meyve sineği.'),
        ('In Mendel\'s pea experiments, the F2 generation showed purple and white flowers in a ratio of about:', ['1:1', '3:1', '9:3:3:1', '1:2:1'], 'B', 'F1 hep mor (baskın); F2\'de 3 mor : 1 beyaz.'),
        ('Mahlon Hoagland and Paul Zamecnik (1957) showed that amino acids must be activated by ATP before being incorporated into a peptide chain. This led to the identification of:', ['mRNA', 'tRNA', 'rRNA', 'siRNA'], 'B', 'tRNA = adaptör molekül.'),
        ('Theodor Svedberg is best known for developing the:', ['electron microscope', 'compound microscope', 'ultracentrifuge', 'X-ray diffraction'], 'C', 'Svedberg 1925 ultrasantrifüj; Nobel Kimya 1926.'),
    ))

    # ================= 3 =================
    k.h2('3 · Hücrenin kökeni ve evrimi')
    add('<p>Bakteri, sinek, kurbağa ya da insan; deri, karaciğer ya da beyin hücresi… hepsinde aynı ya da neredeyse aynı moleküller ve etkileşimler çalışır. Buradan <b>iki sonuç</b> çıkar: '
        '<b>1)</b> yaşamı sürdüren temel yapı ve mekanizmalar bütün canlılarda <b>ortaktır</b>; <b>2)</b> yaşamı oluşturan süreçler <b>ortak kurallarla</b> yönlendirilmiştir. '
        'Yani bütün canlılar birbirine bağlıdır ve yaklaşık <b>4 milyar yıl önceki</b> tek bir başlangıca uzanır.</p>')
    add('<p><b>İlk hücre</b> büyük olasılıkla küçük organik moleküller ve hem <b>bilgi taşıyan hem katalizleyen RNA benzeri</b> bir madde içeren bir keseydi. Zamanla bilgi depolama işini <b>daha kararlı olan DNA</b>, katalizi ise <b>yapı çeşitliliği daha fazla olan proteinler</b> üstlendi. '
        'Bugün DNA genetik bilginin deposu, RNA ise protein sentezini yönlendiren aracıdır.</p>')
    k.h3('Moleküllerden ilk hücreye: 8 adım')
    add(TABLE(['#', 'Adım', 'Açıklama'], [
        ['1', 'Simple biological molecules can form under prebiotic conditions', 'amino asitler, şekerler, pürin ve pirimidinler kendiliğinden oluşabilir'],
        ['2', 'Simple organic molecules associate to form polymers', 'nükleotit → polinükleotit (DNA, RNA), amino asit → polipeptit (protein), monosakkarit → polisakkarit; <b>su kaybıyla</b> (spontaneous polymerization), uzunluk ve dizi rastgele; bugün proteinler <b>20</b> amino asitten'],
        ['3', 'Polynucleotides direct their own synthesis', 'baz eşleşmesi (G–C, U–A, zayıf bağlarla) → bir zincir diğerine <b>kalıp</b> olur'],
        ['4', 'Self-replicating molecules undergo natural selection', 'kendini kopyalayan moleküller arasında seçilim'],
        ['5', 'Specialized RNA molecules catalyze reactions', 'RNA kıvrılarak (aynı zincirde eşleşme) özel şekil alır ve tepkime katalizler'],
        ['6', 'Information flows from polynucleotides to polypeptides', 'bilgi nükleik asitten proteine akar'],
        ['7', 'Membranes defined the first cell', 'zarların temel yapı taşı <b>phospholipids</b>: suda kendiliğinden <b>çift katmanlı kapalı keseler</b> oluşturur'],
        ['8', 'All present-day cells use DNA as hereditary material', 'bugünkü bütün hücrelerde kalıtım materyali DNA']]))
    add('<p><b>Fosfolipitler</b> <b>hydrophilic heads</b> (suyu seven baş) ve <b>lipophilic/hydrophobic tails</b> (yağı seven kuyruk) taşır. Yağ-su sınırında baş suda, kuyruk yağda dizilir; '
        'suda ise kuyruklar birbirine dönük, başlar suya dönük <b>kapalı çift katmanlı keseler</b> (closed bilayer vesicles) oluşur. "Yaşamın bir içi ve bir dışı olmalı": misk öküzleri tehlikede başlar dışarı, kuyruklar içeri daire olur (heads out – tails in).</p>')
    add(TRAP('Slayttaki deney adı', '<p>Slaytta ilkel dünya koşullarını taklit eden deney (kapalı düzenekte su ısıtılır; <b>CH₄, NH₃, H₂</b> karışımından <b>elektrik akımı</b> geçirilir, U-tüpte organik bileşikler birikir) "<b>Wöhler experiment (1828)</b>" diye geçiyor. '
        'Friedrich Wöhler (1800–1882) aslında <b>üre sentezi</b> ile bilinir; anlatılan düzenek yaygın kaynaklarda <b>Miller–Urey deneyi (1953)</b> olarak bilinir <i>(genel bilgi)</i>. Sınavda slayttaki ifade sorulursa slayttakini işaretle.</p>'))
    k.h3('Endosimbiyoz ve evrim')
    add('<p>Bir ökaryot hücre <b>aerobik bir prokaryotu yuttu</b> → ortak yaşam (<b>endosymbiotic relationship</b>) → <b>mitochondrion</b>. Mitokondrili hücreler daha sonra <b>fotosentetik prokaryotları yuttu</b> → <b>chloroplast</b>. '
        'Bütün canlılar ortak bir ata hücreden <b>doğal seçilimle evrim</b> sonucu türemiştir. Bu iki süreçten oluşur: <b>(1)</b> kalıtsal bilgide <b>rastgele çeşitlenme</b> (random variation), <b>(2)</b> sahibinin hayatta kalmasına ve çoğalmasına yardım eden bilginin <b>seçilmesi</b>. '
        '<b>Evrim biyolojinin merkezi ilkesidir.</b></p>')
    add('<p>Prokaryotlardan ökaryotlara: prokaryotlar <b>yapıca basit ama biyokimyasal olarak çok çeşitlidir</b>; <b>cyanobacteria</b> (mavi-yeşil algler) <b>CO₂ ve N₂ bağlayabilir</b>; bakteriler besinleri aerobik olarak oksitleyebilir. '
        'Ökaryotlar: kendine özgü organeller, oksidatif metabolizma için <b>mitokondriye bağımlılık</b>, yutulmuş prokaryottan gelen kloroplastlar, zengin iç zarlar, <b>hücre iskeleti</b>, en karmaşık hücreler <b>protozoa</b> (ör. Didinium\'un Paramecium\'u yutması), genetik materyalin karmaşık paketlenmesi. '
        'Evrimsel ilişkiler <b>DNA dizileri karşılaştırılarak</b> çıkarılabilir.</p>')
    add(KAV((T('First cell', 'ilk hücre'), '~4 milyar yıl önce; RNA benzeri madde hem bilgi hem kataliz'),
            (T('DNA vs protein', 'DNA ve protein'), 'DNA bilgi depolamayı (daha kararlı), proteinler katalizi (daha çeşitli) devraldı'),
            (T('Endosymbiosis', 'endosimbiyoz'), 'yutulan aerobik prokaryot → mitokondri; fotosentetik prokaryot → kloroplast'),
            (T('Natural selection', 'doğal seçilim'), 'rastgele çeşitlenme + yararlı bilginin seçilmesi')))
    add(EXAM(
        ('According to the endosymbiotic theory, mitochondria evolved from:', ['an engulfed aerobic prokaryote', 'an engulfed photosynthetic prokaryote', 'a virus', 'the nuclear envelope'], 'A', 'Aerobik prokaryot → mitokondri; fotosentetik prokaryot → kloroplast.'),
        ('Why did DNA take over the information storage function from RNA during early evolution?', ['DNA is a better catalyst', 'DNA is more stable', 'DNA contains uracil', 'DNA is single-stranded'], 'B', 'DNA daha kararlıdır; kataliz işini çeşitliliği fazla olan proteinler aldı.'),
        ('In water, phospholipids spontaneously form:', ['single-layer sheets with tails in water', 'closed bilayer vesicles with hydrophilic heads exposed to water', 'protein channels', 'DNA double helices'], 'B', 'Kuyruklar içe, başlar suya bakar.'),
        ('Which statement about polymer formation under prebiotic conditions is correct?', ['Polymers formed with addition of water', 'Polymers were of random length and sequence', 'Only DNA could polymerize', 'Proteins were built from 4 amino acids'], 'B', 'Kendiliğinden polimerleşme su kaybıyla olur; ürün rastgele uzunluk ve dizidedir.'),
        ('Evolution by natural selection involves two essential processes:', ['mitosis and meiosis', 'random variation in genetic information and selection of favorable information', 'transcription and translation', 'endocytosis and exocytosis'], 'B', 'Rastgele çeşitlenme + seçilim.'),
    ))

    # ================= 4 =================
    k.h2('4 · Canlıların sınıflandırılması: 3 domain, 6 kingdom')
    add('<p><b>Carl Linnaeus</b> (1707–1778, İsveçli botanikçi, zoolog ve hekim) 1735\'te sınıflandırmayı kurduğunda yalnız <b>iki alem</b> vardı: bitkiler ve hayvanlar. Bir nesneyi önce <b>hayvan, bitki ya da mineral</b> diye ayırırdı; bunlar ilk "domain"lerdi. '
        'Sıralama: <b>domain → kingdom → phylum</b> (bitki ve mantarda <b>division</b>) <b>→ class → order → family → genus → species → subspecies</b> (botanikte <i>varietas</i>, <i>forma</i>).</p>')
    add('<p>Bugün <b>altı alem</b> vardır: <b>Plants, Animals, Protists, Fungi, Archaebacteria, Eubacteria</b>. Bir canlının alemi şunlara göre belirlenir: <b>hücre tipi</b> (karmaşık/basit), <b>kendi besinini yapabilmesi</b>, <b>vücudundaki hücre sayısı</b>.</p>')
    add(TABLE(['Domain (üst alem)', 'İçindeki alemler', 'Not'], [
        ['<b>Bacteria</b>', 'Bacteria (Eubacteria)', 'hem domain hem kingdom'],
        ['<b>Archaea</b>', 'Archaea (Archaebacteria)', 'hem domain hem kingdom; görünüşte bakteriye, moleküler biyolojide ökaryotlara benzer'],
        ['<b>Eukarya</b>', 'Protista (tek hücreli), Fungi, Plantae, Animalia', '4 alem']]))
    add('<p>Üç domain sistemi <b>Woese ve arkadaşları (1990)</b>\'na dayanır. Soy ağacı ilk başta <b>morfolojik ölçütlerle</b> kuruldu: birbirine benzeyen canlılar yan yana kondu. Bütün canlıların ortak bir atadan geldiği düşünülür, çünkü bütün hücrelerin yapı ve molekülleri çok benzerdir.</p>')
    add(KAV((T('Six kingdoms', 'altı alem'), 'Plants, Animals, Protists, Fungi, Archaebacteria, Eubacteria'),
            (T('Three domains', 'üç domain'), 'Bacteria, Archaea, Eukarya (Woese, 1990)'),
            (T('Kingdom placement', 'alem ölçütü'), 'hücre tipi, besin yapabilme, hücre sayısı')))
    add(EXAM(
        ('Which of the following is NOT one of the six kingdoms?', ['Protists', 'Fungi', 'Viruses', 'Archaebacteria'], 'C', 'Virüsler canlı sayılmaz, alemlere girmez.'),
        ('The Eukarya domain includes which kingdoms?', ['Bacteria and Archaea', 'Protista, Fungi, Plantae, Animalia', 'Only Plantae and Animalia', 'Archaebacteria and Fungi'], 'B', 'Eukarya = 4 alem.'),
        ('Organisms are placed into kingdoms according to all of the following EXCEPT:', ['cell type (complex or simple)', 'ability to make food', 'number of cells in the body', 'color of the organism'], 'D', 'Renk bir ölçüt değildir.'),
        ('Archaea resemble bacteria physically, but some aspects of their molecular biology are more similar to:', ['viruses', 'eukaryotes', 'mycoplasmas', 'cyanobacteria'], 'B', 'Slayt: molecular biology more similar to eukaryota.'),
    ))

    # ================= 5 =================
    k.h2('5 · Prokaryotik ve ökaryotik hücreler, arkeler')
    add('<p>Bilim insanları hücreleri boyut ya da şekle göre değil, <b>genetik materyalin nasıl paketlendiğine</b> göre ayırır. DNA sitoplazmadan ayrılmamışsa <b>prokaryote</b> ("çekirdekten önce"), zarla çevrili bir <b>nucleus</b> içindeyse <b>eukaryote</b> ("gerçek çekirdek").</p>')
    add(TIP('🧩 Bütün hücrelerde ortak 4 özellik', '<p>1) <b>Plasma membrane</b> (hücre zarı) · 2) <b>genetic material</b> (DNA; genleri taşıyan kromozomlar) · 3) <b>cytosol / cytoplasm</b> (yarı akışkan madde) · 4) <b>ribosomes</b> (protein yapar).</p>'))
    add(TABLE(['', E('Prokaryotic', 'prokaryotik'), E('Eukaryotic', 'ökaryotik')], [
        ['Çekirdek', '<b>yok</b>; DNA <b>nucleoid</b> bölgesinde, zarla çevrili değil', 'var; <b>nuclear envelope</b> (çift zar, nüklear porlar)'],
        ['Kromozom', '<b>tek, kapalı halka</b> DNA + küçük halkasal <b>plasmids</b>', '<b>doğrusal</b> (linear), DNA + proteinler'],
        ['Zarlı organeller', '<b>yok</b> (ribozom var ama zarsız)', 'var (mitokondri, kloroplast…)'],
        ['Hücre iskeleti', 'yok (slayt)', 'var'],
        ['Hücre duvarı', 'hepsinde; ana bileşen <b>peptidoglycan</b> (<b>mycoplasma hariç</b>)', 'bazen; <b>cellulose</b> (bitki) ya da <b>chitin</b> (mantar); <b>hayvan hücresinde yok</b>'],
        ['Zarda kolesterol', 'yok (sadece <b>mycoplasma</b>)', 'var'],
        ['Elektron taşıma zinciri', 'hücre zarında <i>(genel bilgi)</i>', 'organel zarlarında (mitokondri)'],
        ['Boyut', '<b>0,1–5,0 µm</b>; ~<b>10 kat küçük</b> → daha hızlı büyür ve çoğalır', '<b>10–100 µm</b>'],
        ['Kamçı', '<b>döner</b> (rotate)', '<b>dalga gibi çırpar</b> (beat in waves), ör. sperm'],
        ['Örnek', 'bakteriler, cyanobacteria, arkeler', 'protistler, mantarlar, bitkiler, hayvanlar']]))
    k.h3('Prokaryot hücre yapısı (dıştan içe)')
    add(TABLE(['Yapı', 'Görevi / özelliği'], [
        ['<b>Appendages</b>', E('pili') + ', ' + E('flagella', 'kamçılar') + ', ' + E('axial filaments')],
        ['1 · ' + E('Glycocalyx', 'şeker örtüsü'), 'çoğunlukla <b>capsule</b> (kapsül) denir'],
        ['2 · ' + E('Outer membrane', 'dış zar'), 'çift katman: iç tabaka fosfolipit, dış tabaka <b>lipopolysaccharides</b> (başka hiçbir canlıda bulunmaz)'],
        ['3 · ' + E('Cell wall', 'hücre duvarı'), '<b>peptidoglycan</b>; görevi: <b>hücre şekli</b> ve <b>turgor basıncına dayanma</b>'],
        ['4 · ' + E('Periplasm', 'periplazma'), 'zar ile duvar arasındaki boşluk; besinleri parçalayan proteinler içerir'],
        ['5 · ' + E('Plasma membrane', 'plazma zarı'), 'sitoplazmayı çevreler, madde giriş-çıkışını düzenler'],
        ['6 · ' + E('Cytoplasm', 'sitoplazma'), 'nükleoit, ribozomlar']]))
    add('<p><b>E. coli</b> gibi bazı bakteriler, aralarında <b>periplasmic space</b> olan <b>iki zarla</b> çevrilidir; ince hücre duvarı iç zarın yanındadır. Üç temel şekil: <b>bacillus</b> (çubuk), <b>coccus</b> (küre), <b>spirillum / spirochetes</b> (sarmal). '
        'Cyanobacteria (ör. <b>Spirulina platensis</b>: Gram-negatif, oksijenik, fotosentetik, ipliksi) tek hücreli ya da zincir halinde olabilir; besin takviyelerinde kullanılır (Aztekler "tecuitlatl").</p>')
    add(TABLE(['Bakteri rakamları (slayt)', 'Değer'], [
        ['Bakteri çapı', '0,1–5,0 µm'], ['Bir E. coli\'nin kuru ağırlığı', '≈ 25 × 10⁻¹⁴ g'], ['İnsan vücudundaki bakteri', '≈ 1–1,5 kg'],
        ['Dünyadaki bakteri sayısı / kütlesi', '5 × 10³⁰ / ≈ 10¹² kg'], ['Bulunduğu yerler', 'okyanusta 7 mil derinlik, atmosferde 40 mil yükseklik'],
        ['Karbon', 'bakterilerde depolanan karbon ≈ bitkilerdeki karbon']]))
    add(TRAP('Mycoplasma istisnası', '<p>Prokaryotların hepsinde peptidoglikan duvar vardır, <b>mycoplasma hariç</b>. Duvarı olmadığı için <b>penisiline duyarsızdır</b> (ör. <i>Spiroplasma citrii</i>: üç katmanlı zar). Prokaryotlarda zarında <b>kolesterol</b> olan tek grup da yine mycoplasma.</p>'))
    k.h3('Ökaryotlar')
    add('<p>Ökaryot hücre: DNA <b>nuclear envelope</b> ile çevrili çekirdekte ("control center of the cell"), <b>zarlı organeller</b> ve plazma zarı ile çekirdek arasında <b>sitoplazma</b> (<b>cytosol</b> = sulu faz + organeller). '
        'Zar proteinleri: <b>integral, peripheral, lipid-anchored</b>. Dış uzantılar: <b>cilia</b> (kısa, kıl gibi, hareketli; ciliates), <b>flagella</b> (insanda sperm; dalga gibi çırpar). '
        'Zar dışında <b>glycocalyx</b> (zar glikoproteinlerinin karbonhidrat zincirleri). Ribozomlar zarsızdır (protein sentezi). '
        'Boyut: genelde <b>10–100 µm</b>; insan <b>fibroblastı ~15 µm</b> (hacim ve kuru ağırlığı E. coli\'nin binlerce katı); amip <b>0,5 mm\'den uzun</b>; devekuşu yumurtası tek hücredir ve gözle görülür.</p>')
    add('<p>Eukarya alemleri: <b>Protista</b> (protozoa "hayvan benzeri" tek hücreli, ör. flagellata; protophyta "bitki benzeri" algler; "mantar benzeri" cıvık ve su küfleri), '
        '<b>Fungi</b> (çok hücreli <b>molds</b> / küfler ve tek hücreli <b>yeasts</b> / mayalar), <b>Animalia</b>, <b>Plantae</b>.</p>')
    add(TRAP('Slayttaki iki ifade', '<p>Slaytta ökaryotların prokaryotlardan "<b>about 2 million years</b>" sonra evrimleştiği yazıyor; yaygın kaynaklarda bu süre <b>yaklaşık 2 milyar yıl</b> olarak geçer <i>(genel bilgi)</i>. '
        'Slayttaki DNA çapı da bir yerde ~10 nm, başka bir yerde ~2 nm geçiyor; doğrusu <b>~2 nm</b>.</p>'))
    k.h3('Archaea (arkeler)')
    add('<p>DNA dizileri iki tür prokaryot olduğunu gösterdi: <b>eubacteria</b> (gerçek bakteriler) ve <b>archaea</b> (archaebacteria). Arkeler <b>boyut ve şekilce bakteriye</b>, <b>moleküler biyolojide ökaryotlara</b> benzer. '
        'Çoğu aşırı koşullarda (yüksek basınç ve sıcaklık) yaşar; bu koşullar yaşamın başladığı ilk dünyaya benzer. İlk bulundukları yerlerden biri <b>Yellowstone</b> sıcak su kaynaklarıdır (Grand Prismatic Spring, termofiller).</p>')
    add(TABLE(['Arke grubu', 'Özellik'], [
        ['<b>Halophiles</b> (tuz seven)', 'yaşamak için yüksek tuz gerekir; çoğu kemoheterotrof'],
        ['<b>Thermoacidophiles</b> (sıcak ve asit seven) / sulfur metabolizers', '<b>80 °C</b> kükürtlü kaynaklar, <b>pH &lt; 2</b>'],
        ['<b>Methanogens</b> (metan üreten)', 'oksijensiz ortam; <b>CO₂ + su (H₂)</b> → <b>metan (CH₄)</b>; kesin anaerob, ototrof; işkembede yaşayanlar günde <b>&gt;150 L</b> metan; inekler günde <b>600 L</b>\'ye kadar metan üretir (küresel metanın ~%15\'i)']]))
    k.h3('Tek hücreliler bize yarar da zarar da verir')
    add('<p><b>E. coli</b> sindirime yardım eder; slayta göre "streptomyces" boğaz enfeksiyonu (strep throat) yapar <i>(genel bilgi: strep throat etkeni Streptococcus)</i>. Protozoa toprak verimliliğinde önemlidir ama <b>Plasmodium</b> (4 türü insanda <b>sıtma</b>) zararlıdır; '
        '<b>P. falciparum</b> yılda <b>300 milyondan fazla</b> yeni vaka, <b>1,5–3 milyon</b> ölüm. Mayalar ve küfler (<b>fungi</b>) kalıntıları ayrıştırır, <b>antibiyotik</b> yapar, ekmek, bira, şarap, peynir yapımında kullanılır; zararı: <b>athlete\'s foot</b> (tinea pedis). '
        'Peynir yapımında <b>Lactococcus lactis</b> (eubakteri) kullanılır.</p>'
        '<p>Tek hücreliler <b>eşeyli</b> (mating: besin azken <b>mayozla haploid</b> hücreler) ya da <b>eşeysiz</b> (<b>budding</b>/tomurcuklanma: <b>mitozla diploid</b>) çoğalır. <b>Saccharomyces cerevisiae</b> (ekmek ve bira mayası) iyi bir deney organizmasıdır; '
        'iki <b>mating type</b> vardır (yumurta ve sperm gibi); karşıt tipler kaynaşınca ikisinin genetik materyalini taşıyan üçüncü bir hücre tipi oluşur. Eşeyli üreme genetik değişimi hızlandırır, zararlı mutasyonları ayıklar. Tomurcuklanmada her tomurcuktan sonra bir <b>bud scar</b> (tomurcuk izi) kalır; önceki tomurcuk sayısı sayılabilir.</p>')
    add(KAV((T('Nucleoid', 'nükleoit'), 'prokaryotta çekirdeğin yerine: zarla çevrili olmayan DNA bölgesi'),
            (T('Plasmids', 'plazmitler'), 'bakteride ana kromozom dışındaki küçük halkasal DNA'),
            (T('Peptidoglycan', 'peptidoglikan'), 'prokaryot hücre duvarının ana bileşeni; şekil ve turgor basıncı'),
            (T('Lipopolysaccharides', 'lipopolisakkaritler'), 'bakteri dış zarının dış tabakası; başka canlıda yok'),
            (T('Mycoplasma', 'mikoplazma'), 'hücre duvarı yok, penisiline duyarsız; zarında kolesterol olan tek prokaryot'),
            (T('Methanogens', 'metanojenler'), 'CO₂ + H₂ → CH₄; kesin anaerob arkeler'),
            (T('Budding', 'tomurcuklanma'), 'mayada eşeysiz üreme (mitoz, diploid); bud scar kalır')))
    add(EXAM(
        ('Prokaryotic cells do not have a nucleus. Instead, their DNA is located in a region called the:', ['nucleolus', 'nucleoid', 'periplasm', 'glycocalyx'], 'B', 'Nükleoit: zarla çevrili olmayan DNA bölgesi (hoca tekrar sorusu 8).'),
        ('Which of the following is common to ALL cells?', ['nucleus', 'mitochondria', 'ribosomes', 'cell wall'], 'C', 'Her hücrede: plazma zarı, DNA, sitoplazma, ribozom.'),
        ('The main component of the prokaryotic cell wall is:', ['cellulose', 'chitin', 'peptidoglycan', 'cholesterol'], 'C', 'Peptidoglikan; mycoplasma hariç.'),
        ('Which prokaryotes lack a cell wall and are therefore unaffected by penicillin?', ['Cyanobacteria', 'Mycoplasmas', 'Methanogens', 'Escherichia coli'], 'B', 'Mycoplasma (ör. Spiroplasma citrii).'),
        ('Lipopolysaccharides, a compound not found in any other living organism, are found in the:', ['outer membrane of bacteria', 'nuclear envelope', 'eukaryotic plasma membrane', 'mitochondrial inner membrane'], 'A', 'Bakteri dış zarının dış tabakası.'),
        ('Which statement about flagella is correct?', ['Eukaryotic flagella rotate', 'Prokaryotic flagella rotate, eukaryotic flagella beat in waves', 'Both beat in waves', 'Only plants have flagella'], 'B', 'Slayt: prokaryotic flagella rotate!'),
        ('Archaea that live in oxygen-free environments and produce methane from carbon dioxide are called:', ['halophiles', 'thermoacidophiles', 'methanogens', 'cyanobacteria'], 'C', 'Metanojenler kesin anaerob ve ototroftur.'),
        ('Eukaryotic cells are typically about ___ in diameter, whereas bacteria are about ___ .', ['10–100 µm / 0.1–5.0 µm', '1 mm / 1 µm', '0.1 µm / 10 µm', '200 nm / 2 nm'], 'A', 'Ökaryot 10–100 µm, bakteri 0,1–5,0 µm.'),
        ('The cell walls of fungi are mainly composed of:', ['peptidoglycan', 'chitin', 'cellulose', 'collagen'], 'B', 'Bitki: selüloz; mantar: kitin; hayvan hücresinde duvar yok.'),
    ))

    # ================= 6 =================
    k.h2('6 · Virüsler: "ultimate parasites"')
    add('<p><b>Viruses</b> canlı sayılmaz, çünkü <b>kendi başlarına büyüyemez ve çoğalamazlar</b>. Yaşamak için bir <b>host cell</b> (konak hücre) enfekte edip onun iç makinesini ele geçirmeleri, viral proteinleri ve (bazen) genetik materyallerini onunla sentezletmeleri gerekir. Bu yüzden "<b>the ultimate parasites</b>" (en uç parazitler) denir.</p>')
    add(TABLE(['Özellik', 'Açıklama'], [
        ['Boyut', '~<b>100 nm</b> (bakteri ~<b>1000 nm</b>; 1 nm = 10⁻⁹ m)'],
        ['Yapı', '<b>protein coat</b> (<b>capsid</b>) + içinde genetik materyal; bazılarında dışta zar benzeri <b>envelope</b>'],
        ['Konak', 'çoğunun konak aralığı dardır: belirli bakteri, bitki ya da hayvanlar'],
        ['Önem', 'tıbbi tehdit ama aynı zamanda fırsat: hücrelere genetik materyal taşımak için araç olarak kullanılır']]))
    add(TABLE(['Örnek', 'Ne yapar?'], [
        ['<b>Bacteriophage</b> (phage), ör. <b>T4</b>', 'bakteriyi enfekte eder; kuyruk yapısıyla tutunur'],
        ['<b>Tobacco mosaic virus</b>', 'tütün yapraklarında alacalı leke, büyüme geriliği'],
        ['<b>Adenovirus</b>', 'insanda göz ve solunum yolu enfeksiyonu'],
        ['<b>Poliovirus</b>', 'felç (poliomyelitis); aşıyla neredeyse yok edildi'],
        ['Diğer', 'su çiçeği, grip; çiçek hastalığı (smallpox) eskiden dünya çapında bela; mısırda cüce mozaik virüsü']]))
    add('<p>Diğer patojen örnekleri (slayt): <b>Vibrio cholerae</b> (kolera, ishal salgını), <b>Toxoplasma gondii</b> (kedi paraziti; AIDS\'li bağışıklığı zayıf kişilerde kas ve beyin enfeksiyonu), <b>Ascaris</b> nematodları (bağırsak tıkanıklığı).</p>')
    add(EXAM(
        ('Why are viruses considered the "ultimate parasites"?', ['They have their own ribosomes', 'They cannot grow or reproduce on their own and must take over a host cell\'s machinery', 'They are larger than bacteria', 'They perform photosynthesis'], 'B', 'Hoca tekrar sorusu 10.'),
        ('Viruses that infect bacteria are called:', ['adenoviruses', 'bacteriophages', 'retroviruses', 'mycoplasmas'], 'B', 'Bakteriyofaj (phage), ör. T4.'),
        ('A typical virus is about ___ in diameter.', ['100 nm', '1000 nm', '10 µm', '1 mm'], 'A', 'Virüs ~100 nm, bakteri ~1000 nm.'),
        ('The protein coat that encloses the viral genetic material is called the:', ['capsid', 'glycocalyx', 'nucleoid', 'periplasm'], 'A', 'Kapsit; bazılarında dışında zarf (envelope) da vardır.'),
    ))

    # ================= 7 =================
    k.h2('7 · Tek hücreden organizmaya: zigot, kök hücre, organizasyon')
    add('<p>Her insan bir <b>zygote</b> (yumurta + sperm birleşimi) olarak başlar. İnsan yumurtası yaklaşık <b>200 µm</b> çapında tek bir hücredir. Zigot, yaklaşık <b>60–100 trilyon (10¹⁴)</b> hücreden oluşan bedeni kurmak için gerekli bütün bilgiyi taşır. '
        'İnsan vücudunda yaklaşık <b>200 farklı hücre tipi</b> vardır. Hücrenin içindeki "bilgi", canlının kurbağa mı insan mı olacağını belirler.</p>')
    add('<p>Döllenmiş yumurta 2, 4, 8 hücreye bölünür; <b>proliferation</b> (çoğalma) ve <b>differentiation</b> (farklılaşma) bütün dokuları oluşturur. Farklı hücre tiplerini yapmak yetmez; hücreler doku, organ ve uzantılar halinde <b>doğru dizilmelidir</b> (iki elimiz aynı hücrelerden ama ayna görüntüsü düzende). '
        '<b>Polarity</b> (kutupluluk): hücrelerin işlev ya da yapı bakımından <b>asimetrik</b> olması; bağırsak örtüsü, eller ve kalp gibi asimetrik yapılar böyle oluşur. <b>Tek yumurta ikizleri</b>, erken embriyonun hücre kütlesi ikiye ayrılınca oluşur.</p>')
    add('<p><b>Embryonic stem (ES) cells</b>: embriyodaki en ilkel, farklılaşmamış hücreler; bütün bedeni oluşturabilirler. Birçok hücre tipine farklılaşabilme yeteneğine <b>plasticity</b> denir. '
        'Sekiz hücre evresindeki fare embriyosunda <b>her hücre</b> hayvanın her bölümünü oluşturabilir. Kök hücre ve klonlamaya bilimsel ilgi: genlerin potansiyelini açığa çıkaran sinyalleri öğrenmek; tıbbi ilgi: hasarlı ya da eksik hücre tipleriyle giden hastalıkları tedavi etmek, yaraları daha iyi onarmak.</p>')
    add(TABLE(['Organizasyon düzeyleri (basitten karmaşığa)'], [['atoms → molecules → organelles → cells → tissues → organs and organ systems → organisms → populations → communities → ecosystems → biosphere']]))
    add('<p>Her düzey altındakileri içerir ve her düzeyde <b>yeni özellikler ortaya çıkar</b> (emergent properties). Bütünü parçalarını öğrenerek anlamaya <b>reductionism</b> denir. '
        'Ölçekler: hücreler <b>1 µm ile yüzlerce µm</b>; DNA çift sarmalı ~<b>2 nm</b>; çekirdek ~<b>10 µm</b> (DNA\'dan ~1000 kat büyük); 3 günlük 8 hücreli insan embriyosu ~200 µm; mikrometre = <b>micron</b>.</p>')
    add(KAV((T('Zygote', 'zigot'), 'yumurta + sperm; 60–100 trilyon hücrelik bedenin bütün bilgisi'),
            (T('Cell types in human body', 'insan vücudundaki hücre tipi'), '~200'),
            (T('Plasticity', 'plastisite'), 'kök hücrenin birçok hücre tipine farklılaşabilmesi'),
            (T('Polarity', 'kutupluluk'), 'hücrenin işlev/yapı bakımından asimetrik olması')))
    add(EXAM(
        ('Approximately how many different cell types are in the human body?', ['20', '200', '2,000', '60 trillion'], 'B', '~200 hücre tipi; ~60–100 trilyon hücre (hoca tekrar sorusu 3).'),
        ('The ability of embryonic stem cells to differentiate into a number of cell types is called:', ['polarity', 'plasticity', 'apoptosis', 'reductionism'], 'B', 'Plastisite.'),
        ('Distinct functional and/or structural asymmetry of a cell is called:', ['polarity', 'differentiation', 'proliferation', 'mutation'], 'A', 'Polarite: bağırsak örtüsü, el, kalp gibi asimetrik yapılar.'),
        ('A zygote is formed by:', ['division of a stem cell', 'the union of an egg and a sperm', 'budding', 'fusion of two somatic cells'], 'B', 'Yumurta + sperm.'),
        ('Identical twins occur when:', ['two eggs are fertilized by two sperm', 'the mass of cells composing an early embryo divides into two parts', 'a zygote undergoes meiosis', 'a stem cell differentiates'], 'B', 'Erken embriyo hücre kütlesi ikiye ayrılır.'),
    ))

    # ================= 8 =================
    k.h2('8 · Enerji: canlılar enerjiyi nereden alır?')
    add('<p>Her canlı çevresiyle madde ve enerji alışverişi yapar (ağaç topraktan su ve mineral, havadan CO₂ alır; oksijen verir). Ekosistemin iki temel süreci: <b>besin döngüsü</b> (nutrient cycling: bitkilerin aldığı madde toprağa döner) ve <b>enerji akışı</b> '
        '(güneş ışığı → üreticiler → tüketiciler). Enerji ekosisteme genellikle <b>ışık</b> olarak girer, <b>ısı</b> olarak çıkar. Enerji biçimleri: ışık, kimyasal, kinetik, ısı.</p>')
    add(TABLE(['Grup', 'Diğer adları', 'Enerji kaynağı', 'Örnek'], [
        ['<b>Producers</b> (üreticiler)', '<b>autotrophs = inorganotrophs</b>; "primary energy converters"', 'cansız dünyadan: güneş ışığı ya da inorganik kimyasallar', 'aşağıdaki iki alt grup'],
        ['↳ <b>Phototrophic</b> (fotoototrof)', 'feeding on sunlight', 'güneş ışığı', 'bitkiler, algler, <b>cyanobacteria</b>'],
        ['↳ <b>Chemoautotrophic</b> (lithotrophic, "taş yiyen")', 'feeding on chemicals', 'inorganik kimyasallar', '<b>archaea</b>; derin okyanus, yer kabuğu'],
        ['<b>Consumers</b> (tüketiciler)', '<b>heterotrophs = organotrophs</b> (Yun. <i>trophe</i> = besin)', 'başka canlıları ya da onların ürettiği organik maddeyi yiyerek', 'herbivor (tavşan), karnivor (aslan), omnivor (insan, bağırsaktaki E. coli); hayvanlar, mantarlar'],
        ['<b>Decomposers</b> (ayrıştırıcılar)', '', 'ölü organizmaları ayrıştırarak', 'akbabalar, kırkayaklar, bok böcekleri, <b>mantarlar</b> (odunu ayrıştırabilen <b>tek</b> canlılar)']]))
    add('<p>Organotroflar, <b>birincil enerji dönüştürücüleri</b> (üreticiler) olmadan var olamaz; üreticiler yeryüzündeki <b>en büyük canlı kütlesini</b> oluşturur. Galápagos çatlağındaki <b>tüp solucanları</b> dokularındaki kemosentetik bakterilerden enerji alır, sindirim sistemleri yoktur. '
        '<b>Hidrotermal baca</b>: merkezde <b>350 °C\'nin üstü</b>, çevrede <b>2–3 °C</b>; soğuyan sudan mineraller çökerek baca (chimney) oluşturur (birkaç metre, akış 1–2 m/s).</p>')
    add('<p>Biyolojide enerji dönüşümü örnekleri: koşan at <b>kimyasal → mekanik</b>, elektrik balığı (Torpedinidae) <b>kimyasal → elektrik</b>, fosforlu bakteriler <b>kimyasal → ışık</b>. '
        '<b>James Prescott Joule</b> (1818–1889) 1843\'te termodinamiğin birinci yasasını deneyle kanıtladı ve ısının mekanik eşdeğerini buldu. <b>1 J</b> = 1 newton kuvvetin 1 metre uygulanması; 1 kJ = 1000 J. '
        '<b>1 cal</b> = 1 g suyu 14,5\'ten 15,5 °C\'ye ısıtan enerji; <b>1 kcal = 1000 cal = 4,184 kJ</b>.</p>')
    add(TIP('⚡ ATP: evrensel enerji para birimi', '<p>Serbest enerjiyi <b>metabolic fuels</b>\'tan (şekerler, proteinler, lipitler, vitaminler, mineraller) alırız. Hücrede kimyasal tepkimelerin enerji kaynağı çoğunlukla <b>ATP\'nin hidrolizidir</b>; ATP hazır kimyasal enerjiyi <b>iki kimyasal bağında</b> saklar. '
        'Genel tepkime: <b>C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O</b> (gerçekte çok daha karmaşık). <b>ATP synthase</b> moleküler bir motordur; <b>mitokondriler</b> "güç santralleridir".</p>'))
    add(KAV((T('Autotrophs', 'ototroflar'), 'üreticiler = inorganotroflar; fototrof (güneş) ve kemoototrof (kimyasal)'),
            (T('Heterotrophs', 'heterotroflar'), 'tüketiciler = organotroflar'),
            (T('Decomposers', 'ayrıştırıcılar'), 'ölüleri ayrıştırır; odunu yalnız mantarlar ayrıştırır'),
            (T('ATP', 'ATP'), 'evrensel enerji para birimi; hidroliziyle tepkimelere enerji verir')))
    add(EXAM(
        ('Organisms that obtain energy from inorganic chemicals in the environment (e.g., deep-sea archaea) are called:', ['phototrophic', 'chemoautotrophic (lithotrophic)', 'heterotrophic', 'decomposers'], 'B', 'Kemoototrof = lithotrof ("taş yiyen").'),
        ('Consumers are also called:', ['autotrophs or inorganotrophs', 'heterotrophs or organotrophs', 'producers', 'primary energy converters'], 'B', 'Tüketiciler = heterotroflar = organotroflar.'),
        ('Which organisms are the only ones that can decompose wood?', ['bacteria', 'fungi', 'vultures', 'dung beetles'], 'B', 'Slayt: fungi (the only organisms that can decompose wood).'),
        ('Energy usually enters an ecosystem as ___ and exits as ___ .', ['heat / light', 'light / heat', 'chemical energy / light', 'ATP / glucose'], 'B', 'Işık olarak girer, ısı olarak çıkar.'),
        ('One kilocalorie (kcal) is equal to:', ['4.184 kJ', '1000 kJ', '14.5 J', '1 newton'], 'A', '1 kcal = 1000 cal = 4,184 kJ.'),
        ('The universal energy currency in biological systems is:', ['glucose', 'ATP', 'NADH', 'water'], 'B', 'ATP hidrolizi tepkimelere enerji sağlar.'),
    ))

    # ================= 9 =================
    k.h2('9 · Hücrenin molekülleri: su, küçük moleküller, makromoleküller, genom')
    k.h3('A · Su')
    add('<p><b>Water (H₂O)</b> hücredeki <b>en bol moleküldür</b>: hücre kütlesinin <b>%70</b> ve fazlası (slaytın bir yerinde <b>%70–95</b>). Geri kalan %30 yapısal ve işlevsel moleküllerdir. '
        'Hücreler <b>su, inorganik iyonlar ve karbon içeren organik moleküllerden</b> oluşur. Su küçük ve hızlı bir moleküldür; <b>polar</b>dır (uçları zıt yüklü), bu yüzden birbiriyle <b>hidrojen bağı</b> kurar. '
        'Yaşamı destekleyen dört özelliği: <b>cohesive behavior</b> (birbirine tutunma; yüzey gerilimi), <b>sıcaklığı dengeleme</b>, <b>donunca genleşme</b>, <b>çok yönlü çözücü</b> olma. Suyun bolluğu, Dünya\'nın yaşanabilir olmasının ana nedenidir.</p>')
    k.h3('B · Küçük moleküller')
    add('<p>Hücre içi, küçük moleküllerle (basit şekerler, amino asitler, vitaminler) ve iyonlarla (sodyum, klorür, kalsiyum) "tatlandırılmış" sulu bir çorbadır. Bunların yeri ve derişimi zara yerleşmiş proteinlerle kontrol edilir: <b>pumps, transporters, ion channels</b>. '
        '<b>ATP</b> en bilinen küçük moleküldür ve enerji taşır. Bazı küçük moleküller <b>sinyal</b> görevi görür: <b>hormonlar</b> (ör. <b>epinephrine</b>: "fight or flight" yanıtı) ve <b>neurotransmitters</b>.</p>')
    k.h3('Monomerden polimere: makromoleküller')
    add(TABLE(['Makromolekül', 'Monomer', 'Not'], [
        [E('Polysaccharides', 'polisakkaritler'), 'monosakkarit (ör. <b>glucose</b> = üzüm şekeri)', 'bitki hücre duvarı, böcek iskeleti'],
        [E('Proteins', 'proteinler'), '<b>20</b> farklı amino asit, doğrusal zincir', 'genelde <b>100–1000</b> amino asit; 400 aa\'lık proteinde <b>20⁴⁰⁰</b> olası dizi; yapı: birincil, ikincil, üçüncül, dördüncül'],
        [E('Nucleic acids', 'nükleik asitler'), 'nükleotit = <b>şeker + baz + fosfat</b>', 'DNA: <b>thymine + deoxyribose</b>; RNA: <b>uracil + ribose</b>'],
        [E('Lipids', 'lipitler'), 'uzun yağ asidi zincirleri', 'yağ asitleri → <b>triglycerides</b> (triacylglycerols); zar lipidi <b>phosphatidylcholine</b> = hidrofilik baş (fosfat + alkol) + gliserol + iki yağ asidi']]))
    add('<p>Monomerler, <b>tek tip bir kimyasal bağlanma tepkimesinin tekrarıyla</b> polimer oluşturur. Hücreler <b>üç tip büyük polimer (macromolecule)</b> yapar: <b>polysaccharides, proteins, nucleic acids</b>. '
        'Bunlardan <b>proteinler ve nükleik asitler</b> en fazla <b>bilgi karmaşıklığına</b> sahiptir. Moleküller <b>kovalent ve kovalent olmayan</b> etkileşimlerle kararlı tutulur. '
        'Proteinler hücreye yapı verir ve <b>hücresel işlerin çoğunu yapar</b> (hormon sinyali, iyon kanalı, enzim); nükleik asitler protein yapmak için gereken bilgiyi <b>doğru zamanda ve yerde</b> taşır.</p>')
    k.h3('Genom ve kromozomlar')
    add('<p><b>Genome</b>: bir organizmanın <b>DNA\'sının tamamı</b>. Ökaryotta DNA\'nın çoğu çekirdekte, <b>kromozomlar</b> halinde katlanmıştır; her kromozom <b>tek bir doğrusal DNA molekülü</b> ve ona bağlı proteinlerden oluşur. '
        'Hücre bölünürken çift sarmalın iki zinciri ayrılır ve orijinaliyle aynı iki çift sarmal oluşur (hızlı ve çok doğru kopyalama). '
        'Yumurta ve sperm dışında her normal insan hücresinde <b>46 kromozom</b> vardır; yarısı anneden, yarısı babadan. Mitozun ortasında tam yoğunlaşmış kromozomların büyüklüğe göre çiftler halinde dizilmesine <b>karyotype</b> denir.</p>')
    k.h3('Mutasyonlar: iyi, kötü ya da etkisiz')
    add('<p>Mutasyonlar DNA kopyalanırken <b>kendiliğinden</b>, <b>radyasyonla</b> ya da <b>kimyasal zehirlerle</b> (ör. sigara dumanı) oluşabilir. Biçimleri: bir nükleotidin başkasıyla değişmesi (<b>substitution</b>), '
        '<b>deletion, insertion, inversion</b> ve bir DNA parçasının başka kromozoma geçmesi (<b>translocation</b>). Örnek: <b>insertion → Huntington hastalığı</b>. '
        'Bir canlı için hata, başkası için avantaj olabilir: <b>albinizm</b> çoğu canlıda dezavantajdır ama kutup ayısı, kar tavuğu, kutup tilkisi ve kar ayakkabılı tavşan beyaz kamuflajını albino atalarına borçludur. '
        'Genetik benzerlik (slayt): insan–insan <b>%99,9</b>, insan–şempanze %96–99, insan–kedi %90, insan–muz %60.</p>')
    add(TIP('📏 Boyut ve yüzey', '<p>Kıvrımlar ve çıkıntılar yüzey alanını artırır; bağırsak, akciğer ve beyin sınırlı bir hacimde işlev kapasitesini böyle büyütür.</p>'))
    add(KAV((T('Water', 'su'), 'hücredeki en bol molekül (%70+); polar, hidrojen bağı'),
            (T('Three macromolecules', 'üç makromolekül'), 'polysaccharides, proteins, nucleic acids'),
            (T('Genome', 'genom'), 'organizmanın DNA\'sının tamamı'),
            (T('Karyotype', 'karyotip'), 'kromozomların büyüklüğe göre çiftler halinde dizilmesi'),
            (T('Human chromosomes', 'insan kromozomu'), '46 (yumurta ve sperm hariç)'),
            (T('DNA vs RNA', 'DNA ve RNA'), 'DNA: timin + deoksiriboz · RNA: urasil + riboz')))
    add(EXAM(
        ('The most abundant molecule in cells is:', ['protein', 'DNA', 'water', 'lipid'], 'C', 'Su, hücre kütlesinin %70 ve fazlası.'),
        ('Water can form hydrogen bonds with other water molecules because it is:', ['nonpolar', 'polar', 'hydrophobic', 'a macromolecule'], 'B', 'Polar molekül.'),
        ('Which of the following is NOT one of the three types of macromolecules (large polymers) produced by cells, according to the lecture?', ['polysaccharides', 'proteins', 'nucleic acids', 'vitamins'], 'D', 'Vitaminler küçük moleküldür.'),
        ('RNA differs from DNA in that RNA contains:', ['thymine and deoxyribose', 'uracil and ribose', 'uracil and deoxyribose', 'thymine and ribose'], 'B', 'DNA: timin + deoksiriboz; RNA: urasil + riboz.'),
        ('With the exception of eggs and sperm, every normal human cell has ___ chromosomes.', ['23', '44', '46', '48'], 'C', '46; yarısı anneden yarısı babadan.'),
        ('Chromosomes arranged in pairs in descending order of size is called a:', ['genome', 'karyotype', 'nucleoid', 'chromatid'], 'B', 'Karyotip.'),
        ('Epinephrine is an example of a small molecule that acts as a:', ['structural protein', 'signal (hormone)', 'polysaccharide', 'nucleotide'], 'B', 'Epinefrin: fight-or-flight yanıtını harekete geçiren küçük hormon.'),
        ('Which mutation type is given in the lecture as the cause of Huntington disease?', ['deletion', 'insertion', 'inversion', 'translocation'], 'B', 'Slayt: Insertion: Huntington disease.'),
    ))
