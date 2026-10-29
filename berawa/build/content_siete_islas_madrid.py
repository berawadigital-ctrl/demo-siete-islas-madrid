# Contenido de la demo 7 Islas Hotel (Madrid) (es/ca/en/fr). Hechos de 7islashotel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación Easy','Habitación Deluxe','Ático con terraza'],
'ca':['Habitació Easy','Habitació Deluxe','Àtic amb terrassa'],
'en':['Easy Room','Deluxe Room','Penthouse with Terrace'],
'fr':['Chambre Easy','Chambre Deluxe','Penthouse avec terrasse']}
RD={
'es':['17 m², camas queen size o twin. Pensada para una estancia urbana, con amenities de Malin + Goetz y detalles de diseño de Kikekeller.','23 m², luminosa, con vistas a la calle Valverde o al patio interior. Con escritorio y minibar gourmet.','31 m² en la planta superior, con terraza privada, hamacas y kit de yoga. Camas king size o twin.'],
'ca':['17 m², llits queen size o twin. Pensada per a una estada urbana, amb amenities de Malin + Goetz i detalls de disseny de Kikekeller.','23 m², lluminosa, amb vistes al carrer Valverde o al pati interior. Amb escriptori i minibar gourmet.','31 m² a la planta superior, amb terrassa privada, hamaques i kit de ioga. Llits king size o twin.'],
'en':['17 m², queen size or twin beds. Made for a city stay, with Malin + Goetz amenities and Kikekeller design details.','23 m², bright, with views of Valverde street or the inner courtyard. With a desk and gourmet minibar.','31 m² on the top floor, with a private terrace, hammocks and a yoga kit. King size or twin beds.'],
'fr':['17 m², lits queen size ou twin. Pensée pour un séjour urbain, avec produits Malin + Goetz et détails de design de Kikekeller.','23 m², lumineuse, avec vue sur la rue Valverde ou sur la cour intérieure. Avec bureau et minibar gourmet.','31 m² à l\'étage supérieur, avec terrasse privée, hamacs et kit de yoga. Lits king size ou twin.']}
ART={
'hero':('skyline',7101,['#2a4a58','#e8855f','#ffd9a0','#27434f','#1c3440','#122630']),
'intro':('arches',7102,['#dfe9e4','#f2f1e4','#e29a72','#7fae9f','#2f6e6a']),
'r1':('columns',7111,['#e0e9e3','#f1f0e2','#dd8d68','#8bb3a6','#3d7873']),
'r2':('arches',7112,['#e4e2d3','#f3efdd','#d97b57','#9bb7a8','#4a7f78']),
'r3':('skyline',7113,['#2f5260','#f19a70','#ffe2b0','#2d4c5a','#20404d','#15303c']),
'g1':('skyline',7121,['#3a4f70','#e8996a','#fbd9a0','#34496a','#283c58','#1b2c44']),
'g2':('columns',7122,['#dfe6e0','#f0efe0','#d8825e','#86ad9f','#376f6b']),
'g3':('arches',7123,['#e8dcc6','#f6ecd8','#e59b6a','#b88a62','#8d5c3d']),
'g4':('hills',7124,['#d6e6dc','#f4e8c8','#ffe7ae','#a0c9b0','#74a894','#4f8878']),
'g5':('waves',7125,['#f4dba8','#e99a74','#fff0be','#78b0c7','#4d8fac','#2f6f8e','#1a4d6a']),
'g6':('skyline',7126,['#2b3f5e','#e48a62','#fbd09a','#2a3e5c','#1f3249','#142234'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='7 Islas Hotel · Hotel de diseño entre la Gran Vía y Malasaña, Madrid',see_rooms='Ver habitaciones',hero_k='Madrid · Gran Vía y Malasaña',hero_t='Un hotel familiar de diseño entre la Gran Vía y Malasaña',hero_s='Habitaciones diseñadas por el estudio Kikekeller, bar y cocina propios y una galería de arte en el vestíbulo.',
 intro_t='Descanso, arte, diseño y gastronomía',intro_p1='7 Islas es uno de los pocos hoteles familiares que quedan en Madrid. Se inauguró en 2002 y hoy lo dirige la nieta del fundador.',
 intro_p2='Está en la calle Valverde, entre la Gran Vía y Malasaña. Tiene tres tipos de habitación, 7 Kitchen & Bar y una galería de arte con exposiciones itinerantes.',
 stats=['3 tipos de habitación','Gran Vía · Malasaña','7 Kitchen & Bar','Galería de arte'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Easy, Deluxe y ático con terraza.',
 svcs=['Wifi gratis','Acceso al gimnasio del hotel','Hervidor y selección de té','Caja fuerte y TV LCD','Minibar gourmet','Amenities Malin + Goetz','Servicio de lavandería','Pet friendly (solo perros)'],
 loc_p='C/ Valverde 14, 28004 Madrid, un oasis entre la Gran Vía madrileña y el barrio de Malasaña.',
 chips=['¿Qué tipos de habitación hay?','¿Admiten perros?','¿Hay restaurante o bar?','¿Cómo se reserva?']),
'ca':dict(title='7 Islas Hotel · Hotel de disseny entre la Gran Via i Malasaña, Madrid',see_rooms='Veure habitacions',hero_k='Madrid · Gran Via i Malasaña',hero_t='Un hotel familiar de disseny entre la Gran Via i Malasaña',hero_s='Habitacions dissenyades per l\'estudi Kikekeller, bar i cuina propis i una galeria d\'art al vestíbul.',
 intro_t='Descans, art, disseny i gastronomia',intro_p1='7 Islas és un dels pocs hotels familiars que queden a Madrid. Es va inaugurar el 2002 i avui el dirigeix la néta del fundador.',
 intro_p2='És al carrer Valverde, entre la Gran Via i Malasaña. Té tres tipus d\'habitació, 7 Kitchen & Bar i una galeria d\'art amb exposicions itinerants.',
 stats=['3 tipus d\'habitació','Gran Via · Malasaña','7 Kitchen & Bar','Galeria d\'art'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Easy, Deluxe i àtic amb terrassa.',
 svcs=['Wifi gratis','Accés al gimnàs de l\'hotel','Bullidor i selecció de te','Caixa forta i TV LCD','Minibar gourmet','Amenities Malin + Goetz','Servei de bugaderia','Pet friendly (només gossos)'],
 loc_p='C/ Valverde 14, 28004 Madrid, un oasi entre la Gran Via madrilenya i el barri de Malasaña.',
 chips=['Quins tipus d\'habitació hi ha?','Admeteu gossos?','Hi ha restaurant o bar?','Com es reserva?']),
'en':dict(title='7 Islas Hotel · Design hotel between Gran Vía and Malasaña, Madrid',see_rooms='See the rooms',hero_k='Madrid · Gran Vía and Malasaña',hero_t='A family-run design hotel between Gran Vía and Malasaña',hero_s='Rooms designed by the Kikekeller studio, its own bar and kitchen and an art gallery in the lobby.',
 intro_t='Rest, art, design and food',intro_p1='7 Islas is one of the few family hotels left in Madrid. It opened in 2002 and is now run by the founder\'s granddaughter.',
 intro_p2='It is on Calle Valverde, between Gran Vía and Malasaña. It has three room types, 7 Kitchen & Bar and an art gallery with travelling exhibitions.',
 stats=['3 room types','Gran Vía · Malasaña','7 Kitchen & Bar','Art gallery'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Easy, Deluxe and penthouse with terrace.',
 svcs=['Free wifi','Access to the hotel gym','Kettle and tea selection','Safe and LCD TV','Gourmet minibar','Malin + Goetz amenities','Laundry service','Pet friendly (dogs only)'],
 loc_p='C/ Valverde 14, 28004 Madrid, an oasis between Madrid\'s Gran Vía and the Malasaña neighbourhood.',
 chips=['What room types are there?','Are dogs allowed?','Is there a restaurant or bar?','How do I book?']),
'fr':dict(title='7 Islas Hotel · Hôtel design entre la Gran Vía et Malasaña, Madrid',see_rooms='Voir les chambres',hero_k='Madrid · Gran Vía et Malasaña',hero_t='Un hôtel familial design entre la Gran Vía et Malasaña',hero_s='Chambres dessinées par le studio Kikekeller, bar et cuisine propres et une galerie d\'art dans le hall.',
 intro_t='Repos, art, design et gastronomie',intro_p1='7 Islas est l\'un des rares hôtels familiaux qui restent à Madrid. Il a ouvert en 2002 et est aujourd\'hui dirigé par la petite-fille du fondateur.',
 intro_p2='Il se trouve calle Valverde, entre la Gran Vía et Malasaña. Il propose trois types de chambre, 7 Kitchen & Bar et une galerie d\'art avec des expositions itinérantes.',
 stats=['3 types de chambre','Gran Vía · Malasaña','7 Kitchen & Bar','Galerie d\'art'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Easy, Deluxe et penthouse avec terrasse.',
 svcs=['Wifi gratuit','Accès à la salle de sport de l\'hôtel','Bouilloire et sélection de thés','Coffre-fort et TV LCD','Minibar gourmet','Produits Malin + Goetz','Service de blanchisserie','Pet friendly (chiens uniquement)'],
 loc_p='C/ Valverde 14, 28004 Madrid, une oasis entre la Gran Vía madrilène et le quartier de Malasaña.',
 chips=['Quels types de chambre y a-t-il ?','Les chiens sont-ils admis ?','Y a-t-il un restaurant ou un bar ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='reservas@7islashotel.com')
D=dict(name='7 Islas Hotel',ac='#1f5c5a',ac2='#d1664a',ac2_a11y='#8f3a22',book=BOOK,around=[],foot=FOOT,
 address='C/ Valverde 14 · 28004 Madrid',phones=['91 523 46 88'],emails=['reservas@7islashotel.com'],maps='7 Islas Hotel, Calle Valverde 14, Madrid',t=T)
META=dict(repo='demo-siete-islas-madrid',name='7 Islas Hotel',legal_name='ISLA MADRID, S.L.',registry_ids=['CIF B35564046'],
 url='https://www.7islashotel.com/',domain='7islashotel.com',municipality='Madrid',province='Madrid',sector='hotel boutique de diseno en el centro',
 read_at='2026-10-29T01:25:00+01:00',created_at='2026-10-29T01:22:00+01:00',built_at='2026-10-29T01:50:00+01:00',audit_date='2026-10-29T01:22:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T01:21:38+01:00',url='https://www.google.com/maps/place/7+Islas+Hotel+Madrid/@40.4212052,-3.7019282,17z/data=!4m9!3m8!1s0xd42288790d76793:0x36f798568c536138!5m2!4m1!1i2!8m2!3d40.4212052!4d-3.7019282!16s%2Fg%2F1tcy03xp'),
 book=dict(mode='mail',email='reservas@7islashotel.com',note='La web del negocio reserva con un buscador/motor propio (Bookassist) sin URL propia: la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel urbano boutique de diseno (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay minibar y caja fuerte?','K02'),('¿Cuánto cuesta una noche?','K03'),('¿Admiten perros?','K04'),('¿Hay restaurante o bar?','K05'),('¿Hay early check-in?','K06'),('¿Hay una galería de arte?','K07'),('¿Cómo reservo?','K08'),('¿Dónde está?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Cuál es su historia?','K12'),('¿Hay gimnasio?','K02'),('¿Tienen piscina?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Cuántas estrellas tiene?',None)],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha minibar i caixa forta?','K02'),('Quant costa una nit?','K03'),('Admeteu gossos?','K04'),('Hi ha restaurant o bar?','K05'),('Hi ha early check-in?','K06'),('Hi ha una galeria d\'art?','K07'),('Com reservo?','K08'),('On és?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Quina és la seva història?','K12'),('Hi ha gimnàs?','K02'),('Teniu piscina?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Quantes estrelles té?',None)],
'en':[('What room types are there?','K01'),('Is there a minibar and a safe?','K02'),('How much is a night?','K03'),('Are dogs allowed?','K04'),('Is there a restaurant or bar?','K05'),('Is there early check-in?','K06'),('Is there an art gallery?','K07'),('How do I book?','K08'),('Where is it?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('What is its history?','K12'),('Is there a gym?','K02'),('Is there a swimming pool?',None),('Confirm that there is a free room tomorrow','K08'),('How many stars does it have?',None)],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il un minibar et un coffre-fort ?','K02'),('Combien coûte une nuit ?','K03'),('Les chiens sont-ils admis ?','K04'),('Y a-t-il un restaurant ou un bar ?','K05'),('Y a-t-il un early check-in ?','K06'),('Y a-t-il une galerie d\'art ?','K07'),('Comment réserver ?','K08'),('Où est-ce ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Quelle est son histoire ?','K12'),('Y a-t-il une salle de sport ?','K02'),('Y a-t-il une piscine ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Combien d\'étoiles a-t-il ?',None)]}
