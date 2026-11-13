"""Bölüm 25–26: Cell Adhesion (Prof. Dr. A. Kevser Özden, 37 slayt, görüntüden okundu)."""
from ortak import E, T

BOLUMLER = [('25', 'Hücre bağlantıları: sıkı, yapışma, desmozom, hemidesmozom, gap', 'Cell Adhesion (A. K. Özden)'),
            ('26', 'Hücre adezyon molekülleri: kaderin, Ig-CAM, selektin, integrin; dezintegrinler', 'Cell Adhesion')]


def yaz(k):
    add, KAV, TIP, TRAP, TABLE, EXAM = k.add, k.KAV, k.TIP, k.TRAP, k.TABLE, k.EXAM

    # ================= 25 =================
    k.h2('25 · Hücre adezyonu ve hücre bağlantıları')
    add('<p>Çok hücreli olmak <b>dokuları</b> gerektirir; dört doku tipi: <b>connective</b> (bağ), <b>epithelial</b> (epitel), <b>muscle</b> (kas), <b>nervous</b> (sinir). Dokuyu bir arada tutan <b>cell adhesion</b> (hücre adezyonu) iki türlüdür: '
        '<b>hücre–hücre</b> ve <b>hücre–ECM</b> (hücre dışı matriks). Adezyonun önemi: <b>embriyonik gelişim</b>, <b>farklılaşma</b>, <b>doku oluşumu</b>, <b>hücre göçü</b> ve hücrelerin <b>uyum içinde çalışması</b> (functioning in concert).</p>')
    add(TABLE(['Bağlantı', 'Neyi neye bağlar?', 'Hangi lif / protein?'], [
        [E('Tight junction', 'sıkı bağlantı'), 'komşu epitel hücreleri arasındaki <b>boşluğu kapatır</b> (seals); epitelin en tepesinde', '—'],
        [E('Adherens junction', 'yapışma bağlantısı'), 'komşu hücrelerin <b>aktin</b> liflerini birbirine bağlar', 'kaderin (E-cadherin) + <b>katenin</b> (α, β, p120) + aktin'],
        [E('Desmosome', 'desmozom'), 'komşu hücrelerin <b>ara filamentlerini</b> birbirine bağlar', 'desmoglein, desmocollin (kaderin) + plakoglobin, plakophilin, desmoplakin + tonofilament (ara filament)'],
        [E('Hemidesmosome', 'hemidesmozom'), 'hücrenin <b>ara filamentlerini ECM\'ye</b> (bazal lamina) bağlar', 'integrin <b>α6β4</b> + laminin'],
        [E('Actin-linked cell–matrix junction', 'aktine bağlı hücre–matriks bağlantısı'), 'hücrenin <b>aktinini ECM\'ye</b> bağlar', 'integrin (fokal adezyon)'],
        [E('Gap junction', 'aralık bağlantısı'), 'komşu hücreler arasında <b>kanal</b>: küçük suda çözünen moleküller geçer', '<b>connexin</b> (connexon)']]))
    add('<p>Gruplar: <b>hücre–hücre tutunma</b> (adherens, desmozom), <b>kanal oluşturan</b> (gap), <b>hücre–matriks tutunma</b> (aktine bağlı bağlantı, hemidesmozom). Sıkı bağlantı + adherens + desmozom birlikte <b>junctional complex</b> (bağlantı kompleksi) oluşturur. '
        'Bağlantılarda <b>hücre içi adaptör proteinler</b>, hücre iskeleti liflerini <b>transmembran adezyon proteinlerine</b> bağlar.</p>')
    add('<p><b>Gap junction</b>: komşu hücreleri bağlayan <b>büyük, kontrollü bir kanaldır</b>; çok alt birimli <b>connexin</b> proteininden yapılır; iyonlar ve (slayta göre) proteinler geçer; aktarım hızlıdır. Kanal <b>Ca²⁺, pH ve voltajla</b> açılıp kapanır. '
        'Bu yüzden <b>hızlı iletim ve kasılma</b> sağlar (ör. <b>kalp</b>).</p>')
    add(TRAP('Desmozom ↔ hemidesmozom ↔ adherens', '<p><b>Desmozom</b> = hücre–hücre, <b>ara filament</b> · <b>Hemidesmozom</b> = hücre–<b>ECM</b>, <b>ara filament</b> · <b>Adherens</b> = hücre–hücre, <b>aktin</b> · <b>Gap</b> = kanal, connexin · <b>Tight</b> = boşluğu kapatır.</p>'))
    add(KAV((T('Tight junction', 'sıkı bağlantı'), 'epitel hücreleri arasındaki boşluğu kapatır'),
            (T('Adherens junction', 'yapışma bağlantısı'), 'hücre–hücre, aktin; kaderin + katenin'),
            (T('Desmosome', 'desmozom'), 'hücre–hücre, ara filament; desmoglein, desmocollin'),
            (T('Hemidesmosome', 'hemidesmozom'), 'hücre–ECM, ara filament; integrin α6β4'),
            (T('Gap junction', 'aralık bağlantısı'), 'kanal; connexin; Ca²⁺/pH/voltajla kontrol; kalpte hızlı iletim')))
    add(EXAM(
        ('Which junction connects the intermediate filaments of a cell to the extracellular matrix?', ['desmosome', 'hemidesmosome', 'adherens junction', 'tight junction'], 'B', 'Desmozom ise iki hücrenin ara filamentlerini bağlar.'),
        ('Adherens junctions connect the ___ of adjacent cells.', ['intermediate filaments', 'actin fibers', 'microtubules', 'collagen fibers'], 'B', 'Kaderin + katenin + aktin.'),
        ('Gap junctions are composed of a multiunit protein called:', ['cadherin', 'connexin', 'integrin', 'selectin'], 'B', 'Konnekson kanalı.'),
        ('Which junction seals the gap between epithelial cells?', ['gap junction', 'tight junction', 'desmosome', 'hemidesmosome'], 'B', 'Sıkı bağlantı.'),
        ('Gap junction channels are regulated by:', ['Ca²⁺, pH and voltage', 'only ATP', 'clathrin', 'collagen'], 'A', 'Kalpte hızlı iletim ve kasılma.'),
        ('Desmoglein and desmocollin are:', ['integrins', 'desmosomal cadherins', 'selectins', 'connexins'], 'B', 'Desmozomal kaderinler (epitel).'),
    ))

    # ================= 26 =================
    k.h2('26 · Hücre adezyon molekülleri (CAMs)')
    add('<p><b>Cell adhesion molecules</b> hücreleri birbirine ya da ECM\'ye bağlar; <b>50\'den fazla tipi</b> vardır. Dört ana aile: <b>cadherins</b>, <b>immunoglobulin-like CAMs</b>, <b>selectins</b>, <b>integrins</b>. '
        'Bağlanma <b>homophilic</b> (aynı molekülle: kaderin–kaderin, N-CAM–N-CAM) ya da <b>heterophilic</b> (farklı molekülle: selektin–karbonhidrat, integrin–fibronektin) olabilir.</p>')
    add(TABLE(['Aile', 'Özellik', 'Ca²⁺?', 'Örnek / görev'], [
        ['<b>I. Cadherins</b>', 'transmembran <b>glikoproteinler</b>; dokuyu bir arada tutar; <b>katenin</b> hücre içi adaptör proteindir (catenia = zincir); en az <b>40 tip</b>; <b>uzun süreli</b> tutunma; embriyonik gelişim ve erişkinde doku hücrelerini birlikte tutma', '<b>bağımlı</b> (kalsiyum aktive eder ve yıkımdan korur; bazıları bağımsız)', 'klasik: <b>E-cadherin</b> (epitel), <b>N-cadherin</b> (MSS, lens, iskelet ve kalp kası), <b>P-cadherin</b> (trofoblast) · desmozomal: <b>desmocollin, desmoglein</b> (epitel) · protokaderinler'],
        ['<b>II. Ig-like CAMs</b>', 'immünoglobulinler (antikorlar) gibi <b>halka (Ig-loop) bölgeleri</b> olan zar proteinleri (slayt: 5 halka); hücre–hücre bağlantısı; ligandları integrinler ve diğer Ig-CAM\'ler; sinir gruplaşması; <b>geçici</b> bağlantı', 'çoğu <b>bağımsız</b> (desmozom ve sıkı bağlantıdakiler hariç)', '<b>NCAM</b> (nöral), <b>ICAM-1, ICAM-2</b> (hücreler arası), <b>VCAM-1</b> (vasküler), PECAM-1, L1-CAM, CD2, CD3, CD4; ICAM/VCAM lökositlerin yerleşmesi (homing) ve <b>inflamasyonda</b>; patolojiler (MS) ve metastaz'],
        ['<b>III. Selectins</b>', '<b>lökositlerin endotel hücrelerine</b> bağlanması; trombosit ve lökositlerin lenf düğümü ve dokulara geçişi; <b>düşük afiniteli, geçici</b>', '—', '<b>L-selectin</b> (lökosit), <b>P-selectin</b> (trombosit ve endotel), <b>E-selectin</b> (endotel)'],
        ['<b>IV. Integrins</b>', 'hücreyi hücreye ve <b>ECM\'ye</b> bağlar; <b>20\'den fazla</b> tip; <b>α + β heterodimer</b> (19 α, 8 β zinciri); ECM\'de <b>fibronektin ve laminin</b>, hücrede iskelet proteinlerine bağlanır', '<b>iki değerlikli katyona bağımlı</b> (Me²⁺)', 'tanıma dizisi <b>RGD</b> (arginin–glisin–aspartat); ECM (fibronektin), kan proteinleri (fibrinojen, von Willebrand faktörü)']]))
    add(TRAP('Kaderin/katenin kaybı = metastaz', '<p>Kaderin ya da katenin kaybı hücrelerin birbirinden ayrılmasına ve <b>metastaza</b> izin verir: <b>epithelial–mesenchymal transition (EMT)</b>.</p>'))
    k.h3('Enfeksiyonda lökositin damar dışına çıkışı (extravasation)')
    add('<p>Enfeksiyonda sitokinlerin (<b>IL-1, TNF</b>) etkisiyle endotelde önce <b>P-selektin</b> (nötrofillerin geçişi için), sonra <b>E-selektin</b> (makrofajlar için) ifade edilir. Basamaklar: '
        '<b>1) tethering and rolling</b> (yuvarlanma: selektin–karbonhidrat ligandı) → <b>2) signaling</b> (kemokinler integrinleri etkinleştirir) → <b>3) firm adhesion</b> (sıkı yapışma: integrin–ICAM/VCAM) → <b>4) extravasation</b> (damar dışına çıkış). '
        'L-selektin lökositlerde, E- ve P-selektin etkin endotel hücrelerinde bulunur.</p>')
    k.h3('İntegrinlerin iki görevi')
    add('<p><b>1) Hücre iskeletini ECM\'ye bağlar</b>: integrin, hücre içinde <b>talin, vinculin, α-actinin, paxillin, tensin, ILK, parvin</b> gibi proteinlerle aktine bağlanır. '
        '<b>2) ECM\'den hücreye sinyal iletir</b>: <b>focal adhesion kinase (FAK)</b> üzerinden çekirdeğe sinyal gider; hücre iskeleti ve hücre uyarana yanıt verir.</p>')
    add(TABLE(['İntegrin (slayt)', 'Ligand', 'Dağılım'], [
        ['α5β1', 'fibronectin', 'her hücre'], ['α6β1', 'laminin', 'her hücre'], ['α7β1', 'laminin', 'kas hücreleri'],
        ['αLβ1 (slayttaki yazım)', 'Ig süperailesi', 'lökositler'], ['α2β3 (slayttaki yazım)', 'fibrinogen', 'trombositler'], ['<b>α6β4</b>', 'laminin', '<b>hemidesmozomlar</b>']]))
    add('<p><b>ECM ve adezyonla ilgili hastalıklar</b>: mutant formlar ya da sentez kusurları, ECM sentez/yıkım kusurları, otoimmün hastalıklar: <b>skorbüt (scurvy)</b>, <b>mukopolisakkaridoz</b>, <b>metastaz</b>, <b>romatoid artrit</b>, <b>sistemik lupus eritematozus</b>. '
        '<b>Disintegrins</b>: <b>yılan zehirindeki</b> küçük peptitler; <b>β1 ve β3</b> integrin bağlantısını bozar; <b>MMP etkinlikleri</b> vardır (ör. echistatin, kistrin, barbourin, triflavin, flavoridin…).</p>')
    add(KAV((T('Four CAM families', 'dört CAM ailesi'), 'cadherins, Ig-like CAMs, selectins, integrins'),
            (T('Catenin', 'katenin'), 'kaderinin hücre içi adaptör proteini'),
            (T('E / N / P-cadherin', 'E / N / P-kaderin'), 'epitel / sinir, lens, kas / trofoblast'),
            (T('EMT', 'epitel–mezenkim geçişi'), 'kaderin/katenin kaybı → metastaz'),
            (T('Selectins', 'selektinler'), 'L (lökosit), P (trombosit + endotel), E (endotel); düşük afinite, geçici'),
            (T('Integrins', 'integrinler'), 'αβ heterodimer (19α, 8β); Me²⁺ bağımlı; RGD dizisi; FAK ile sinyal'),
            (T('Disintegrins', 'dezintegrinler'), 'yılan zehri peptitleri; β1, β3 integrin bağlantısını bozar')))
    add(EXAM(
        ('Which family of adhesion molecules is calcium dependent and uses catenin as an intracellular adapter?', ['selectins', 'cadherins', 'Ig-like CAMs', 'integrins'], 'B', 'Kaderinler; uzun süreli tutunma.'),
        ('E-cadherin is typically found in:', ['epithelia', 'trophoblasts', 'heart muscle only', 'platelets'], 'A', 'N: sinir, lens, kas; P: trofoblast.'),
        ('Loss of cadherin or catenin allowing metastasis is called:', ['apoptosis', 'epithelial–mesenchymal transition (EMT)', 'extravasation', 'treadmilling'], 'B', 'EMT.'),
        ('Leukocyte binding to endothelial cells with low affinity, temporary connections is mediated by:', ['cadherins', 'selectins', 'connexins', 'desmogleins'], 'B', 'Selektinler.'),
        ('In infection, which selectin is expressed first on the endothelium to allow neutrophils to pass?', ['L-selectin', 'P-selectin', 'E-selectin', 'N-selectin'], 'B', 'Önce P, sonra E (makrofajlar).'),
        ('Integrins are:', ['homodimers of two α chains', 'heterodimers of α and β subunits', 'single-chain glycolipids', 'gap junction proteins'], 'B', '19 α ve 8 β zinciri.'),
        ('The protein recognition sequence of integrins is:', ['KDEL', 'RGD (arginine–glycine–aspartate)', 'NPA', 'PEST'], 'B', 'Fibronektindeki RGD.'),
        ('Signals from the ECM are transmitted into the cell through integrins mainly via:', ['focal adhesion kinase (FAK)', 'clathrin', 'catalase', 'cytochrome c'], 'A', 'FAK → çekirdek.'),
        ('Which integrin is found in hemidesmosomes?', ['α5β1', 'α6β4', 'α7β1', 'α2β3'], 'B', 'Laminine bağlanır.'),
        ('Disintegrins, which disrupt β1 and β3 integrin connections, are found in:', ['bacterial cell walls', 'snake venom', 'plant cell walls', 'mitochondria'], 'B', 'Yılan zehri; MMP etkinliği.'),
        ('ICAM-1 and VCAM-1 belong to which family?', ['cadherins', 'immunoglobulin-like CAMs', 'selectins', 'integrins'], 'B', 'Lökosit yerleşmesi ve inflamasyon.'),
    ))
