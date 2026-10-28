"""Pruebas de integridad de AgroCiencia Del Norte, sin dependencias externas."""
from pathlib import Path
from html.parser import HTMLParser
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.hrefs=[]; self.frames=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a' and 'href' in a: self.hrefs.append(a['href'])
        if tag=='iframe' and 'src' in a: self.frames.append(a['src'])

class Integracion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.main=(ROOT/'index.html').read_text(encoding='utf-8')
        cls.child=(ROOT/'herramientas/agrosanidad-norte.html').read_text(encoding='utf-8')
        cls.indice=json.loads((ROOT/'datos/agrosanidad-indice.json').read_text(encoding='utf-8'))
    def test_nombre_y_separacion(self):
        self.assertIn('AgroCiencia Del Norte',self.main)
        self.assertNotIn('AgroCiencia Aplicada',self.main)
        self.assertIn('D E L  N O R T E',self.main)
        self.assertIn('OAF-Lambayeque',(ROOT/'GUIA_PUBLICACION.md').read_text(encoding='utf-8'))
    def test_publicacion(self):
        self.assertTrue((ROOT/'.nojekyll').exists())
        self.assertTrue((ROOT/'index.html').exists())
        self.assertTrue((ROOT/'herramientas/agrosanidad-norte.html').exists())
        self.assertTrue((ROOT/'datos/agrosanidad-indice.json').exists())
    def test_navegacion(self):
        p=Tags();p.feed(self.main)
        self.assertEqual(len(p.ids),len(set(p.ids)))
        for h in p.hrefs:
            if h.startswith('#') and len(h)>1:
                self.assertTrue(h[1:] in p.ids or ('data-page="'+h[1:]+'"') in self.main,h)
        for h in p.frames:
            if not h.startswith('http'):
                self.assertTrue((ROOT/h).is_file(),h)
    def test_catalogo(self):
        rows=self.indice['registros']
        self.assertEqual(len(rows),120)
        self.assertEqual(len({r['id'] for r in rows}),120)
        self.assertEqual({r['crop'] for r in rows},{'Mango','Palto','Arándano','Vid','Banano','Café','Maracuyá'})
        self.assertTrue(all(r['crop'] and r['type'] in ['IRAC','FRAC'] for r in rows))
    def test_puente(self):
        for token in ['AGRO_TOOL_SET_CONTEXT','AGRO_TOOL_READY','AGRO_TOOL_ACK','event.origin===location.origin']:
            self.assertIn(token,self.child)
        for token in ['AGRO_TOOL_SET_CONTEXT','integrationApply','integrationSearchRender','integraciones']:
            self.assertIn(token,self.main)
    def test_seguridad_y_evidencia(self):
        self.assertIn('SENASA SIGIA',self.main)
        self.assertIn('no se afirma una sincronización',self.main)
        self.assertNotIn('AGRO_DATA_FAKE',self.main)

if __name__=='__main__':unittest.main(verbosity=2)
