"""Bölüm 22–24: Cell Organisation and Movement: The Cytoskeleton (cell 3.pdf, Dr. Selma Yılmaz)."""
from ortak import E, T, _t

BOLUMLER = [('22', 'Hücre iskeletine genel bakış; mikrotübüller, MTOC, sentrozom', 'Cell 3 (S. Yılmaz)'),
            ('23', 'Aktin mikrofilamentleri ve ara filamentler', 'Cell 3'),
            ('24', 'Hücre hareketi: kinezin, dinein, sil ve kamçı, miyozin, kas kasılması', 'Cell 3')]


def lif_svg():
    """Üç lifin kalınlık karşılaştırması (ölçekli daireler) + yapı ipucu."""
    items = [('Microfilament (actin)', 'mikrofilament', '7–9 nm', 8, '#e05a5a', 'iki zincirli bükülmüş aktin; en ince'),
             ('Intermediate filament', 'ara filament', '8–12 nm', 10, '#5aa05a', 'halat gibi; dokuya özgü 6 sınıf'),
             ('Microtubule', 'mikrotübül', '25 nm', 25, '#3a6ea5', 'içi boş tüp; 13 protofilament; en kalın')]
    s = ''
    for i, (a, b, c, r, col, d) in enumerate(items):
        x = 110 + i * 230
        if i == 2:
            s += f'<circle cx="{x}" cy="80" r="{r * 2}" fill="none" stroke="{col}" stroke-width="10"/>'
            for j in range(13):
                import math
                ang = 2 * math.pi * j / 13
                s += f'<circle cx="{x + 45 * math.cos(ang):.1f}" cy="{80 + 45 * math.sin(ang):.1f}" r="5" fill="{col}"/>'
        else:
            s += f'<circle cx="{x}" cy="80" r="{r * 2}" fill="{col}"/>'
        s += _t(x, 158, a, 11, '700', col) + _t(x, 172, f'({b})', 10, '400', '#555') + _t(x, 190, c, 12, '700', '#222') + _t(x, 206, d, 9, '400', '#555')
    svg = f'<svg width="720" height="215" viewBox="0 0 720 215" style="display:block;margin:6px auto;max-width:100%">{s}</svg>'
    return ('<div style="page-break-inside:avoid;break-inside:avoid">' + svg +
            '<p class="small" style="text-align:center">Şekil (bu kağıt için çizildi, kesitler ölçekli): incelikten kalınlığa <b>aktin &lt; ara filament &lt; mikrotübül</b>.</p></div>')


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM, CHAIN = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM, k.CHAIN

    # ================= 22 =================
    k.h2('22 · Hücre iskeleti (Cytoskeleton) ve mikrotübüller')
    add('<p>Ökaryot hücrenin <b>cytoskeleton</b>\'u ipliksi proteinlerden yapılır; hücreye ve sitoplazma bileşenlerine <b>mekanik destek</b> verir, hücreye <b>şeklini</b> verir, parçaları düzenler, <b>hareket</b> ve <b>hücre bölünmesi</b> için temel oluşturur. '
        'Tek bir bileşen yoktur; birkaç bileşen birlikte çalışır ve lifler <b>ağlar ve demetler</b> halinde düzenlenir. Bütün hücre iskeletleri boyut ve protein bileşimi farklı <b>üç ana sınıftan</b> oluşur: '
        '<b>microtubules</b>, <b>actin filaments (microfilaments)</b>, <b>intermediate filaments</b>.</p>')
    add(lif_svg())
    add(TABLE(['', E('Microtubules', 'mikrotübüller'), E('Actin microfilaments', 'aktin mikrofilamentleri'), E('Intermediate filaments', 'ara filamentler')], [
        ['Çap', '<b>25 nm</b> (en büyük)', '<b>7–9 nm</b> (en küçük)', '<b>8–12 nm</b> (orta)'],
        ['Alt birim', '<b>α-β tubulin</b> heterodimeri', '<b>actin</b> (G-aktin → F-aktin)', 'dokuya göre değişen proteinler (ör. keratin, vimentin, lamin)'],
        ['Yapı', 'içi boş tüp, 13 protofilament', 'iki zincirli bükülmüş', 'halat gibi (ropelike)'],
        ['Kutupluluk', 'var (+ / −)', 'var (+ / −)', '—'],
        ['Dinamiklik', 'dinamik', 'çok dinamik', '<b>en az dinamik</b>'],
        ['Ana görev', 'mitoz, hareket, hücre içi taşıma, akson ve şekil', 'kas kasılması, hücre göçü, şekil', '<b>mekanik dayanıklılık</b>']]))
    k.h3('Mikrotübül görevleri')
    add('<ul><li><b>Cytoplasmic microtubules</b>: 1) <b>aksonları</b> korur, 2) <b>hücre şeklini</b> korur, 3) bitkide <b>selüloz mikrofibrillerini</b> yönlendirir, 4) <b>mitoz</b>: mitotik ve mayotik <b>iğ (spindle)</b> ile kromozom hareketi, 5) <b>hücre içi taşıma</b>: kesecik hareketi.</li>'
        '<li><b>Axonemal microtubules</b>: <b>sil, kamçı ve bazal cisimlerdeki</b> çok düzenli, kararlı mikrotübüller; merkezdeki eksen (<b>axoneme</b>) düzenli bir mikrotübül demetidir (ör. sperm kuyruğu).</li></ul>'
        '<p>Benzetme: mikrotübüller tren rayları gibidir; hücreye yapı verir, kesecik ve proteinleri <b>yönlü</b> taşır; üzerinde vagon gibi giden motor proteinler <b>kinesin ve dynein</b>\'dir. '
        'Hücre bölünmesindeki önemleri nedeniyle, mikrotübül işlevini bozarak hızla bölünen <b>kanser hücrelerini</b> öldüren ilaçlar geliştirilmiştir: mitozu engelleyen bu ilaçlara <b>antimitotics</b> denir.</p>')
    k.h3('Mikrotübül yapısı')
    add('<p><b>α-tubulin ve β-tubulin</b> birlikte bir <b>heterodimer</b> oluşturur; dimerler uç uca dizilerek doğrusal <b>protofilament</b> yapar. Bir mikrotübül, bir <b>lümen</b> çevresinde dizilmiş <b>10–15 protofilamentten</b> oluşan içi boş bir silindirdir (<b>memelilerde 13</b>).</p>')
    add(TABLE(['Mikrotübül tipi', 'Protofilament', 'Nerede?'], [
        ['<b>Singlet</b>', '<b>13</b> (A)', 'sitoplazma'],
        ['<b>Doublet</b>', '13 + 10 (ya da 11) (A + B)', '<b>sil ve kamçı</b>'],
        ['<b>Triplet</b>', '13 + 10 (11) + 10 (11)', '<b>bazal cisim ve sentriyoller</b>']]))
    add('<p><b>Polarite</b>: tubulinin <b>α ucu eksi (−)</b>, <b>β ucu artı (+)</b> uçtur; 13 protofilamentin hepsinin artı uçları aynı tarafta olduğu için mikrotübülün bir <b>yönü</b> vardır. '
        'Mikrotübüller uçlara tubulin dimerleri eklenerek oluşur: önce <b>çekirdeklenme merkezleri (nucleation, oligomer)</b>, sonra iki uçtan alt birim eklenerek uzama (<b>elongation</b>). İki uçtaki hız eşit değildir: <b>artı uç hızlı büyür</b>, eksi uç yavaş. '
        'Yapım ve yıkımın tam dengede olduğu derişime <b>critical concentration</b> denir: <b>treadmilling</b>.</p>')
    add('<p>Hücrede mikrotübüllerin <b>eksi uçları</b> <b>microtubule organizing centers (MTOCs)</b> içinde sabitlenir; MTOC hem başlangıç yeri hem çapadır. Hücredeki ana MTOC <b>centrosome</b>\'dur ve genelde <b>çekirdeğin yanındadır</b>; '
        'mikrotübüller sentrozomdan <b>plazma zarına doğru</b> büyür. Sentrozom (<b>yalnız hayvan hücrelerinde</b>) <b>pericentriolar material (PCM)</b> ile çevrili <b>iki fıçı şeklinde sentriyol</b>den oluşur; sentriyoller <b>triplet</b> mikrotübüllerdir ve '
        'kromozomların ayrılmasına yardım eden <b>aster ve iğ ipliklerinden</b> oluşan mitoz aygıtını düzenler. Mikrotübül polaritesi hücrenin işlevine göre değişebilir (sinir hücresi, silli epitel, kırmızı kan hücresi, bölünen hücre). '
        '<b>Microtubule-associated proteins (MAPs)</b> mikrotübülleri <b>kararlı hale getirir ve demetler</b>.</p>')
    add(KAV((T('Three cytoskeletal filaments', 'üç hücre iskeleti lifi'), 'microtubules (25 nm) > intermediate filaments (8–12 nm) > actin (7–9 nm)'),
            (T('Tubulin heterodimer', 'tubulin heterodimeri'), 'α (− uç) + β (+ uç)'),
            (T('Protofilaments', 'protofilamentler'), 'memeli singlet mikrotübülünde 13'),
            (T('Singlet / doublet / triplet', 'tekli / ikili / üçlü'), 'sitoplazma / sil-kamçı / bazal cisim-sentriyol'),
            (T('Treadmilling', 'koşu bandı'), 'kritik derişimde yapım = yıkım'),
            (T('MTOC / centrosome', 'MTOC / sentrozom'), 'eksi uçların çapası; çekirdek yanında; 2 sentriyol + PCM (hayvan)'),
            (T('MAPs', 'mikrotübülle ilişkili proteinler'), 'kararlı hale getirir ve demetler'),
            (T('Antimitotics', 'antimitotikler'), 'mikrotübülü bozarak kanser hücresinde mitozu engelleyen ilaçlar')))
    add(EXAM(
        ('Which cytoskeletal filament has the largest diameter (about 25 nm)?', ['actin microfilament', 'intermediate filament', 'microtubule', 'myosin filament'], 'C', 'Mikrotübül 25 nm; ara filament 8–12; aktin 7–9.'),
        ('How many protofilaments make up a singlet microtubule in mammalian cells?', ['9', '11', '13', '20'], 'C', 'Doublet 13+10/11; triplet 13+10+10.'),
        ('Triplet microtubules are found in:', ['cilia and flagella', 'basal bodies and centrioles', 'the cell cortex', 'microvilli'], 'B', 'Doublet: sil ve kamçı.'),
        ('The minus (−) end of a microtubule corresponds to:', ['β-tubulin', 'α-tubulin', 'γ-actin', 'keratin'], 'B', 'α = eksi, β = artı.'),
        ('When assembly and disassembly of a microtubule are exactly balanced, this is called:', ['nucleation', 'elongation', 'treadmilling', 'phosphorylation'], 'C', 'Kritik derişim: treadmilling.'),
        ('In animal cells, the primary microtubule organizing center (MTOC) is the:', ['nucleolus', 'centrosome', 'Golgi', 'basal lamina'], 'B', 'Sentrozom: 2 sentriyol + PCM, çekirdeğin yanında.'),
        ('Drugs that kill rapidly dividing cancer cells by disrupting microtubules and preventing mitosis are called:', ['antibiotics', 'antimitotics', 'anticoagulants', 'antioxidants'], 'B', 'Antimitotikler.'),
    ))

    # ================= 23 =================
    k.h2('23 · Aktin mikrofilamentleri ve ara filamentler')
    k.h3('Aktin mikrofilamentleri (Microfilaments)')
    add('<p><b>Actin microfilaments</b> hücre iskeletinin <b>en ince</b> elemanıdır (<b>7–9 nm</b>); <b>aktin</b> proteininden yapılmış, <b>iki zincirli bükülmüş</b> liflerdir. Aktin bütün ökaryot hücrelerde boldur. '
        '<b>G-actin</b> (globüler aktin) monomerleri polimerleşerek <b>F-actin</b> mikrofilamentlerini oluşturur. Aktin liflerinin <b>artı ve eksi uçları</b> vardır; <b>ATP ile beslenen büyüme daha çok artı uçta</b> olur. '
        'Hücrede aktin iskeleti dinamiktir: lifler hızla büyüyüp kısalabilir. <b>Actin-binding proteins</b> aktinin düzenini kontrol eder.</p>')
    add(TABLE(['Aktinin görevleri ve yapıları', 'Açıklama'], [
        ['<b>Kas kasılması</b>', '<b>myosin</b> lifleriyle birlikte'],
        ['<b>Hücre göçü</b>', '<b>lamellipodia</b> (yaprak gibi uzantılar), <b>filopodia</b> (ince parmak gibi uzantılar), <b>amip hareketi</b>, <b>sitoplazma akışı</b>'],
        ['Sürünen hücrede (makrofaj) 3 rol', '1) <b>contractile bundle</b> (stres liflerinde) · 2) <b>gel</b> (hücre korteksi) · 3) <b>parallel bundle</b> (filopodyumda)'],
        ['<b>Microvilli</b>', 'bağırsak emici epitelinde apikal uzantılar; çekirdeğindeki aktin demeti yapıyı sabitler; <b>emilim yüzeyini artırır</b>'],
        ['<b>Contractile ring</b>', 'sitokinezde hücreyi ortadan boğarak ikiye ayırır'],
        ['<b>Cell cortex</b> (aktin korteksi)', 'hücre duvarı olmayan hücrelerde zarın altındaki aktin + miyozin + aktin bağlayan protein ağı; hücreye <b>şeklini</b> verir; büyüyerek uzantılar yapar: sürünme ve <b>fagositoz</b>'],
        ['<b>Spectrin–actin network</b>', '<b>eritrosit</b> zarının gücü ve esnekliği; <b>spectrin</b> (lifli protein) kortikal iskeletin ana bileşeni; "uzun kollar ve göbekler" ağı; <b>ankyrin</b> spektrini integral zar proteinlerine bağlar'],
        ['<b>Stress fibers</b>', 'aktin + çapraz bağlayıcı proteinler + <b>miyozin II</b> (kas dışı hücre); gerilimle oluşur; kasılabilir; zara <b>focal adhesions</b> denen noktalarda tutunur']]))
    add('<p><b>Aktin polimerleşmesiyle hareket örnekleri</b>: <b>Listeria</b> bakterisi, enfekte ettiği fibroblastta konak hücrenin aktinini kullanarak hareket eder (her bakterinin arkasında aktin "kuyruğu"); '
        '<b>trombositler (platelets)</b> pıhtılaşmada şekil değiştirir (dinlenme → pıhtılaştırıcıya maruz kalma → pıhtı büzülmesi). Hücre göçünü dış sinyaller koordine eder: <b>G proteinleri ve kalsiyum</b> hücreyi kutuplaştırır; '
        '<b>Rho ailesi</b> proteinleri aktine bağlı uzantıları düzenler. Düz kas ve kas dışı hücrelerde kasılma, sitozolik <b>Ca²⁺ artışı</b> ya da dış sinyallere yanıt olarak <b>Rho kinaz</b> ile <b>miyozinin fosforillenmesiyle</b> tetiklenir.</p>')
    k.h3('Ara filamentler (Intermediate filaments)')
    add('<p><b>Intermediate filaments (IFs)</b> orta kalınlıktadır (<b>8–12 nm</b>), <b>halat gibidir</b> ve güçlüdür. Bütün hücrelerde bulunur ama alt birim proteinleri değişir: <b>dokuya ve hücreye özgüdür</b>, <b>6 sınıftır</b>. '
        'Genelde <b>homodimerlerin</b> sarmal halde protofilamentlere dizilmesiyle oluşur; <b>keratin</b> istisnadır: <b>tip I ve tip II</b> polipeptitlerin zorunlu <b>heterodimerlerinden</b> yapılır. '
        'Keratin hayvanlarda kıl, pençe, tırnak, boynuz, gaga, kaplumbağa kabuğu, tüy, pul ve derinin en dış tabakası için gereklidir.</p>'
        '<p>Ana görevi <b>mekaniktir</b>: hücreye <b>mekanik dayanıklılık</b> verir, strese dayanmasına yardım eder. Aktin ve mikrotübüllerden <b>daha az dinamiktir</b>; genelde mikrotübüllerle birlikte çalışıp narin tubulin yapılarına destek olur. '
        'IF bağlayan proteinlerle (lamin vb.) ağlar ve demetler kurar. Yapım ve yıkımı lif proteinlerinin <b>fosforilasyonuyla</b> düzenlenir; örnek: <b>mitozda nükleer laminanın (lamin) yıkılması</b>. Hareket eden hücre önde bir ara filament (ör. <b>vimentin</b>) ağı kurar.</p>')
    add(TRAP('Hangisi hangisi?', '<p>Sitokinezdeki <b>kasılma halkası</b> = <b>aktin</b> (+ miyozin II) · mitozdaki <b>iğ iplikleri</b> = <b>mikrotübül</b> · <b>mikrovillus</b> çekirdeği = <b>aktin</b> · <b>sil ve kamçı</b> = <b>mikrotübül</b> · <b>keratin, vimentin, lamin</b> = <b>ara filament</b> · eritrosit zarının esnekliği = <b>spektrin–aktin</b> (+ ankirin).</p>'))
    add(KAV((T('G-actin / F-actin', 'globüler / ipliksi aktin'), 'monomer / polimer (mikrofilament)'),
            (T('Lamellipodia / filopodia', 'lamellipodyum / filopodyum'), 'yaprak gibi / parmak gibi aktin uzantıları; hücre göçü'),
            (T('Cell cortex', 'hücre korteksi'), 'zar altı aktin ağı; şekil, sürünme, fagositoz'),
            (T('Spectrin & ankyrin', 'spektrin ve ankirin'), 'eritrosit zarının kortikal iskeleti; ankirin spektrini zar proteinine bağlar'),
            (T('Stress fibers / focal adhesions', 'stres lifleri / fokal adezyonlar'), 'aktin + miyozin II; zara tutunma noktaları'),
            (T('Intermediate filaments', 'ara filamentler'), '8–12 nm, halat, dokuya özgü 6 sınıf, mekanik güç; keratin = tip I + II heterodimer'),
            (T('Rho family', 'Rho ailesi'), 'aktine bağlı uzantıları düzenler; Rho kinaz miyozini fosforiller')))
    add(EXAM(
        ('Actin microfilaments have a diameter of about:', ['25 nm', '7–9 nm', '8–12 nm', '100 nm'], 'B', 'En ince lif.'),
        ('Monomers of ___ polymerize into microfilaments of ___ .', ['F-actin / G-actin', 'G-actin / F-actin', 'tubulin / actin', 'keratin / lamin'], 'B', 'Globüler → ipliksi.'),
        ('The core of intestinal microvilli is stabilized by a bundle of:', ['microtubules', 'actin microfilaments', 'intermediate filaments', 'collagen fibers'], 'B', 'Emilim yüzeyini artırır.'),
        ('In human erythrocytes, ___ cross-links spectrin to integral membrane proteins.', ['ankyrin', 'kinesin', 'dynein', 'vimentin'], 'A', 'Spektrin–aktin ağı.'),
        ('Which statement about intermediate filaments is correct?', ['They are the most dynamic filaments', 'They are tissue-specific, ropelike and mainly provide mechanical strength', 'They are made of tubulin', 'They form the mitotic spindle'], 'B', '6 sınıf, 8–12 nm.'),
        ('Keratin intermediate filaments differ from most others because they are made of:', ['homodimers only', 'obligate heterodimers of type I and type II polypeptides', 'tubulin dimers', 'actin monomers'], 'B', 'Tip I + tip II heterodimer.'),
        ('Breakdown of the nuclear lamina during mitosis is regulated by:', ['phosphorylation of filament proteins', 'ATP hydrolysis by kinesin', 'clathrin coating', 'glycosylation'], 'A', 'Ara filamentlerin fosforilasyonu.'),
        ('The sites where stress fibers anchor to the cell membrane are called:', ['tight junctions', 'focal adhesions', 'desmosomes', 'coated pits'], 'B', 'Fokal adezyonlar.'),
        ('The bacterium Listeria moves inside infected cells by using the host cell\'s:', ['microtubules', 'actin', 'keratin', 'cilia'], 'B', 'Arkasında aktin kuyruğu oluşur.'),
    ))

    # ================= 24 =================
    k.h2('24 · Hücre hareketi: motor proteinler, sil ve kamçı, kas kasılması')
    add('<p>Hücre iskeleti yalnız iskele değildir, <b>hücre hareketinin</b> de temelidir. Çok hücreli canlıda göç önemlidir: <b>embriyoda</b> tek hücre ve grup göçü gelişim için kritiktir; <b>erişkinde</b> enfeksiyona karşı savunmanın parçasıdır; '
        '<b>kontrolsüz hücre göçü kanser belirtisidir</b>. Hareket belirli zaman ve yerde, hücrenin kontrolünde olur; <b>yakıt (ATP) ve proteinler</b> gerektirir. Hareket etmeyen hücreler de şekil değiştirebilir: kas kasılması, sinir aksonunun uzaması, kromozom ayrılması, kesecik taşınması.</p>')
    add(TIP('⚙️ ATP kullanan iki temel hareket sistemi', '<p><b>1)</b> <b>Mikrotübüller</b> + motor proteinler <b>kinesin ve dynein</b> · <b>2)</b> <b>Aktin mikrofilamentleri</b> + motor protein <b>myosin</b>. '
        'Motor proteinler (<b>mechanoenzymes</b>) ATP\'deki <b>kimyasal enerjiyi mekanik enerjiye</b> çevirerek kuvvet ve hareket üretir. Aktin ve mikrotübüllerin yapım-yıkımı <b>hücre şeklini</b>, motor proteinlerin etkinliği <b>kasılma ve kesecik taşımayı</b> sağlar.</p>'))
    k.h3('Kinesin ve dynein: mikrotübül üzerinde taşıma')
    add(TABLE(['', E('Kinesins', 'kinezinler'), E('Dyneins', 'dineinler')], [
        ['Ortak yapı', '<b>ATP bağlayan globüler baş</b> (motor bölge, mikrotübüle tutunur) + yükü bağlayan <b>kuyruk</b>', 'aynı'],
        ['Yön', 'çoğu <b>artı (+) uca</b> → hücre <b>merkezinden uzağa</b>', '<b>eksi (−) uca</b> → hücre <b>merkezine doğru</b>'],
        ['Görev', 'yükü hücre <b>çevresine</b> götürür; çoğu <b>processive</b> (kopmadan uzun yürür)', 'yükü <b>merkeze</b> getirir; <b>dynein/dynactin</b> kompleksi kesecik yüküne bağlanır']]))
    add('<p>Kinezin ve dynein, ATP hidrolizini mikrotübül üzerinde <b>yürümeye</b> bağlayan motor proteinlerdir; yükü bir çekici gibi tutup raylar boyunca çekerler. Endomembran sistemi bütünüyle mikrotübüller ve motor proteinler üzerinde hareket eder.</p>')
    k.h3('Sil ve kamçı (Cilia and flagella)')
    add('<p>Sil ve kamçıyı <b>mikrotübüller</b> hareket ettirir. Merkezlerinde <b>axoneme</b> vardır; protofilamentler ve <b>dynein</b> sayesinde hareket ederler, aralarındaki bağı <b>nexin</b> kurar. <b>Basal bodies</b> denen özel mikrotübül gruplarından oluşur ve plazma zarına bağlıdır. '
        'Hücre yüzeyinde <b>çok sayıdaysa sil</b>, <b>bir ya da birkaç taneyse kamçı</b> denir. Sil ve kamçı hücre yüzeyi boyunca sıvıyı hareket ettirir; sperm gibi tek hücrelerde yüzmeye yarar. Kamçı sinek kuşunun kanatları gibi hızlıdır, sil su örümceğinin bacakları gibidir.</p>')
    add(TABLE(['', 'Sil (cilium)', 'Kamçı (flagellum)'], [
        ['Yapı', 'kısa, mikroskobik, kıl gibi titreşen; <b>motile</b> (hareketli) ve <b>non-motile</b> (duyusal organel) iki tipi var', 'sile çok benzer; protozoa, alg, mantar ve hayvan hücrelerinde hareket organeli'],
        ['Örnek', '<b>solunum yolu epiteli</b>: mukustaki parçacıkları süpürüp atar · <b>yumurta kanalı (oviduct)</b>: yumurtayı fallop tüpünden taşır', '<b>memeli spermi</b> (dişi üreme yolunda ilerler; tek kamçı, ~<b>1 mm/s</b>) · <b>Helicobacter pylori</b>: çok sayıda kamçıyla mukusu geçip mide epiteline ulaşır (ülser)'],
        ['Not', '', 'prokaryot ve ökaryot kamçısı <b>protein bileşimi, yapı ve itme mekanizması</b> bakımından çok farklıdır; ikisi de yüzmeye yarar (ökaryot kamçısı dalgalanır, prokaryotunki döner)']]))
    k.h3('Aktine dayalı hareket ve kas kasılması')
    add('<p><b>Myosins</b> aktin üzerinde çalışan motor proteinlerdir; en bol tipler <b>myosin-I</b> ve <b>myosin-II</b>; <b>kas miyozini myosin-II</b> ailesindendir. İskelet kası hücresinde ince <b>aktin</b> ve kalın <b>miyozin</b> lifleri, <b>sarcomere</b> denen düzenli yapılar oluşturur '
        '(sarkomer yapısal ve destek proteinlerinden oluşur). Kas hücresinin parçaları: <b>sarcolemma</b> (kas hücre zarı), <b>sarcoplasmic reticulum</b> (iskelet kasının ER\'si), <b>transverse (T) tubules</b>. '
        'Kas dışı hücrelerde aktin ve miyozin II ilkel sarkomer benzeri <b>kasılabilir demetler</b> oluşturur (ör. sitokinez kasılma halkası).</p>')
    add(CHAIN([('1 · Miyozin aktine gevşek bağlanır', ''), ('2 · Güç vuruşu (power stroke)', 'konformasyon değişir; kalın lif ince lifi kaydırır'), ('3 · ATP bağlanır', 'miyozin–aktin bağı zayıflar (ATP yoksa: rigor / sertlik)'), ('4 · ATP hidrolizi', 'miyozin yüksek enerjili hale döner; yeni tur')],
              title='Kas kasılması: dört adımlı döngü', note='Şema bu kağıt için çizildi. "ATP yoksa rigor" ölüm sertliğinin nedenidir (genel bilgi).'))
    add('<p><b>Kas dışı hücrede aktine dayalı göç</b>: aktin mikrofilamentleri hücreyi <b>uzanma (protrusion) → tutunma (attachment) → ilerleme (translocation) → ayrılma (detachment)</b> döngüleriyle hareket ettirir; hareket, kuvvet üretimini <b>hücre adezyonuyla</b> koordine eder. '
        'Hızlı hareket eden hücrelerde (ör. balık epidermis hücresi, keratinosit, fibroblast) hareket, öndeki kenardan bir ya da daha çok <b>lamellipodyum</b> uzatılmasıyla başlar.</p>')
    add(KAV((T('Kinesin', 'kinezin'), 'mikrotübülde artı uca, merkezden uzağa (çevreye); çoğu processive'),
            (T('Dynein', 'dinein'), 'mikrotübülde eksi uca, merkeze doğru; dynein/dynactin; sil-kamçıda hareket'),
            (T('Axoneme / nexin', 'aksonem / neksin'), 'sil-kamçının merkezi; ikili mikrotübülleri neksin bağlar'),
            (T('Cilia vs flagella', 'sil ve kamçı'), 'çok sayıda ve kısa / bir-birkaç ve uzun'),
            (T('Myosin II', 'miyozin II'), 'kas miyozini; aktinle kasılma; kas dışı hücrede stres lifi ve kasılma halkası'),
            (T('Sarcomere', 'sarkomer'), 'iskelet kasında aktin (ince) + miyozin (kalın) birimi'),
            (T('Rigor', 'rigor / sertlik'), 'ATP yokken miyozin aktinden ayrılamaz')))
    add(EXAM(
        ('Most kinesins move cargo toward the ___ end of microtubules, that is, toward the ___ of the cell.', ['minus / center', 'plus / periphery', 'plus / center', 'minus / periphery'], 'B', 'Dynein ise eksi uca, merkeze.'),
        ('Which motor protein carries cargo toward the center of the cell along microtubules?', ['kinesin', 'dynein', 'myosin II', 'actin'], 'B', 'Dynein/dynactin kompleksi.'),
        ('The two main systems for ATP-dependent cell movement are:', ['tubulin–keratin and actin–lamin', 'microtubules with kinesin/dynein and actin with myosin', 'collagen and elastin', 'spectrin and ankyrin'], 'B', 'Hoca tekrar sorusu.'),
        ('Cilia and flagella are driven by:', ['actin filaments', 'microtubules (axoneme) and dynein', 'intermediate filaments', 'collagen'], 'B', 'Nexin ikili mikrotübülleri bağlar.'),
        ('In the respiratory tract, the function of cilia is to:', ['absorb nutrients', 'dislodge and expel particulate matter collected in mucus', 'produce surfactant', 'contract smooth muscle'], 'B', 'Yumurta kanalında yumurtayı taşır.'),
        ('Helicobacter pylori reaches the stomach epithelium by using:', ['cilia', 'multiple flagella', 'pseudopodia', 'microvilli'], 'B', 'Ülsere neden olan bakteri.'),
        ('Muscle myosin belongs to the:', ['myosin-I family', 'myosin-II family', 'kinesin family', 'dynein family'], 'B', 'Miyozin II.'),
        ('In the muscle contraction cycle, binding of ATP to myosin:', ['causes the power stroke', 'weakens the bond between myosin and actin', 'is not required', 'binds myosin tightly to actin permanently'], 'B', 'ATP yoksa rigor (sertlik).'),
        ('Uncontrolled cell migration is a sign of:', ['normal development', 'infection defense', 'cancer', 'apoptosis'], 'C', 'Embriyoda gelişim, erişkinde savunma; kontrolsüzse kanser.'),
    ))
