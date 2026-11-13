"""Bölüm 19–21: Membrane Transport (Prof. Dr. A. Kevser Özden, 54 slayt, görüntüden okundu) + Cell 1'in taşınım kısmı (S. Yılmaz)."""
from ortak import E, T, gecirgenlik_svg

BOLUMLER = [('19', 'Zar taşınımı: geçirgenlik, basit difüzyon, ozmoz, Fick yasası', 'Membrane Transport (Özden) + Cell 1'),
            ('20', 'Kolaylaştırılmış difüzyon: kanallar, taşıyıcılar, GLUT, Michaelis-Menten', 'Membrane Transport + Cell 1'),
            ('21', 'Aktif taşıma: pompalar, Na⁺/K⁺-ATPaz, MDR, kotransport; endositoz ve ekzositoz', 'Membrane Transport + Cell 1')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM, CHAIN = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM, k.CHAIN

    # ================= 19 =================
    k.h2('19 · Zar taşınımı (Membrane Transport): geçirgenlik ve pasif taşıma')
    add('<p>Hücre zarının <b>etkin bir metabolizması</b> vardır: taşıma, enzim tepkimeleri, hücre dışı matrikse bağlanma, hücre–hücre iletişimi ve tutunma, çeşitli <b>ligandlara</b> (hormonlar, büyüme faktörleri, kimyasal sinyaller) bağlanma. '
        'Yaşam suda başladı; hücreler <b>kan plazmasından türeyen doku sıvısına</b> gömülüdür. Doku sıvısı glikoz, iyonlar ve gazlar içerir. Hücre içi ve dışının bileşimi farklıdır: <b>hücre içinde potasyum (K⁺), doku sıvısında sodyum (Na⁺) fazladır</b>.</p>'
        '<p>Zar <b>çok incedir (60–100 Å)</b> ve lipit ile proteinlerden oluşan <b>iki boyutlu bir sıvı</b> gibidir. Zar <b>semipermeable (selectively permeable)</b>, yani seçici geçirgendir; çünkü: iç kısmı <b>hidrofobiktir</b>, '
        '<b>kanallar</b> ve <b>pompalar</b> içerir, <b>pinositoz reseptörleri</b> vardır ve bu moleküllerin zardaki ifadesi değişebilir. <b>Lipit çift katmanı polar maddeleri geçirmez</b>; bunlar <b>taşıyıcı sistemler, kanallar ve pompalarla</b> taşınır.</p>')
    add(gecirgenlik_svg())
    add('<p>Grafikteki geçirgenlik sırası: <b>O₂ &gt; CO₂ ≈ H₂O &gt; glycerol</b> (çift katmandan doğrudan); <b>K⁺, Na⁺, Cl⁻</b> ise çift katmandan neredeyse hiç geçmez, zarda geçebilmeleri <b>taşıma proteinleri</b> sayesindedir.</p>')
    k.h3('Taşınım tipleri (genel tablo)')
    add(TABLE(['Tip', 'Enerji?', 'Yön', 'Nasıl?', 'Yasa (slayt)'], [
        ['<b>Simple diffusion</b> (basit difüzyon)', 'yok', 'yüksek → düşük derişim', 'doğrudan çift katmandan (apolar ve küçük polar)', '<b>Fick</b>'],
        ['<b>Osmosis / bulk flow</b> (ozmoz, toplu akış)', 'yok', 'serbest suyun çok olduğu yerden az olduğu yere', 'çift katmandan + <b>aquaporin</b> kanalından', '<b>Poiseuille</b> (kanal)'],
        ['<b>Facilitated diffusion</b> (kolaylaştırılmış difüzyon)', 'yok (pasif)', 'derişim gradyanı yönünde', '<b>kanal</b> ya da <b>taşıyıcı (carrier)</b> protein', '<b>Michaelis–Menten</b> (taşıyıcı)'],
        ['<b>Active transport</b> (aktif taşıma)', '<b>var (ATP)</b>', '<b>gradyana karşı</b>', '<b>pompa</b>', 'metabolik'],
        ['<b>Endocytosis / exocytosis</b>', 'var', 'büyük moleküller', 'kesecik (vesicle)', '—']]))
    k.h3('Basit difüzyon ve Fick yasası')
    add('<p><b>Simple diffusion</b>: parçacıkların çözeltideki hareketiyle gerçekleşir; parçacıklar <b>yüksek derişimden düşük derişime</b> geçer. Lipitte çözünen moleküller (<b>O₂, CO₂</b>) zardan serbestçe difüze olur; etanol gibi <b>küçük polar</b> moleküller de geçebilir. '
        'Yılmaz\'ın slaytına göre plazma zarı sitoplazmaya erişimde her zaman bir engeldir ve hücreye girişin çoğu zar proteinleri gerektirir.</p>')
    add(TABLE(['Fick\'in birinci difüzyon yasası (elektrolit olmayan madde)', 'Gazlar (O₂, CO₂) için'], [[
        '<b>J = P · A · (C<sub>A</sub> − C<sub>B</sub>)</b><br>J = net difüzyon hızı (mmol/s) · P = maddenin geçirgenliği (cm/s) · <b>A = difüzyon yüzey alanı</b> (cm²) · C<sub>A</sub> − C<sub>B</sub> = <b>derişim gradyanı</b>',
        '<b>Hız = k × A × (P₂ − P₁) / D</b><br>k = difüzyon sabiti (gazın çözünürlüğü ve sıcaklığa bağlı) · A = gaz alışveriş alanı · P₂ − P₁ = iki taraftaki <b>kısmi basınç farkı</b> · <b>D = mesafe (engelin kalınlığı)</b>']]))
    add(TIP('💡 Formülü sözle hatırla', '<p>Difüzyon hızı <b>yüzey alanı</b> ve <b>derişim (ya da basınç) farkı</b> ile <b>artar</b>, <b>engelin kalınlığı (D)</b> ile <b>azalır</b>. Bu yüzden bağırsak ve akciğerin yüzeyi kıvrımlarla büyütülmüştür.</p>'))
    k.h3('Ozmoz ve aquaporin')
    add('<p><b>Osmosis</b>: suyun yarı geçirgen zardan, <b>serbest suyun daha çok olduğu</b> (çözünen az) taraftan <b>daha az olduğu</b> (çözünen çok) tarafa geçmesidir (slayt özeti: <b>hypo → hyper</b>). Şeker molekülleri porlardan geçemez, su geçer; su molekülleri şekerin çevresinde kümelenir. '
        'Su hücreye ozmozla girer ve çıkar; bunun için <b>su kanalı proteinleri</b> gerekir. Su hem çift katmandan <b>difüzyonla</b> hem de integral bir protein olan <b>aquaporin</b>\'den <b>bulk flow</b> (toplu akış) ile geçer. '
        '<b>AQP1</b> bir su kanalıdır. Aquaporinin keşfiyle <b>Peter Agre</b> <b>2003 Nobel Ödülü</b>\'nü aldı (Kimya, <i>genel bilgi</i>).</p>')
    add(KAV((T('Selectively permeable', 'seçici geçirgen'), 'iç kısım hidrofobik; kanal, pompa, pinositoz reseptörleri'),
            (T('Membrane thickness', 'zar kalınlığı'), '60–100 Å'),
            (T('Ion distribution', 'iyon dağılımı'), 'hücre içi K⁺ fazla, doku sıvısı Na⁺ fazla'),
            (T("Fick's first law", 'Fick\'in birinci yasası'), 'J = P·A·(C_A − C_B)'),
            (T('Gas diffusion rate', 'gaz difüzyon hızı'), 'k × A × (P₂ − P₁) / D'),
            (T('Aquaporin', 'akuaporin'), 'su kanalı (AQP1); bulk flow; Peter Agre, Nobel 2003')))
    add(EXAM(
        ('Which of the following crosses a pure lipid bilayer most easily?', ['Na⁺', 'glucose', 'O₂', 'Cl⁻'], 'C', 'Hidrofobik küçük gazlar kolay geçer; iyonlar ve glikoz geçemez.'),
        ('Compared with tissue fluid, the inside of the cell contains:', ['more sodium', 'more potassium', 'equal Na⁺ and K⁺', 'no ions'], 'B', 'Hücre içinde K⁺, dışında Na⁺ fazla.'),
        ('In Fick\'s first law of diffusion (J = PA(C_A − C_B)), "A" stands for:', ['activity', 'surface area for diffusion', 'ATP', 'affinity'], 'B', 'Yüzey alanı (cm²).'),
        ('According to the formula for gas diffusion, the rate of diffusion DECREASES when:', ['the area increases', 'the partial pressure difference increases', 'the thickness of the barrier (D) increases', 'the diffusion constant increases'], 'C', 'D paydadadır.'),
        ('Water moves rapidly across membranes through integral proteins called:', ['GLUTs', 'aquaporins', 'connexins', 'integrins'], 'B', 'Akuaporin; Peter Agre.'),
        ('The plasma membrane is approximately how thick?', ['60–100 Å', '1–2 µm', '0.1 mm', '10 nm–1 µm'], 'A', 'Slayt: very thin (60–100 Å).'),
        ('Large uncharged polar molecules such as glucose:', ['diffuse freely through the bilayer', 'cannot cross the bilayer and need carriers', 'are pumped only by ABC transporters', 'enter only by phagocytosis'], 'B', 'Glikoz taşıyıcıyla (GLUT) girer.'),
    ))

    # ================= 20 =================
    k.h2('20 · Kolaylaştırılmış difüzyon: kanallar ve taşıyıcılar')
    add('<p><b>Facilitated diffusion</b> (passive transport, catalyzed transport): zar proteinleri (iyon kanalları, taşıyıcılar) belirli <b>ligandlara</b> (klorür, glikoz, sodyum, potasyum…) bağlanarak onların zardan geçişini kolaylaştırır; '
        'hareket <b>derişim gradyanı yönündedir</b> ve <b>enerji harcanmaz</b>. Kanallar ve taşıma proteinleri çözüneni belirli bir <b>afiniteyle</b> bağlar ve hareketi <b>doyurulabilir (saturable)</b> biçimde katalizler. <b>Taşıyıcıların çoğu özgüldür (specific)</b>.</p>')
    add(TABLE(['', E('Channel-mediated', 'kanal aracılı'), E('Carrier-mediated', 'taşıyıcı aracılı')], [
        ['Nasıl çalışır?', 'zarı boydan boya geçen proteinde bir <b>kanal</b>; hidrofilik amino asitler iyonun geçeceği yolu oluşturur, iyonu çift katmanın hidrofobik çekirdeğinden korur', 'molekül proteine <b>bağlanır</b> → protein <b>şekil değiştirir</b> (state A ↔ state B) → molekül öbür tarafa bırakılır'],
        ['Örnek', 'iyon kanalları, su (aquaporin)', '<b>glikoz</b> taşıyıcıları (GLUT)'],
        ['Kinetik', 'hızlı', '<b>doyar</b> (Vmax) → Michaelis–Menten']]))
    k.h3('İyon kanalı tipleri')
    add(TABLE(['Kanal', 'Ne açar?', 'Örnek'], [
        [E('Leak / always open', 'sızıntı, hep açık'), 'her zaman açık', 'K⁺, Na⁺ sızıntı kanalları'],
        [E('Voltage-gated', 'voltaj kapılı'), 'zar potansiyelindeki değişme', '<b>Na⁺, Ca²⁺, K⁺, Cl⁻</b> kanalları'],
        [E('Ligand-gated', 'ligand kapılı'), 'bir molekülün (ligand) bağlanması', 'nörotransmitter reseptörleri: <b>acetylcholine, GABA, glutamate</b>; Ca²⁺ ile aktive olan K⁺ kanalı; <b>cyclic nucleotide-gated</b> kanal (cAMP/cGMP)'],
        [E('Mechanically-gated', 'mekanik kapılı'), '<b>basınç</b> (gerilme)', 'dokunma, işitme reseptörleri <i>(genel bilgi)</i>']]))
    k.h3('Taşıyıcı kinetiği: Michaelis–Menten')
    add('<p>Basit difüzyonda hız, derişim arttıkça <b>doğrusal</b> olarak artar. Taşıyıcı aracılı taşımada ise hız önce hızla artar, sonra taşıyıcılar dolunca <b>Vmax</b>\'ta <b>doyar</b> (asimptot). '
        '<b>V = Vmax · [S] / (Km + [S])</b>. <b>Km</b>: hızın <b>Vmax\'ın yarısı</b> olduğu çözünen derişimidir; Km küçükse taşıyıcının <b>afinitesi yüksektir</b>. Toplam taşıma = taşıyıcı aracılı + pasif.</p>')
    add(TABLE(['Glikoz taşıyıcısı (GLUT)', 'Doku', 'Afinite (slayttaki grafik)'], [
        ['<b>GLUT1</b>', 'birçok hücre (slayttaki mekanizma örneği)', '1) glikoz dışa açık bağlanma yerine bağlanır → 2) protein konformasyon değiştirir → 3) glikoz içeri bırakılır, protein eski haline döner'],
        ['<b>GLUT3</b>', '<b>beyin</b>', 'en yüksek (düşük glikozda bile hızlı)'],
        ['<b>GLUT4</b>', '<b>kas, yağ</b>', 'orta'],
        ['<b>GLUT2</b>', '<b>karaciğer</b> (ve bağırsak hücresinin bazolateral yüzü)', 'en düşük (yüksek Km)']]))
    add(KAV((T('Facilitated diffusion', 'kolaylaştırılmış difüzyon'), 'kanal ya da taşıyıcı ile, gradyan yönünde, enerjisiz; doyurulabilir'),
            (T('Channel types', 'kanal tipleri'), 'leak, voltage-gated, ligand-gated, mechanically-gated'),
            (T('Ligand-gated examples', 'ligand kapılı örnekler'), 'acetylcholine, GABA, glutamate reseptörleri'),
            (T('Michaelis–Menten', 'Mikaelis–Menten'), 'V = Vmax[S]/(Km+[S]); Km = ½ Vmax\'taki derişim; taşıyıcı doyar'),
            (T('GLUT2 / 3 / 4', 'GLUT tipleri'), 'karaciğer / beyin / kas-yağ')))
    add(EXAM(
        ('Which type of transport shows saturation kinetics (Vmax)?', ['simple diffusion', 'carrier-mediated transport', 'osmosis through the bilayer', 'diffusion of O₂'], 'B', 'Taşıyıcılar dolunca hız Vmax\'ta sabitlenir.'),
        ('In the Michaelis–Menten equation, Km is the substrate concentration at which the rate is:', ['zero', 'equal to Vmax', 'half of Vmax', 'twice Vmax'], 'C', 'Km düşük = afinite yüksek.'),
        ('Acetylcholine, GABA and glutamate receptors are examples of:', ['voltage-gated channels', 'ligand-gated channels', 'mechanically-gated channels', 'P-type pumps'], 'B', 'Ligand kapılı reseptör kanalları.'),
        ('Channels opened by pressure are called:', ['ligand-gated', 'voltage-gated', 'mechanically-gated', 'leak channels'], 'C', 'Mekanik kapılı.'),
        ('Which glucose transporter is typical of the brain and has the highest affinity in the lecture graph?', ['GLUT1', 'GLUT2', 'GLUT3', 'GLUT4'], 'C', 'GLUT3 beyin; GLUT4 kas-yağ; GLUT2 karaciğer.'),
        ('Facilitated diffusion:', ['requires ATP', 'moves solutes against their gradient', 'moves solutes along their concentration gradient with the help of membrane proteins', 'occurs only for gases'], 'C', 'Pasif taşımadır.'),
    ))

    # ================= 21 =================
    k.h2('21 · Aktif taşıma, kotransport, endositoz ve ekzositoz')
    add('<p><b>Active transport</b>: iyon ya da moleküllerin <b>derişim gradyanına karşı</b>, <b>enerji harcanarak</b> taşınmasıdır.</p>')
    add(TABLE(['', E('Primary active transport', 'birincil aktif taşıma'), E('Secondary active transport', 'ikincil aktif taşıma')], [
        ['Enerji', 'taşıyıcı protein <b>ATP\'yi doğrudan hidroliz eder</b>', 'taşıyıcının <b>ATPaz etkinliği yoktur</b>; <b>dolaylı</b> olarak ATP\'ye bağlıdır: birincil taşımanın kurduğu <b>iyon gradyanının</b> enerjisini kullanır'],
        ['Nasıl?', 'pompa', 'bir maddenin taşınması başka bir maddeninkine bağlıdır: <b>cotransport</b>; bir iyon yüksekten düşüğe akarken diğer madde <b>gradyanına karşı</b> taşınır'],
        ['Örnek', '<b>Na⁺/K⁺-ATPaz</b>, Ca²⁺ pompası, H⁺ pompaları, ABC', '<b>SGLT1</b> (Na⁺–glikoz simportu), Na⁺/H⁺ antiportu']]))
    k.h3('Pompa sınıfları (4 sınıf ATPaz)')
    add(TABLE(['Sınıf', 'Ne taşır?', 'Örnek (slayt)'], [
        ['<b>P-class</b>', 'iyonları gradyanlarına karşı', '<b>sodium/potassium pump</b>, <b>calcium pump</b>'],
        ['<b>F-class</b>', '<b>protonları (H⁺)</b>', '<b>mitokondriyal H⁺ pompaları</b> (ATP sentazı)'],
        ['<b>V-class</b>', '<b>protonları (H⁺)</b>', '<b>lizozom zarı H⁺ pompaları</b> (lümeni asitleştirir)'],
        ['<b>ABC-class</b> (ATP-binding cassette)', '<b>ilaçlar, iyonlar, ksenobiyotikler</b>', '<b>MDR</b> (multidrug resistance) pompası, <b>P-glycoprotein (Pg)</b>']]))
    k.h3('Sodyum-potasyum pompası (Na⁺/K⁺-ATPase)')
    add('<p>1) <b>Tetramerik integral zar glikoproteinidir</b> (2 α + 2 β alt birim), 2) <b>elektrojeniktir</b> (her döngüde dışarı 3 pozitif, içeri 2 pozitif yük → zar potansiyeline katkı), 3) <b>α alt biriminin ATPaz etkinliği</b> vardır.</p>')
    add(CHAIN([('1 · 3 Na⁺ bağlanır', 'sitozol tarafından'), ('2 · Fosforilasyon', 'ATP → ADP; şekil değişir'), ('3 · 3 Na⁺ dışarı', '2 K⁺ bağlanır'), ('4 · Defosforilasyon', 'Pi ayrılır; eski şekil'), ('5 · 2 K⁺ içeri', 'döngü tekrar')],
              title='Na⁺/K⁺ pompasının döngüsü: her ATP ile 3 Na⁺ dışarı, 2 K⁺ içeri', note='Şema bu kağıt için çizildi.'))
    add(TIP('💊 MDR: kanser hücresinin ilaç direnci', '<p>ABC ailesinden <b>MDR (multidrug resistance)</b> taşıyıcısı (<b>P-glycoprotein, Pg pompası</b>) ilacı hücreden dışarı pompalar → <b>dirençli hücre</b>. '
        'Transporter <b>geninin ifadesi artınca</b> taşıyıcı düzeyi ve dışarı atılım artar: <b>detoksifikasyon</b> ve <b>ilaç direnci</b>. Pg pompası bir <b>inhibitörle</b> engellenirse ilaç hücrede birikir ve <b>duyarlılık geri gelir</b>.</p>'))
    k.h3('Kotransport: uniport, symport, antiport')
    add(TABLE(['Tip', 'Anlamı'], [
        ['<b>Uniport</b>', 'tek bir molekül taşınır (ör. GLUT2)'],
        ['<b>Symport</b> (cotransport)', 'iki madde <b>aynı yönde</b> (ör. Na⁺ + glikoz; bitkide H⁺ ile NO₃⁻, PO₄³⁻, K⁺, amino asit, sükroz)'],
        ['<b>Antiport</b> (exchange)', 'iki madde <b>zıt yönlerde</b> (ör. Na⁺/H⁺ antiportu)']]))
    add('<p><b>Bağırsakta glikoz emilimi</b> (sınav için klasik örnek):</p><ul>'
        '<li><b>Apikal giriş (SGLT1)</b>: sodyum-glikoz kotransporteri <b>1 glikozu (ya da galaktozu)</b> <b>2 Na⁺</b> ile birlikte içeri alır; glikoz <b>kendi gradyanına karşı</b> hücreye girer (ikincil aktif, symport).</li>'
        '<li><b>Sodyum gradyanı</b>: hücre içindeki düşük Na⁺\'yı <b>bazolateral zardaki Na⁺/K⁺-ATPaz</b> korur (ATP kullanır).</li>'
        '<li><b>Basolateral çıkış (GLUT2)</b>: glikoz hücreden kana (portal dolaşım) <b>kolaylaştırılmış difüzyonla</b> çıkar (uniport, yokuş aşağı).</li>'
        '<li><b>Yüksek yük istisnası</b>: lümende glikoz çok yüksekse GLUT2 geçici olarak <b>apikal zara</b> da yerleşir.</li></ul>')
    add(CHAIN([('Bağırsak lümeni', 'glikoz + 2 Na⁺'), ('SGLT1 (apikal)', 'symport, gradyana karşı'), ('Enterosit', 'glikoz birikir'), ('GLUT2 (bazolateral)', 'kolaylaştırılmış difüzyon'), ('Kan (portal)', '')],
              title='Bağırsakta glikoz yolculuğu', note='Na⁺ gradyanını bazolateral Na⁺/K⁺-ATPaz kurar (3 Na⁺ dışarı, 2 K⁺ içeri).'))
    k.h3('Büyük moleküller: endositoz ve ekzositoz')
    add('<p>Proteinler, <b>LDL</b>, <b>transferrin</b> gibi büyük moleküller ve katı kümeler zar yoluyla <b>keseciklerle</b> taşınır. <b>Endocytosis</b>: maddenin zarın içe kıvrımları (cepleri) ile alınması; cep zardan kopup sitoplazmada bir koful/kesecik (<b>endosome</b>) olur. '
        '<b>Exocytosis</b>: salgı keseciğinin plazma zarıyla kaynaşıp içeriğini dışarı vermesi.</p>')
    add(TABLE(['Endositoz tipi', 'Ne alınır?', 'Nasıl?'], [
        [E('Phagocytosis', 'fagositoz, "hücre yemesi"'), '<b>katı</b> parçacıklar (bakteri)', '<b>pseudopodium</b> (yalancı ayak) sarar → <b>phagosome</b> (besin kofulu)'],
        [E('Pinocytosis', 'pinositoz, "hücre içmesi"'), '<b>sıvı</b> (hücre dışı sıvı)', 'zar içe çöker → küçük kesecik'],
        [E('Receptor-mediated endocytosis', 'reseptör aracılı endositoz'), 'belirli <b>hedef molekül</b> (ligand)', '<b>reseptör</b> + <b>clathrin</b> ile kaplı <b>coated pit</b> → <b>coated vesicle</b>']]))
    add(CHAIN([('1 · Ligand reseptöre bağlanır', ''), ('2 · Klatrin kaplı çukura göç', ''), ('3 · Endositoz', 'kaplı kesecik'), ('4 · Klatrin kılıf atılır', ''), ('5 · Endozom', 'reseptör ve ligand ayrılır'),
               ('6 · Ligand', 'lizozom ya da Golgi'), ('7–8 · Reseptörlü kesecik zara döner', 'zar geri dönüşümü'), ('9 · Ekzositoz', '')],
              title='Kesecik trafiği (reseptör aracılı endositoz)'))
    add(TRAP('Yılmaz ve Özden\'in ifadeleri', '<p>Yılmaz\'ın slaytında ozmoz "often included in passive transport" ve fagositoz "bulk transport" altında geçer; taşıma <b>A) su</b> (ozmoz), <b>B) iyon ve küçük moleküller</b> (pasif: basit ve kolaylaştırılmış difüzyon; aktif), <b>C) büyük moleküller</b> (fagositoz; endositoz: pinositoz, reseptör aracılı) diye gruplanır. '
        'Özden\'in özet şemasında: <b>Passive</b> = simple diffusion (apolar ve küçük polar, doğrudan zardan), facilitated diffusion (taşıma proteini), osmosis (su, hipo → hiper) · <b>Active</b> = gradyana karşı, Na/K pompası, ATP · <b>Endocytosis</b> = fagositoz (katı), pinositoz (sıvı) · <b>Exocytosis</b> = keseciğin zarla kaynaşması.</p>'))
    add(KAV((T('Primary active transport', 'birincil aktif taşıma'), 'ATP\'yi doğrudan hidroliz eden pompa'),
            (T('Secondary active transport', 'ikincil aktif taşıma'), 'iyon gradyanının enerjisiyle kotransport; ATPazı yok'),
            (T('P / F / V / ABC', 'pompa sınıfları'), 'P: Na/K, Ca · F: mitokondri H⁺ · V: lizozom H⁺ · ABC: ilaç, ksenobiyotik (MDR)'),
            (T('Na⁺/K⁺-ATPase', 'sodyum-potasyum pompası'), 'tetramerik (2α2β) glikoprotein, elektrojenik, α\'da ATPaz; 3 Na⁺ dışarı, 2 K⁺ içeri'),
            (T('MDR / P-glycoprotein', 'çoklu ilaç direnci'), 'ABC pompası ilacı dışarı atar; inhibitörle engellenince duyarlılık döner'),
            (T('Symport / antiport', 'simport / antiport'), 'aynı yön / zıt yön'),
            (T('SGLT1', 'sodyum-glikoz kotransporteri'), 'apikal; 1 glikoz + 2 Na⁺'),
            (T('Endocytosis types', 'endositoz tipleri'), 'fagositoz (katı), pinositoz (sıvı), reseptör aracılı (klatrin)')))
    add(EXAM(
        ('Which of the following describes primary active transport?', ['transport along the gradient through a channel', 'direct hydrolysis of ATP by the transport protein to move ions against their gradient', 'cotransport powered by an ion gradient', 'movement of water through aquaporins'], 'B', 'Birincil aktif taşıma.'),
        ('Transporters that function in secondary active transport:', ['have ATPase activity', 'do not possess ATPase activity and depend indirectly on ATP hydrolysis', 'move only water', 'are always channels'], 'B', 'İyon gradyanını birincil taşıma kurar.'),
        ('Mitochondrial H⁺ pumps belong to the ___ class, and lysosomal membrane H⁺ pumps to the ___ class.', ['P / V', 'F / V', 'V / F', 'ABC / P'], 'B', 'F: mitokondri; V: lizozom; P: Na/K ve Ca.'),
        ('In each cycle, the Na⁺/K⁺-ATPase moves:', ['2 Na⁺ out and 3 K⁺ in', '3 Na⁺ out and 2 K⁺ in', '3 Na⁺ in and 2 K⁺ out', '1 Na⁺ out and 1 K⁺ in'], 'B', 'Elektrojenik: net bir pozitif yük dışarı.'),
        ('Which subunit of the Na⁺/K⁺ pump has ATPase activity?', ['alpha', 'beta', 'gamma', 'delta'], 'A', 'α alt birim.'),
        ('The multidrug resistance (MDR) pump that pumps drugs out of cancer cells belongs to the:', ['P-class', 'V-class', 'F-class', 'ABC family'], 'D', 'P-glikoprotein.'),
        ('Symporters move substrates:', ['in opposite directions', 'in the same direction', 'only out of the cell', 'without any ion'], 'B', 'Antiport: zıt yön.'),
        ('In the intestine, SGLT1 on the apical membrane transports glucose together with:', ['one K⁺', 'two Na⁺', 'one H⁺', 'two Cl⁻'], 'B', '1 glikoz + 2 Na⁺; çıkış bazolateral GLUT2 ile.'),
        ('Glucose leaves the enterocyte into the blood through the basolateral membrane by:', ['SGLT1 by active transport', 'GLUT2 by facilitated diffusion', 'the Na⁺/K⁺ pump', 'pinocytosis'], 'B', 'Kolaylaştırılmış difüzyon.'),
        ('Uptake of solid particles such as bacteria by pseudopodia is called:', ['pinocytosis', 'phagocytosis', 'receptor-mediated endocytosis', 'exocytosis'], 'B', 'Fagositoz (katı); pinositoz (sıvı).'),
        ('In receptor-mediated endocytosis, the coated pit is lined by:', ['clathrin', 'collagen', 'actin', 'aquaporin'], 'A', 'Klatrin kaplı kesecik.'),
    ))
