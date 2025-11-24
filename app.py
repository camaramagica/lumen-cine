import streamlit as st
import random
import time

# --- CONFIGURACIÓN INICIAL (Debe ser lo primero) ---
st.set_page_config(page_title="Lumen AI v4.0", page_icon="🎬", layout="wide")

# --- ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B; 
        color: white; 
        font-weight: bold;
    }
    .big-font { font-size: 20px !important; }
    .movie-title { font-size: 30px; font-weight: bold; color: #FAFAFA; }
    </style>
    """, unsafe_allow_html=True)

class LumenWeb:
    def __init__(self):
        self.name = "Lumen v4.0"

    def render(self):
        # Cabecera
        col1, col2 = st.columns([1, 4])
        with col1:
            st.write("## 🎬")
        with col2:
            st.title("Lumen: Cine Assistant")
            st.caption("Dirección • Fotografía • Producción • Inspiración")
        
        st.markdown("---")

        # Sidebar de Navegación
        with st.sidebar:
            st.header("🎛️ Panel de Control")
            menu = st.radio(
                "Módulos:",
                ["🍿 Lumen Recomienda (Extendido)", 
                 "🎨 Inspiración Visual", 
                 "💾 Calculadora de Data", 
                 "🔭 Analizador de Lentes", 
                 "⏱️ Calculadora de Rodaje"]
            )
            st.info("Lumen v4.0 ahora incluye una base de datos cinematográfica masiva.")

        # Enrutador
        if menu == "🎨 Inspiración Visual":
            self.creative_assistant()
        elif menu == "💾 Calculadora de Data":
            self.data_calculator()
        elif menu == "🔭 Analizador de Lentes":
            self.lens_analyzer()
        elif menu == "⏱️ Calculadora de Rodaje":
            self.scheduler()
        elif menu == "🍿 Lumen Recomienda (Extendido)":
            self.movie_recommender()

    # ------------------------------------------------------------------
    # MÓDULO 1: RECOMENDADOR MASIVO
    # ------------------------------------------------------------------
    def movie_recommender(self):
        st.header("🍿 Lumen Recomienda: La Bóveda")
        st.markdown("He desbloqueado mi base de datos completa. Elige tu veneno.")

        genre = st.selectbox("Selecciona Género:", 
            ["Ciencia Ficción", "Terror / Horror", "Drama & Autor", "Comedia & Sátira", "Fotografía Espectacular", "Animación Adulta", "Thriller / Crimen"])

        # --- BASE DE DATOS (Compactada para eficiencia) ---
        library = {
            "Ciencia Ficción": [
                "Blade Runner 2049", "Ex Machina", "Arrival", "Dune (Part 1 & 2)", "The Matrix", "Children of Men", 
                "2001: A Space Odyssey", "Interstellar", "Solaris (Tarkovsky)", "Her", "District 9", "Gattaca", 
                "Under the Skin", "Minority Report", "The Thing", "Alien", "Aliens", "Inception", "Brazil", "Dark City", 
                "Moon", "Primer", "Coherence", "Eternal Sunshine of the Spotless Mind", "Stalker", "Metropolis", 
                "Akira", "Ghost in the Shell", "Paprika", "Donnie Darko", "The Prestige", "Tenet", "Edge of Tomorrow", 
                "Looper", "Source Code", "12 Monkeys", "Contact", "Close Encounters of the Third Kind", "E.T.", 
                "The Fly (Cronenberg)", "Videodrome", "RoboCop (1987)", "Total Recall", "Starship Troopers", "The Fifth Element",
                "Predator", "Terminator 2", "Back to the Future", "A.I. Artificial Intelligence", "War of the Worlds (2005)",
                "Gravity", "The Martian", "Sunshine", "Ad Astra", "High Life", "Aniara", "Possessor", "Crimes of the Future",
                "Nope", "Everything Everywhere All At Once", "Scanners", "Existenz", "Cube", "Limitless", "Melancholia"
            ],
            "Terror / Horror": [
                "Hereditary", "The Witch", "Midsommar", "The Shining", "Get Out", "Psycho", "The Exorcist", "It Follows", 
                "Rosemary's Baby", "Suspiria (1977)", "Suspiria (2018)", "The Lighthouse", "Let the Right One In", 
                "Train to Busan", "Raw", "Titane", "Barbarian", "Talk to Me", "Silence of the Lambs", "Possession (1981)", 
                "28 Days Later", "The Texas Chain Saw Massacre", "Halloween (1978)", "A Nightmare on Elm Street", 
                "Scream", "The Cabin in the Woods", "Evil Dead II", "The Blair Witch Project", "REC", "The Others", 
                "The Sixth Sense", "Poltergeist", "Carrie", "The Omen", "Hellraiser", "Candyman", "The Babadook", 
                "It Comes at Night", "Saint Maud", "X", "Pearl", "Men", "Us", "Funny Games", "Audition", "Ringu", 
                "Ju-on", "Dark Water", "Pulse (Kairo)", "The Wailing", "I Saw the Devil", "Martyrs", "Inside", "Green Room",
                "Don't Look Now", "Eraserhead", "Jacob's Ladder", "Angel Heart", "Malignant", "Drag Me to Hell"
            ],
            "Drama & Autor": [
                "Whiplash", "The Godfather", "The Godfather Part II", "Parasite", "Roma", "Citizen Kane", "Fight Club", 
                "There Will Be Blood", "No Country for Old Men", "Moonlight", "Pulp Fiction", "Taxi Driver", "The Master", 
                "Portrait of a Lady on Fire", "Chungking Express", "In the Mood for Love", "City of God", "La Haine", 
                "Spirited Away", "Bicycle Thieves", "12 Angry Men", "Schindler's List", "Goodfellas", "Casino", "The Irishman",
                "Magnolia", "Boogie Nights", "Phantom Thread", "Punch-Drunk Love", "Marriage Story", "The Social Network",
                "Zodiac", "Se7en", "Gone Girl", "Amour", "The White Ribbon", "Cache", "Piano Teacher", "Oldboy", "The Handmaiden",
                "Decision to Leave", "Memories of Murder", "Drive My Car", "Shoplifters", "Burning", "Minari", "Past Lives",
                "Aftersun", "The Worst Person in the World", "Another Round", "The Hunt", "Triangle of Sadness", "The Square",
                "Force Majeure", "Y Tu Mamá También", "Amores Perros", "Babel", "Biutiful", "Birdman", "The Revenant"
            ],
            "Comedia & Sátira": [
                "The Grand Budapest Hotel", "Superbad", "Jojo Rabbit", "Dr. Strangelove", "The Big Lebowski", 
                "What We Do in the Shadows", "Monty Python and the Holy Grail", "Life of Brian", "Groundhog Day", 
                "Knives Out", "Glass Onion", "Shaun of the Dead", "Hot Fuzz", "The World's End", "Mean Girls", 
                "Palm Springs", "Lady Bird", "The Truman Show", "In Bruges", "The Banshees of Inisherin", "Frances Ha", 
                "Singin' in the Rain", "Some Like It Hot", "The Apartment", "Annie Hall", "Manhattan", "Midnight in Paris", 
                "Zoolander", "Tropic Thunder", "Anchorman", "Step Brothers", "Talladega Nights", "Borat", "Bruno", 
                "The Dictator", "Booksmart", "Bottoms", "Barbie", "Poor Things", "The Favourite", "The Lobster", 
                "Killing of a Sacred Deer", "Licorice Pizza", "American Graffiti", "Dazed and Confused", "Everybody Wants Some!!",
                "School of Rock", "Bernie", "Best in Show", "Waiting for Guffman", "A Fish Called Wanda", "Airplane!", 
                "The Naked Gun", "Top Secret!", "Young Frankenstein", "Blazing Saddles"
            ],
            "Fotografía Espectacular": [
                "Lawrence of Arabia", "Barry Lyndon", "1917", "Dunkirk", "Oppenheimer", "Hero", "House of Flying Daggers", 
                "Crouching Tiger, Hidden Dragon", "The Tree of Life", "Days of Heaven", "The Thin Red Line", "The New World", 
                "Baraka", "Samsara", "Koyaanisqatsi", "Blade Runner (1982)", "Skyfall", "Mad Max: Fury Road", "Furiosa", 
                "The Fall", "The Cell", "Amélie", "La La Land", "Babylon", "Apocalypse Now", "Ran", "Kagemusha", "Dreams", 
                "Mishima: A Life in Four Chapters", "First Man", "Ad Astra", "The Assassination of Jesse James", 
                "No Time to Die", "Sicario", "Prisoners", "Enemy", "Arrival", "Blade Runner 2049", "Dune", "Euphoria (Series style)",
                "Saltburn", "The Neon Demon", "Only God Forgives", "Drive", "Valhalla Rising", "Bronson", "Enter the Void", 
                "Climax", "Love", "Irreversible", "Spring Breakers", "Florida Project", "Tangerine", "Red Rocket"
            ],
            "Thriller / Crimen": [
                "Heat", "Collateral", "The Departed", "Infernal Affairs", "Reservoir Dogs", "Snatch", "Lock, Stock and Two Smoking Barrels",
                "The Gentlemen", "RocknRolla", "The Usual Suspects", "L.A. Confidential", "Chinatown", "The French Connection",
                "Bullitt", "Dirty Harry", "Uncut Gems", "Good Time", "Nightcrawler", "Prisoners", "Mystic River", "Gone Baby Gone",
                "The Town", "Argo", "Sicario", "Wind River", "Hell or High Water", "No Country for Old Men", "Blue Ruin",
                "Green Room", "I Don't Feel at Home in This World Anymore", "Fargo", "The Big Lebowski", "Miller's Crossing",
                "Blood Simple", "Memories of Murder", "Mother", "Parasite", "The Chaser", "The Yellow Sea", "New World (Korean)"
            ],
             "Animación Adulta": [
                "Spirited Away", "Princess Mononoke", "Howl's Moving Castle", "My Neighbor Totoro", "Kiki's Delivery Service",
                "Porco Rosso", "The Wind Rises", "The Boy and the Heron", "Grave of the Fireflies", "Akira", "Ghost in the Shell",
                "Perfect Blue", "Paprika", "Tokyo Godfathers", "Millennium Actress", "Cowboy Bebop: The Movie", "End of Evangelion",
                "Your Name", "Weathering with You", "Suzume", "A Silent Voice", "Wolf Children", "The Girl Who Leapt Through Time",
                "Summer Wars", "Redline", "Vampire Hunter D: Bloodlust", "Ninja Scroll", "Fantastic Mr. Fox", "Isle of Dogs",
                "Spider-Man: Into the Spider-Verse", "Across the Spider-Verse", "The Mitchells vs. the Machines", "Puss in Boots: The Last Wish",
                "The Lego Movie", "Rango", "Coraline", "Kubo and the Two Strings", "Paranorman", "Mary and Max", "Persepolis",
                "Waltz with Bashir", "Flee", "Anomalisa", "I Lost My Body", "The Triplets of Belleville", "The Illusionist"
            ]
        }

        col1, col2 = st.columns([2, 1])
        
        with col1:
            if st.button("🎲 GENERAR RECOMENDACIÓN", help="Click para obtener una película aleatoria"):
                # Efecto de carga
                with st.spinner("Buscando en los archivos de Lumen..."):
                    time.sleep(0.4)
                    movie = random.choice(library[genre])
                    
                    st.markdown("---")
                    st.caption(f"Género seleccionado: {genre}")
                    st.markdown(f'<p class="movie-title">{movie}</p>', unsafe_allow_html=True)
                    
                    # Generamos una razón falsa pero creíble (o genérica) para simular IA
                    reasons = [
                        "Por su dirección de arte impecable.",
                        "Por el uso magistral de la iluminación.",
                        "Una clase maestra de guion.",
                        "Rompe todas las reglas del género.",
                        "Imprescindible para cualquier cineasta.",
                        "Atención al diseño sonoro en esta cinta.",
                        "Fíjate en cómo mueven la cámara.",
                        "La estructura narrativa es única."
                    ]
                    st.info(f"💡 **Lumen dice:** {random.choice(reasons)}")
                    st.balloons()

        with col2:
            st.write("### Historial")
            st.caption("Las últimas sugerencias aparecerán aquí si implementas una base de datos local.")
            st.write("*(Esta función requiere memoria persistente)*")

    # ------------------------------------------------------------------
    # MÓDULOS TÉCNICOS (Optimizados)
    # ------------------------------------------------------------------
    def creative_assistant(self):
        st.header("🎨 Inspiración Visual")
        col1, col2 = st.columns(2)
        with col1:
            emotion = st.selectbox("Emoción:", ["Tensión", "Nostalgia", "Euforia", "Soledad", "Romance", "Caos"])
        
        if st.button("Analizar"):
            st.success(f"Análisis para: {emotion}")
            if emotion == "Tensión":
                st.write("**Lente:** >85mm (Compresión). **Luz:** Clave baja. **Ángulo:** Picado.")
            elif emotion == "Nostalgia":
                st.write("**Lente:** Vintage/Anamórfico. **Luz:** Golden Hour. **Filtro:** ProMist 1/4.")
            elif emotion == "Euforia":
                st.write("**Lente:** Gran Angular (16mm). **Movimiento:** Snorricam/Steadicam rápido.")
            elif emotion == "Soledad":
                st.write("**Lente:** Gran Angular. **Encuadre:** Gran Plano General (Sujeto pequeño).")
            else:
                st.write("Usa la psicología del color para potenciar esta emoción.")

    def data_calculator(self):
        st.header("💾 Data Wrangling")
        st.caption("Cálculo estimado para ProRes 422 HQ")
        c1, c2, c3 = st.columns(3)
        res = c1.selectbox("Resolución", ["1080p", "4K", "6K", "8K"])
        fps = c2.number_input("FPS", 24, 120, 24)
        min = c3.number_input("Minutos", 1, 500, 10)
        
        # Mapeo de bitrates aproximados (Mbps)
        bitrates = {"1080p": 185, "4K": 750, "6K": 1800, "8K": 2600}
        
        total_gb = ((bitrates[res] * (fps/24) * 60 * min) / 8) / 1024
        st.metric("Espacio Requerido", f"{total_gb:.2f} GB")

    def lens_analyzer(self):
        st.header("🔭 Óptica")
        mm = st.slider("Distancia Focal (mm)", 8, 200, 50)
        if mm < 16: st.warning("Ojo de Pez / Ultra Gran Angular")
        elif mm < 35: st.success("Gran Angular (Espacio expandido)")
        elif mm < 55: st.info("Normal (Visión Humana)")
        elif mm < 100: st.success("Teleobjetivo Corto (Retrato)")
        else: st.warning("Teleobjetivo Largo (Compresión extrema)")

    def scheduler(self):
        st.header("⏱️ Plan de Rodaje")
        pags = st.number_input("Páginas del guion", 1, 200, 90)
        ritmo = st.slider("Páginas por día", 0.5, 10.0, 4.0)
        dias = pags / ritmo
        st.metric("Días de Rodaje", f"{dias:.1f}", delta=f"{dias/5:.1f} Semanas")

if __name__ == "__main__":
    app = LumenWeb()
    app.render()