"""Bölüm 10–12: Cell Membranes and Organelles (cell 1.pdf, Dr. Selma Yılmaz) — zar yapısı, lipitler, proteinler.
(Zar taşınımı s_mt içinde, Özden'in dosyasıyla birlikte.)"""
from ortak import E, T, zar_svg

BOLUMLER = [('10', 'Hücre zarı: görevleri, akışkan mozaik model, zar yüzleri', 'Cell 1 (S. Yılmaz)'),
            ('11', 'Zar lipitleri: fosfolipitler, glikolipitler, kolesterol, akışkanlık', 'Cell 1'),
            ('12', 'Zar proteinleri ve glikoproteinler', 'Cell 1')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM

    # ================= 10 =================
    k.h2('10 · Hücre zarı (plasma membrane): görevleri ve yapısı')
    add('<p>' + E('Plasma membrane', 'plazma zarı / hücre zarı') + ' her hücrenin sitoplazmasını çevreler ve hücreyi dış ortamdan ayırır. Prokaryotların zarları ökaryot zarlarına çok benzer. '
        'Ökaryot hücreyi <b>tek bir zar</b> (plazma zarı) çevreler ama içinde zarla sınırlı birçok bölme (<b>organelles</b> ve <b>vesicles</b>) vardır. '
        'Ökaryot hücredeki <b>iç zarların toplam yüzey alanı, plazma zarınınkinden çok daha büyüktür</b>.</p>')
    k.h3('Plazma zarının 5 temel görevi')
    add(TABLE(['#', 'Görev', 'Açıklama'], [
        ['1', E('Protection', 'koruma'), 'sitoplazmayı çevreler, hücrenin dışını belirler; hareket, salgılama ve uyarı iletiminde rol alabilir'],
        ['2', E('Regulation of passage of materials', 'madde geçişini düzenleme'), 'sitozol ile hücre dışı arasındaki madde hareketini kontrol eder; <b>selectively permeable</b> (seçici geçirgen). Geçiş yolları: pasif taşıma (osmoz, basit difüzyon), kolaylaştırılmış difüzyon (iyon kanalları), aktif taşıma (Na⁺-K⁺ pompası), toplu taşıma (ekzositoz, reseptör aracılı endositoz, fagositoz)'],
        ['3', E('Maintenance of differential distribution of ions', 'iyonların farklı dağılımını koruma'), 'hücre içi ve dışındaki iyon farkını korur (ör. <b>membrane potential</b>)'],
        ['4', E('Response to the environment', 'çevreye yanıt'), '<b>receptor proteins</b> ile başka hücrelerden gelen kimyasal mesajları alır: hücre tanıma, hormonlar, büyüme faktörleri, nörotransmitterler'],
        ['5', E('Communication with neighbouring cells', 'komşu hücrelerle iletişim'), 'belirli <b>glycoproteins</b> ile komşu hücrelerle yapısal ve kimyasal ilişki kurar']]))
    k.h3('Akışkan mozaik model (Fluid Mosaic Model)')
    add('<p>Zarın yapısına <b>Fluid Mosaic Model</b> denir, çünkü zar <b>katıdan çok sıvı gibi davranır</b>. Bu modele göre zar, <b>fosfolipit ve protein moleküllerinden oluşan iki boyutlu bir mozaiktir</b>; proteinler akışkan lipit çift katmanında "yüzer". '
        'Zarın iki bileşeni: <b>membrane lipids</b> (fosfolipitler, glikolipitler, kolesterol) ve <b>membrane proteins</b> (integral, peripheral, lipid-anchored ve glikoproteinler).</p>')
    add(zar_svg())
    k.h3('Prokaryot ve ökaryot zarı arasındaki 2 fark')
    add(TABLE(['', 'Prokaryot', 'Ökaryot'], [
        ['<b>Electron transport chain (ETC)</b> ve fotosentez proteinleri', 'hücre zarında', 'hücre zarında <b>değil</b>; organellerde (ETC → <b>mitokondri</b>, fotosentez → <b>kloroplast</b>)'],
        ['<b>Cholesterol</b>', 'yok (yalnız <b>mycoplasma</b>)', 'var']]))
    k.h3('Zarın yüzleri')
    add('<p>Her hücre zarının bir <b>cytosolic face</b> (iç yüz: bölmenin içine bakan taraf) ve bir <b>external / exoplasmic face</b> (dış yüz: ortama bakan taraf) vardır. '
        '<b>Üç organel iki zarla</b> çevrilidir ve iki zar arasında dar bir <b>intermembrane space</b> bulunur: <b>nucleus, mitochondrion, chloroplast</b>.</p>')
    add(KAV((T('Fluid Mosaic Model', 'akışkan mozaik model'), 'zar = fosfolipit ve proteinlerden oluşan iki boyutlu mozaik; sıvı gibi davranır'),
            (T('Selectively permeable', 'seçici geçirgen'), 'zar yalnız belirli maddelerin geçişine izin verir'),
            (T('Double-membrane organelles', 'çift zarlı organeller'), 'nucleus, mitochondrion, chloroplast'),
            (T('ETC location', 'ETZ yeri'), 'prokaryotta hücre zarı; ökaryotta mitokondri')))
    add(EXAM(
        ('According to the fluid mosaic model, the membrane is viewed as:', ['a rigid protein sheet', 'a two-dimensional mosaic of phospholipid and protein molecules', 'a single layer of cholesterol', 'a carbohydrate wall'], 'B', 'Zar katıdan çok sıvı gibi davranır.'),
        ('Which three organelles are enclosed by two membranes separated by an intermembrane space?', ['nucleus, mitochondrion, chloroplast', 'Golgi, ER, lysosome', 'ribosome, centriole, nucleolus', 'peroxisome, vacuole, lysosome'], 'A', 'Çift zarlı organeller.'),
        ('In eukaryotic cells, the proteins of the electron transport chain are found in the:', ['plasma membrane', 'mitochondrial membranes', 'cell wall', 'Golgi apparatus'], 'B', 'Prokaryotta ETZ hücre zarındadır; ökaryotta mitokondride.'),
        ('Which function of the plasma membrane is performed by receptor proteins?', ['Protection', 'Response to the environment (receiving chemical messages)', 'Synthesis of DNA', 'Storage of energy'], 'B', 'Reseptörler hormon, büyüme faktörü ve nörotransmitterleri tanır.'),
        ('The total surface area of internal membranes in a eukaryotic cell is ___ the plasma membrane.', ['much smaller than', 'equal to', 'far greater than', 'unrelated to'], 'C', 'Slayt: far exceeds that of the plasma membrane.'),
    ))

    # ================= 11 =================
    k.h2('11 · Zar lipitleri')
    add(TABLE(['Ana zar lipitleri', 'Alt gruplar'], [
        ['1 · ' + E('Phospholipids', 'fosfolipitler'), 'a) <b>Phosphoglycerides</b> (glycerophospholipids) · b) <b>Sphingolipids</b>'],
        ['2 · ' + E('Glycolipids', 'glikolipitler'), '<b>glycosphingolipids</b>: gangliosides, cerebrosides'],
        ['3 · ' + E('Cholesterol', 'kolesterol'), 've diğer steroidler']]))
    k.h3('Fosfolipitler')
    add('<p>Zar lipitlerinin çoğu fosfolipittir. Fosfolipitler <b>polar, iyonik</b> bileşiklerdir; <b>bir ya da iki uzun yağ asidi</b> (hidrofobik hidrokarbon zinciri) bir <b>hidrofilik baş grubuna</b> bağlıdır. '
        'Simetrik çift katmanda <b>hidrofilik fosfat başları</b> sulu ortama bakar, <b>hidrofobik yağ asidi kuyrukları</b> ortadadır. Bütün biyolojik zarların temel yapısı bu fosfolipit çift katmanıdır.</p>')
    add(TABLE(['', E('Phosphoglycerides', 'fosfogliseritler / gliserofosfolipitler'), E('Sphingolipids', 'sfingolipitler')], [
        ['İskelet', '<b>glycerol</b>', '<b>sphingosine</b> (uzun doymamış hidrokarbon zincirli bir amino alkol); gliserol <b>yok</b>'],
        ['Yağ asidi', '<b>2</b> yağ açil zinciri', '<b>1</b> yağ asidi'],
        ['Formül (slayt)', 'glycerol + 2 fatty acyl + phosphate + polar head', 'sphingosine + 1 fatty acyl + phosphate + polar head'],
        ['Not', 'zarlardaki <b>en bol</b> lipit sınıfı; alkol, fosfodiester köprüsüyle <b>diacylglycerol</b>\'e bağlı; açil zincirleri genelde <b>16 ya da 18</b> karbon, <b>0, 1 ya da 2</b> çift bağ; baş grubuna göre adlandırılır', 'alkol, fosfodiester köprüsüyle sfingozine bağlı'],
        ['Örnek', '<b>PC</b> phosphatidylcholine (kolin + diasilgliserol), <b>PE</b> phosphatidylethanolamine, <b>PS</b> phosphatidylserine, <b>PI</b> phosphatidylinositol', '<b>Sphingomyelin (SM)</b>: sfingozin + fosfokolin ya da fosfoetanolamin; bazı sinir aksonlarını saran <b>myelin sheath</b>\'te bol']]))
    k.h3('Glikolipitler')
    add('<p><b>Glycolipids</b>: fosfat grubu yerine <b>şeker birimi</b> içerir; karbonhidrat zinciri gliserol ya da sfingozin iskeletine bağlıdır (slayt formülü: gliserol + 2 yağ açil + şeker ya da <b>sfingozin + 1 yağ açil + şeker</b>). '
        'Genellikle ökaryot zarlarının <b>dış (hücre dışı) yüzünde</b> bulunur. <b>Ceramide</b> = sfingozin + uzun zincirli yağ asidi (mumsu lipitler). En basit glikolipit <b>glucosylcerebroside</b>: seramide bağlı tek glikoz.</p>')
    add(TABLE(['İki glikolipit sınıfı', 'Yapı'], [
        [E('Gangliosides', 'gangliyozitler'), '<b>çok sayıda karmaşık karbonhidrat zinciri</b> + sfingolipit'],
        [E('Cerebrosides', 'serebrozitler'), '<b>glikoz ya da galaktoz</b> (tek şeker) + sfingolipit']]))
    add(TIP('🍬 Lipit ve proteinlere bağlı karbonhidratların görevleri', '<ul><li>Lipit ve proteinlerin <b>hidrofilik</b> karakterini artırır</li><li>Zarın <b>kararlılığını</b> korur</li><li><b>Hücre–hücre etkileşimini</b> kolaylaştırır</li>'
        '<li>İnsan <b>kan grubu antijenlerinde (ABO)</b> rol alır</li><li>Glikolipitler <b>virüs ve diğer patojenlerin</b> hücreye girmesi için <b>reseptör</b> olur</li></ul>'))
    k.h3('Kolesterol')
    add('<p><b>Cholesterol</b> ve türevleri üçüncü önemli zar lipit sınıfıdır: <b>steroids</b>. Steroidlerin temel yapısı <b>dört halkalı hidrokarbondur</b>; kolesterolde bir halkada <b>hidroksil (–OH)</b> grubu vardır. '
        'Neredeyse tamamen hidrokarbon olmasına rağmen kolesterol <b>amphipathic</b>tir (hem suyu seven hem sudan kaçan kısmı var), çünkü <b>hidroksil grubu suyla etkileşebilir</b>. '
        'Amfipatik moleküller suda kendiliğinden <b>micelle</b> ya da <b>liposome</b> oluşturur.</p>'
        '<p>Kolesterol <b>memeli hücrelerinin plazma zarında çok bol</b>, <b>çoğu prokaryotta yok</b>. Bitki plazma zarı lipitlerinin <b>%30–50</b>\'si bitkiye özgü steroidlerdir. '
        'Kolesterol <b>zar sentezi</b> ve <b>kolesterol metabolizması</b> (safra asidi ve steroid sentezi) için gereklidir; zarın <b>akışkanlığını korumada</b> önemlidir, normal hücre büyümesi ve üremesi için şarttır.</p>')
    k.h3('Zar akışkanlığı ve asimetri')
    add(TABLE(['Akışkanlığı', 'Ne yapar?'], [
        ['<b>Sphingolipids</b> ve <b>cholesterol</b>', '<b>azaltır</b> ↓'],
        ['<b>Phosphoglycerides</b>', '<b>artırır</b> ↑'],
        ['Isıtma', 'çift katman dar bir sıcaklık aralığında <b>jel benzeri</b> halden <b>daha akışkan</b> hale geçer (phase transition)']]))
    add('<p>Doğal zarlar düşük viskoziteli, <b>sıvı benzeri</b> kıvamdadır. Lipit bileşimi zarın <b>kalınlığını ve eğriliğini</b> de etkiler (ör. SM içeren bölge PC içerenden kalındır). '
        '<b>Asimetri:</b> fosfolipitler ve sfingolipitler iki tabakaya <b>asimetrik</b> dağılır; <b>kolesterol iki tabakaya oldukça eşit</b> dağılır. Lipitlerin ve integral proteinlerin çoğu zarda <b>yanlamasına (lateral) hareket eder</b>.</p>')
    add(TRAP('Flip-flop', '<p><b>Proteinler hiçbir zaman flip-flop yapmaz</b> (bir tabakadan öbürüne geçmez; enerji açısından elverişsiz). Saf fosfolipit çift katmanında fosfolipitler de flip-flop yapmaz. '
        'Doğal bazı zarlarda fosfolipitler <b>ara sıra</b> flip-flop yapar; bunu <b>flippases</b> adlı zar proteinleri katalizler. <b>Lateral (yanlamasına) hareket</b> ise lipit ve proteinlerin çoğunda serbesttir.</p>'))
    add('<p><b>Lipid rafts</b>: kolesterol, sfingolipitler ve bazı zar proteinlerini içeren, çift katman düzleminde oluşan <b>mikrobölgelerdir</b>; plazma zarından <b>sinyal iletimi</b> yerleridir.</p>')
    add(KAV((T('Phosphoglycerides', 'fosfogliseritler'), 'gliserol + 2 yağ açil + fosfat + polar baş; en bol zar lipidi; PC, PE, PS, PI'),
            (T('Sphingolipids', 'sfingolipitler'), 'sfingozin (amino alkol) + 1 yağ asidi + fosfat; gliserol yok; sfingomiyelin (miyelin kılıf)'),
            (T('Glycolipids', 'glikolipitler'), 'fosfat yerine şeker; dış yüzde; gangliyozit, serebrozit'),
            (T('Ceramide', 'seramit'), 'sfingozin + yağ asidi'),
            (T('Cholesterol', 'kolesterol'), 'steroid; 4 halka + OH → amfipatik; akışkanlığı azaltır; mycoplasma dışında prokaryotta yok'),
            (T('Flippases', 'flipazlar'), 'fosfolipit flip-flop\'unu katalizleyen zar proteinleri'),
            (T('Lipid rafts', 'lipit salları'), 'kolesterol + sfingolipit + protein mikrobölgeleri; sinyal yeri')))
    add(EXAM(
        ('Which is the most abundant class of lipids in most membranes?', ['sphingolipids', 'glycerophospholipids (phosphoglycerides)', 'cholesterol', 'gangliosides'], 'B', 'Slayt: the most abundant class of lipids in most membranes.'),
        ('Instead of a glycerol backbone, sphingolipids contain:', ['ceramide', 'sphingosine', 'inositol', 'choline'], 'B', 'Sfingozin: uzun doymamış zincirli amino alkol.'),
        ('Sphingomyelin is found mainly in the:', ['mitochondrial inner membrane', 'myelin sheath surrounding some nerve axons', 'bacterial cell wall', 'nuclear pores'], 'B', 'Miyelin kılıf.'),
        ('Why is cholesterol considered amphipathic?', ['It contains a phosphate group', 'Its hydroxyl group can interact with water', 'It has two fatty acid chains', 'It is a protein'], 'B', 'Neredeyse tamamen hidrokarbon ama OH grubu suyla etkileşir (hoca tekrar sorusu).'),
        ('Membrane fluidity is DECREASED by:', ['phosphoglycerides', 'sphingolipids and cholesterol', 'heating', 'unsaturated fatty acids only'], 'B', 'Fosfogliseritler artırır; sfingolipit ve kolesterol azaltır.'),
        ('Glycolipids that contain multiple complex carbohydrate chains are called:', ['cerebrosides', 'gangliosides', 'sphingomyelins', 'phosphatidylserines'], 'B', 'Serebrozit: tek glikoz/galaktoz; gangliyozit: çok sayıda karmaşık şeker zinciri.'),
        ('Which statement about flip-flop is correct?', ['Proteins frequently flip-flop across the membrane', 'In some natural membranes phospholipids occasionally flip-flop, catalyzed by flippases', 'Cholesterol cannot move laterally', 'Flip-flop is the main way proteins move laterally'], 'B', 'Proteinler asla flip-flop yapmaz.'),
        ('Lipid rafts are microdomains containing:', ['DNA and histones', 'cholesterol, sphingolipids and certain membrane proteins', 'only phosphatidylcholine', 'ribosomes'], 'B', 'Sinyal iletim bölgeleri.'),
        ('Which of the following is NOT a function of carbohydrates bound to membrane lipids and proteins?', ['increasing hydrophilic character', 'maintaining membrane stability', 'facilitating cell–cell interactions', 'synthesizing ATP'], 'D', 'Diğerleri ve ABO kan grubu antijenleri, patojen reseptörleri.'),
    ))

    # ================= 12 =================
    k.h2('12 · Zar proteinleri ve glikoproteinler')
    add('<p>Her zar tipinin kendine özgü işi, içerdiği <b>belirli zar proteinleri</b> sayesindedir. Proteinler akışkan lipit çift katmanında "yüzer".</p>')
    add(TABLE(['Tip', 'Zara nasıl bağlı?', 'Görev / örnek'], [
        [E('Integral (transmembrane) proteins', 'integral proteinler'), 'çift katmanın <b>içine gömülü</b>, zarı boydan boya geçer', 'esas olarak <b>taşıma</b>: <b>carrier (transporter)</b> proteinler belirli maddeleri bağlayıp taşır (ör. şeker taşıyıcıları); <b>pumps</b> molekülleri düşükten yüksek derişime taşır (<b>Na⁺/K⁺-ATPase</b>); <b>channel</b> proteinler küçük, suda çözünen maddelere kanal açar. Örnek: <b>glycophorin A</b> (hidrofobik amino asitler zar içinde; pozitif yüklü kalıntılar negatif fosfolipit başlarına bağlanarak proteini sabitler)'],
        [E('Peripheral proteins', 'periferal proteinler'), 'zar <b>yüzeyine</b> tutunur; çift katmanın hidrofobik çekirdeğine girmez; <b>dolaylı</b> (integral proteinlere bağlanarak) ya da <b>doğrudan</b> (lipit başlarına bağlanarak); iç ya da dış yüzde', 'bazıları enzim; bazıları elektron taşıma zinciri ya da fotosentezde; bazıları bölünmede hücre şekli değişiminde. Örnek: <b>Phospholipase C (PLC)</b>: GPCR → G proteini → PLC-β; <b>PIP₂</b>\'yi <b>DAG</b> ve <b>IP₃</b>\'e dönüştürür (kalsiyum sinyali)'],
        [E('Lipid-anchored proteins', 'lipide bağlı proteinler'), 'bir ya da daha çok lipide <b>kovalent</b> bağlı; lipidin hidrokarbon zinciri bir tabakaya gömülür; <b>polipeptid zincirin kendisi çift katmana girmez</b>', 'üç tip; <b>prenylated proteins</b> ökaryot hücre büyümesi, farklılaşması ve morfolojisi için önemli'],
        [E('Glycoproteins', 'glikoproteinler'), 'proteine kovalent bağlı karbonhidrat; genelde <b>dış yüzde</b>', 'ABO kan grubu antijenleri, hücre tanıma, kararlılık']]))
    add('<p>İntegral proteinlerin çoğu bir ya da birkaç amino asit yan zincirine bağlı dallı şeker grubuyla <b>glikozillenmiştir</b>. <b>Glikoproteinler ve glikolipitler yalnızca exoplasmic (dış) tabakada</b> bulunur; '
        'ökaryot plazma zarında çok boldur, <b>iç mitokondri zarında</b>, kloroplast lamellerinde ve bazı iç zarlarda <b>yoktur</b>. Bütün integral proteinler ve glikolipitler çift katmana sitozolik ve ekzoplazmik yüzlere göre <b>asimetrik</b> bağlanır; '
        'bu asimetri zarın yapısı ve işlevinin temelidir. Protein yönelimindeki <b>mutlak asimetri</b>, iki yüze farklı özellikler kazandırır.</p>')
    k.h3('Plazma zarı proteinlerinin görevleri')
    add('<ul><li>Besinleri içeri, metabolik atıkları dışarı taşımak; sitozolün <b>iyon bileşimini, pH\'sını ve ozmotik basıncını</b> korumak (pompalar, taşıyıcılar, iyon kanalları).</li>'
        '<li>Belirli küçük moleküllerin (basit şekerler, amino asitler, vitaminler) ve iyonların (Na⁺) geçişine izin verip diğerlerini engellemek.</li>'
        '<li>Zarı hücre iskeleti liflerine, <b>hücre dışı matrikse</b> ya da (bakteri ve bitkide) <b>hücre duvarına</b> bağlamak (anchor).</li>'
        '<li>Hücreler arası iletişim: <b>reseptör proteinler</b> hormon gibi sinyal moleküllerini bağlar.</li>'
        '<li>Zara bağlı <b>enzimler</b>, sulu çözeltide zor gerçekleşecek tepkimeleri katalizler.</li>'
        '<li>Hücre gelişimi ve çok hücreli dokuların düzgün çalışması için kritiktir.</li></ul>')
    add(TRAP('Integral ↔ peripheral ↔ lipid-anchored', '<p><b>Integral</b> = zarı geçer, taşıma yapar · <b>Peripheral</b> = yüzeyde, hidrofobik çekirdeğe <b>girmez</b>, PLC · <b>Lipid-anchored</b> = lipide kovalent bağlı, <b>polipeptit zara girmez</b>, prenilasyon.</p>'))
    add(KAV((T('Integral proteins', 'integral proteinler'), 'zarı geçer; taşıyıcı, pompa, kanal; ör. glikoforin A'),
            (T('Peripheral proteins', 'periferal proteinler'), 'yüzeyde; enzim, ETZ, şekil değişimi; ör. fosfolipaz C'),
            (T('Lipid-anchored proteins', 'lipide bağlı proteinler'), 'kovalent lipit bağlı; prenile proteinler büyüme ve farklılaşmada'),
            (T('Phospholipase C', 'fosfolipaz C'), 'PIP₂ → DAG + IP₃ (kalsiyum sinyali)'),
            (T('Glycophorin A', 'glikoforin A'), 'tipik transmembran (integral) protein')))
    add(EXAM(
        ('Integral membrane proteins are mainly involved in:', ['transport', 'DNA replication', 'photosynthesis only', 'cell wall synthesis'], 'A', 'Taşıyıcılar, pompalar, kanallar.'),
        ('Peripheral membrane proteins:', ['span the entire lipid bilayer', 'do not interact with the hydrophobic core of the bilayer', 'are covalently bound to lipids', 'are found only in prokaryotes'], 'B', 'Yüzeyde; dolaylı ya da doğrudan bağlanır.'),
        ('In lipid-anchored proteins:', ['the polypeptide chain spans the bilayer', 'the polypeptide chain itself does not enter the phospholipid bilayer', 'there is no covalent bond', 'the protein is always a pump'], 'B', 'Lipidin hidrokarbon zinciri bir tabakaya gömülür.'),
        ('Phospholipase C (PLC), a peripheral protein, converts PIP2 into:', ['ATP and ADP', 'DAG and IP3', 'glucose and fructose', 'cholesterol and bile acids'], 'B', 'Kalsiyum sinyali.'),
        ('Glycoproteins and glycolipids are found exclusively in the:', ['cytosolic leaflet', 'exoplasmic leaflet', 'inner mitochondrial membrane', 'nuclear matrix'], 'B', 'Dış tabaka; iç mitokondri zarında yok.'),
        ('Which is an example of a typical transmembrane (integral) protein?', ['Glycophorin A', 'Phospholipase C', 'Collagen', 'Actin'], 'A', 'Glikoforin A.'),
        ('Pumps are carrier proteins that move molecules:', ['from high to low concentration without energy', 'against the concentration gradient', 'only water', 'only by vesicles'], 'B', 'Düşükten yüksek derişime, ör. Na⁺/K⁺-ATPaz.'),
    ))
