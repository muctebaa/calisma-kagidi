"""Bölüm 18: Mitochondria (Prof. Dr. Ayşe Kevser Özden) — DOC-20261109 dosyası, 32 sayfa."""
from ortak import E, T, mito_svg

BOLUMLER = [('18', 'Mitokondri: yapı, 4 bölme, enerji, kalsiyum, apoptoz, mtDNA', 'Mitochondria (A. K. Özden)')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM, CHAIN = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM, k.CHAIN

    k.h2('18 · Mitokondri (Mitochondria)')
    add('<p><b>Mitochondrion</b> sözcüğü Yunanca <b>mitos</b> (<b>iplik</b>) ve <b>chondrion</b> (<b>granül, tanecik</b>) sözcüklerinden gelir. <b>Richard Altmann</b> mitokondriyi <b>1890</b>\'da keşfetti ve <b>"bioblasts"</b> adını verdi; '
        '<b>Carl Benda</b> <b>1898</b>\'de <b>"mitochondrion"</b> terimini kullandı.</p>'
        '<p>Mitokondri büyük olasılıkla bir ökaryot hücre ile eski bir bakteri arasındaki <b>endosimbiyotik ilişkinin</b> sonucu evrimleşti. Bu kuram <b>çift zarı</b>, <b>kendi genomunu (mtDNA)</b> ve çekirdekle ilişkisini açıklar. '
        'Bugünkü görüş: mitokondri yalnız enerji üreten bağımsız bir organel değil, <b>anneden kalıtılan</b> genomunu aktaran ve birçok hücresel süreçte <b>etkin rol oynayan</b> bir yapıdır.</p>')
    add(TABLE(['Mitokondrinin 4 ana görevi (slayt)'], [['I · <b>ATP production</b> (enerji üretimi)'], ['II · Metabolik tepkimelerin bazı adımlarını yürütmek (other metabolic functions)'],
                                                       ['III · <b>Ca²⁺ storage</b> ve sinyal iletimi (signal transduction)'], ['IV · <b>Apoptosis induction</b> (apoptozu başlatma)']]))
    add('<p>Mitokondri <b>çok dinamik</b> bir organeldir: şekli ve hücre içindeki yönelimi sürekli değişir; <b>ER ve çekirdekle etkileşir</b>; hücrenin enerji ihtiyacına göre (ör. hücre bölünmesi, kas kasılması) <b>bölünüp sayısını artırır</b>. '
        'Farklı dokularda aynı görünse de işlevleri farklıdır: <b>kalp</b> mitokondrisinin iç zarı daha kalındır ve ATP sentez kapasitesi <b>karaciğerdekinden yüksektir</b>.</p>')
    k.h3('Yapı ve 4 bölme')
    add('<p>Çift zarlı, oval–küresel bir organeldir; boyut <b>0,2–5,0</b> (slaytta "mm" yazıyor; doğrusu <b>µm</b>, <i>genel bilgi</i>). <b>4 ana bölmeden</b> oluşur:</p>')
    add(mito_svg())
    add(TABLE(['Bölme', 'Özellik ve görev'], [
        [E('Outer mitochondrial membrane', 'dış zar'), 'sitozol ile iç bölmeler arasında metabolit, iyon ve sinyal molekülü alışverişinin ana arayüzü; <b>VDAC</b> kanalları iyon ve <b>&lt; 5 kD</b> küçük polar moleküllere geçirgenlik sağlar · '
         '<b>TOM complex</b> (translocase of the outer membrane): çekirdekte kodlanan proteinleri içeri alır · <b>MFNs (mitofusins)</b>: kaynaşma (fusion) · ER ile temas noktaları (lipit ve kalsiyum aktarımı) · '
         'geçirgen hale gelince <b>sitokrom c</b> gibi faktörleri sitozole bırakarak <b>apoptozu</b> düzenler · fusion ve fission (birleşme–bölünme) dinamiği'],
        [E('Intermembrane space', 'zarlar arası boşluk'), 'iki zar arası; <b>proton elektrokimyasal gradyanı</b> burada oluşur (<b>proton deposu</b>); sitokromlar, <b>sitokrom c deposu</b>; protein katlanması; '
         '<b>SOD</b> (superoxide dismutase): zararlı süperoksit radikallerini O₂ ve H₂O₂\'ye çevirir'],
        [E('Inner mitochondrial membrane', 'iç zar'), 'dış zara göre <b>geçirgen değildir</b>; <b>elektron taşıma zinciri</b> bileşenleri ve <b>ATP synthase</b> buradadır → <b>ATP burada sentezlenir</b>; elektron taşınması ve H⁺ pompalanması; '
         'çok kıvrımlıdır (<b>cristae</b>) → yüzey alanı artar; yapısal bileşenler: <b>cardiolipin</b>, <b>OPA1</b> (Optic Atrophy 1 protein), <b>MICOS</b> (Mitochondrial Contact Site and Cristae Organizing System); '
         'özel taşıyıcılar: <b>pyruvate</b>, <b>ATP/ADP</b>'],
        [E('Matrix', 'matriks'), '<b>TCA (Krebs) döngüsü</b> burada tamamlanır; <b>mtDNA</b> kopyalanır ve yazılır; mitokondri ribozomlarında protein sentezi ve gen ifadesinde görevli RNA-protein kompleksleri (<b>RNA granules</b>); '
         '<b>SOD2</b> (mitokondriyal süperoksit dismutaz: oksijen radikallerini O₂ ve H₂O₂\'ye çevirir); <b>yağ asidi katabolizması</b>; <b>üre detoksifikasyonu</b>']]))
    k.h3('I · Enerji üretimi')
    add(CHAIN([('Glucose', 'sitozol'), ('Glycolysis', '→ pyruvic acid'), ('Pyruvate', 'matrikse taşınır'), ('Acetyl CoA', 'oksidasyonla'), ('TCA (Krebs) cycle', 'NADH + FADH₂'),
               ('Electron transport chain', 'iç zar'), ('H⁺ pumping', 'zarlar arası boşluğa'), ('F₁F₀-ATP synthase', 'H⁺ geri akışıyla'), ('ATP', '')],
              title='Mitokondride ATP üretimi', note='Şema bu kağıt için çizildi. NADH ve FADH₂ indirgeyici moleküllerdir; protonlar (H⁺) bunlardan gelir.'))
    add('<p>Glikoz sitozolde <b>glikoliz</b> ile <b>pirüvik aside</b> çevrilir. Pirüvat mitokondriye, oradan <b>matrikse</b> taşınır; önce <b>Acetyl CoA</b>\'ya oksitlenir, sonra <b>sitrik asit döngüsüne</b> girer. TCA döngüsü <b>NADH ve FADH₂</b> verir; '
        'bunlar iç zardaki elektron taşıma sistemine gönderilir. Elektron taşıma zinciri boyunca akış, <b>H⁺\'nin zarlar arası boşluğa pompalanmasıyla</b> sonuçlanır; oluşan <b>H⁺ gradyanı</b> <b>F₁F₀-ATP synthase</b>\'ı uyararak ATP ürettirir.</p>')
    add(TIP('📝 Küçük not: TCA döngüsü', '<p>TCA (Krebs) döngüsü yalnız enerji yolu değildir, <b>biyosentez yollarına da katkı verir</b>: ör. <b>sitrat</b> sitozole geçer ve <b>yağ asidi ve kolesterol sentezi</b> için <b>asetil-CoA</b> kaynağı olur. '
        'Krebs döngüsünde üretilen NADH ve FADH₂\'den gelen protonlar ATP sentezinde kullanılır.</p>'))
    k.h3('II · Diğer metabolik görevler')
    add('<p>TCA döngüsünün ara ürünleri sitozole geçip <b>yağ asidi, kolesterol, nükleotit, hem ve amino asit</b> sentezine katılır. Moleküler oksijen içerdiği için metabolik tepkimelerdeki oksidasyon adımları mitokondride tamamlanır. '
        'Bu yüzden mitokondri <b>anabolizma ve katabolizmanın kavşak noktalarından</b> biridir.</p>')
    k.h3('III · Kalsiyum deposu ve sinyalleşme')
    add(TABLE(['Kalsiyum derişimi', 'Değer'], [['Hücre dışı', '<b>1–2 mM</b>'], ['Sitozol', '<b>100 nM</b>'], ['Hücre içi depolar', '<b>endoplazmik retikulum ve mitokondri</b> (Ca²⁺ pompalarıyla)']]))
    add('<p>Hormon sinyalleri hücrede Ca²⁺\'u artırır; Ca²⁺ özel enzimleri ve proteinleri etkinleştirir: <b>Ca²⁺ ikincil habercidir (second messenger)</b>. '
        '"<b>Mitochondrial signalisation</b>" terimi ilk kez <b>1990\'larda</b>, apoptozu başlatan <b>sitokrom c salınımının</b> keşfiyle kullanıldı. '
        'Oksidatif stres ve mitokondriyal ROS (<b>mtROS</b>) da sinyal görevi görür. <b>Mitohormesis</b>: düşük düzeydeki mitokondriyal stres organizmanın sağlığı ve yaşam süresi için <b>yararlıdır</b>; '
        'egzersizin metabolizmaya bazı iyi etkileri buna bağlı olabilir. Egzersizle ilgili mitohormezis ROS üretimini ve <b>mitochondria-derived peptides (MDPs)</b> salınımını içerir: mtDNA\'da kodlanan, yararlı metabolik etkileri olan küçük peptitler.</p>')
    k.h3('IV · Apoptozdaki rolü')
    add('<p>Programlı hücre ölümü dış ya da iç etkilerle başlayabilir. <b>Mitokondriyal yol</b>, <b>sitokrom c\'nin mitokondriden salınmasıyla</b> başlar.</p>')
    k.h3('Mitokondri DNA\'sı (mtDNA)')
    add(TABLE(['Özellik', 'mtDNA'], [
        ['Keşif', '<b>Margit Nass ve Sylvan Nass, 1963</b>; ilk tam dizi <b>18 yıl sonra, 1981</b>'],
        ['Yapı', '<b>halkasal (circular)</b>, çift zincirli, <b>histonsuz</b>'],
        ['Büyüklük', 'yaklaşık <b>16.569 baz çifti</b>'],
        ['Gen sayısı', 'yalnız <b>37 gen</b>: oksidatif fosforilasyon için <b>13 protein</b> + <b>22 tRNA</b> + <b>2 rRNA</b>'],
        ['Kopya sayısı', 'çekirdek DNA\'sı hücrede 2 kopya; bir hücrede <b>yüzlerce–binlerce</b> mtDNA kopyası'],
        ['Kalıtım', '<b>yalnız anneden</b>; spermin mitokondrileri döllenmede genellikle yok edilir'],
        ['Hassasiyet', 'elektron taşıma zincirine yakın ve histonsuz olduğu için <b>oksidatif hasara açık</b>; mtDNA hasarı: <b>yaşlanma</b>, <b>mitokondriyal hastalıklar</b>, <b>kanser</b>']]))
    add(TIP('🏁 Take home message', '<p>Mitokondri yalnız enerji üretim yeri değildir; hücrenin <b>metabolik durumunu, redoks durumunu ve stres yükünü</b> hücresel kararlara ve hücrenin kaderine dönüştüren bir merkezdir.</p>'))
    add(TRAP('Rakamları karıştırma', '<p>mtDNA: <b>16.569 bp · 37 gen = 13 protein + 22 tRNA + 2 rRNA</b> · 1963 keşif, 1981 dizi · dış zar VDAC <b>&lt; 5 kD</b> (Özden) · Yılmaz\'ın slaytında dış zar "<b>10.000 daltona kadar</b> geçirgen". '
        'Ca²⁺: hücre dışı <b>1–2 mM</b>, sitozol <b>100 nM</b>. Altmann <b>1890</b> (bioblasts), Benda <b>1898</b> (mitochondrion).</p>'))
    add(KAV((T('Mitochondrion etymology', 'mitokondri sözcüğü'), 'mitos = iplik, chondrion = granül'),
            (T('Altmann / Benda', 'Altmann / Benda'), '1890 keşif "bioblasts" / 1898 "mitochondrion" terimi'),
            (T('VDAC', 'VDAC kanalı'), 'dış zarda; iyon ve < 5 kD küçük polar moleküller'),
            (T('TOM complex', 'TOM kompleksi'), 'dış zar; çekirdekte kodlanan proteinleri içeri alır'),
            (T('Mitofusins (MFNs)', 'mitofüzinler'), 'dış zar; mitokondri kaynaşması (fusion)'),
            (T('Cardiolipin, OPA1, MICOS', 'iç zar yapı bileşenleri'), 'kristaları oluşturan yapısal bileşenler'),
            (T('SOD / SOD2', 'süperoksit dismutaz'), 'süperoksiti O₂ + H₂O₂\'ye çevirir; SOD zarlar arası, SOD2 matriks'),
            (T('F₁F₀-ATP synthase', 'ATP sentaz'), 'iç zarda; H⁺ gradyanıyla ATP yapar'),
            (T('Mitohormesis', 'mitohormezis'), 'düşük mitokondriyal stres yararlıdır; egzersiz, ROS, MDP'),
            (T('mtDNA', 'mtDNA'), 'halkasal, histonsuz, 16.569 bp, 37 gen; anneden; çok kopyalı; oksidatif hasara açık')))
    add(EXAM(
        ('Who discovered mitochondria in 1890 and called them "bioblasts"?', ['Carl Benda', 'Richard Altmann', 'Margit Nass', 'Robert Brown'], 'B', 'Altmann 1890; Benda 1898 "mitochondrion" terimi.'),
        ('In which mitochondrial compartment is the TCA (Krebs) cycle completed?', ['outer membrane', 'intermembrane space', 'inner membrane', 'matrix'], 'D', 'Matriks.'),
        ('The components of the electron transport chain and ATP synthase are located in the:', ['outer membrane', 'inner membrane', 'matrix', 'cytosol'], 'B', 'İç zar; ATP burada sentezlenir.'),
        ('The proton electrochemical gradient (proton reservoir) forms in the:', ['matrix', 'intermembrane space', 'cytosol', 'nucleus'], 'B', 'Zarlar arası boşluk.'),
        ('Which complex imports nuclear-encoded proteins through the outer mitochondrial membrane?', ['MICOS', 'TOM complex', 'OPA1', 'VDAC'], 'B', 'TOM = translocase of the outer membrane.'),
        ('Human mitochondrial DNA contains only 37 genes, which encode:', ['13 proteins, 22 tRNAs and 2 rRNAs', '37 proteins', '22 proteins, 13 tRNAs and 2 rRNAs', '2 proteins, 22 tRNAs and 13 rRNAs'], 'A', '16.569 bp, halkasal, histonsuz.'),
        ('Mitochondrial DNA is inherited:', ['from both parents equally', 'exclusively from the mother', 'exclusively from the father', 'randomly'], 'B', 'Sperm mitokondrileri döllenmede yok edilir.'),
        ('Why is mtDNA vulnerable to oxidative damage?', ['It is linear and long', 'It is close to the electron transport chain and has no histones', 'It is in the cytosol', 'It has many introns'], 'B', 'Hasar: yaşlanma, mitokondriyal hastalık, kanser.'),
        ('The mitochondrial pathway of apoptosis starts with the release of:', ['ATP', 'cytochrome c', 'calcium only', 'mtDNA'], 'B', 'Sitokrom c salınımı.'),
        ('Low levels of mitochondrial stress that are beneficial for health and survival describe:', ['apoptosis', 'mitohormesis', 'autophagy', 'fission'], 'B', 'Mitohormezis; egzersiz, ROS, MDP.'),
        ('Cytosolic calcium concentration is about ___ whereas extracellular calcium is ___ .', ['100 nM / 1–2 mM', '1–2 mM / 100 nM', '1 µM / 1 nM', 'equal in both'], 'A', 'Sitozolde çok düşük; ER ve mitokondri depolar.'),
        ('Mitochondria of the heart, compared with those of the liver, have:', ['a thinner inner membrane', 'a thicker inner membrane and higher ATP synthetic capacity', 'no cristae', 'no mtDNA'], 'B', 'Slayt örneği.'),
    ))
