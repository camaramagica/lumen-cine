import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Lumen AI",
    page_icon="lumen.png",
    layout="centered",
    initial_sidebar_state="collapsed" 
)

# --- ESTILOS VISUALES (CLEAN DESIGN) ---
st.markdown("""
    <style>
    /* 1. FONDO DEGRADADO DORADO/ANARANJADO */
    .stApp {
        background: linear-gradient(135deg, #fce38a 0%, #f38181 100%);
        background-attachment: fixed;
    }

    /* 2. PRIVACIDAD: OCULTAR MENÚS */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 3. BOTONES PERSONALIZADOS */
    .stButton>button {
        background-color: #2D2D2D; 
        color: #Fce38a;
        border-radius: 8px;
        border: 2px solid #f38181;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #f38181;
        color: white;
        border-color: #2D2D2D;
        transform: scale(1.02);
    }

    /* 4. TIPOGRAFÍA */
    h1, h2, h3 { color: #2D2D2D !important; font-family: 'Helvetica', sans-serif; }
    
    /* 5. TARJETAS DE PELÍCULAS (Solo para el recomendador) */
    .movie-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #f38181;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* ELIMINADO EL BLOQUE QUE GENERABA LAS BARRAS BLANCAS */
    </style>
    """, unsafe_allow_html=True)

# --- CLASE PRINCIPAL ---
class LumenApp:
    def __init__(self):
        if 'page' not in st.session_state:
            st.session_state.page = "🏠 Inicio"

    def navigate_to(self, page_name):
        st.session_state.page = page_name

    def render_navigation(self):
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            opciones = ["🏠 Inicio", "🍿 Recomendador", "🎨 Inspiración Visual", "💾 Calculadora Data", "🔭 Lentes", "⏱️ Rodaje"]
            try:
                index_actual = opciones.index(st.session_state.page)
            except:
                index_actual = 0
                
            destino = st.selectbox("📍 **MENÚ RÁPIDO:**", opciones, index=index_actual, label_visibility="collapsed")
            
            if destino != st.session_state.page:
                st.session_state.page = destino
                st.rerun()

        with col2:
            if st.button("🏠 Home"):
                st.session_state.page = "🏠 Inicio"
                st.rerun()
        st.markdown("---")

    def main(self):
        if st.session_state.page != "🏠 Inicio":
            self.render_navigation()

        page = st.session_state.page

        if page == "🏠 Inicio":
            self.home_page()
        elif page == "🍿 Recomendador":
            self.movie_recommender()
        elif page == "🎨 Inspiración Visual":
            self.creative_assistant()
        elif page == "💾 Calculadora Data":
            self.data_calculator()
        elif page == "🔭 Lentes":
            self.lens_analyzer()
        elif page == "⏱️ Rodaje":
            self.scheduler()

    # --- PÁGINA PRINCIPAL ---
    def home_page(self):
        st.title("🎬 Lumen AI")
        st.markdown("### Asistente de Producción Cinematográfica")
        st.markdown("Bienvenido al sistema **Lumen Gold Edition**.")
        
        # Botones grandes
        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)
        c5, c6 = st.columns(2)
        
        with c1: 
            if st.button("🍿 CINE RECOMENDADOR"): self.navigate_to("🍿 Recomendador"); st.rerun()
        with c2: 
            if st.button("🎨 DIRECTOR CREATIVO"): self.navigate_to("🎨 Inspiración Visual"); st.rerun()
        with c3: 
            if st.button("💾 DATA CALCULATOR"): self.navigate_to("💾 Calculadora Data"); st.rerun()
        with c4: 
            if st.button("🔭 LENTES Y ÓPTICA"): self.navigate_to("🔭 Lentes"); st.rerun()
        with c5: 
            if st.button("⏱️ PLAN DE RODAJE"): self.navigate_to("⏱️ Rodaje"); st.rerun()
            
    # --- MÓDULOS ---
    
    def movie_recommender(self):
        st.header("🍿 Lumen Recomienda")
        genre = st.selectbox("Elige un Género:", ["Ciencia Ficción", "Terror", "Drama", "Comedia", "Fotografía Épica", "Animación", "Thriller"])
        
        library = {
            "Ciencia Ficción": ["Blade Runner 2049", "Dune", "Arrival", "Ex Machina", "Interstellar", "2001: Odisea del Espacio", "Matrix", "Alien", "Children of Men", "Her", "Gattaca", "Under the Skin", "Moon", "District 9", "Dark City", "Solaris", "Stalker", "Metropolis", "Brazil", "Inception", "Tenet", "The Thing", "E.T.", "Close Encounters", "Contact", "Primer", "Coherence", "Annihilation", "Sunshine", "Ad Astra", "Minority Report", "Edge of Tomorrow", "Looper", "12 Monkeys", "Akira", "Ghost in the Shell", "Paprika", "Donnie Darko", "Source Code", "Videodrome", "The Fly", "Robocop", "Total Recall", "Starship Troopers", "The Fifth Element"],
            "Terror": ["Hereditary", "The Witch", "Midsommar", "The Shining", "Get Out", "Psycho", "The Exorcist", "Alien", "The Thing", "Rosemary's Baby", "Suspiria", "Halloween", "Texas Chainsaw Massacre", "Scream", "The Lighthouse", "It Follows", "Let the Right One In", "Train to Busan", "Raw", "Barbarian", "Talk to Me", "Silence of the Lambs", "Possession", "28 Days Later", "The Cabin in the Woods", "Evil Dead 2", "Blair Witch Project", "REC", "The Others", "Sixth Sense", "Poltergeist", "Carrie", "The Omen", "Hellraiser", "Candyman", "Babadook", "Saint Maud", "X", "Pearl", "Men", "Us", "Funny Games", "Audition"],
            "Drama": ["The Godfather", "Parasite", "Roma", "Citizen Kane", "Fight Club", "There Will Be Blood", "No Country for Old Men", "Moonlight", "Pulp Fiction", "Taxi Driver", "The Master", "Portrait of a Lady on Fire", "In the Mood for Love", "City of God", "Spirited Away", "Bicycle Thieves", "12 Angry Men", "Schindler's List", "Goodfellas", "Casino", "The Irishman", "Magnolia", "Boogie Nights", "Social Network", "Zodiac", "Se7en", "Amour", "The White Ribbon", "Oldboy", "Handmaiden", "Memories of Murder", "Drive My Car", "Shoplifters", "Burning", "Minari", "Past Lives", "Aftersun", "Worst Person in the World"],
            "Comedia": ["Grand Budapest Hotel", "Superbad", "Jojo Rabbit", "Dr. Strangelove", "Big Lebowski", "What We Do in the Shadows", "Monty Python Holy Grail", "Groundhog Day", "Knives Out", "Shaun of the Dead", "Hot Fuzz", "Mean Girls", "Palm Springs", "Lady Bird", "Truman Show", "In Bruges", "Frances Ha", "Singin in the Rain", "Some Like it Hot", "Annie Hall", "Midnight in Paris", "Zoolander", "Tropic Thunder", "Anchorman", "Borat", "Booksmart", "Barbie", "Poor Things", "The Favourite", "Lobster", "Licorice Pizza", "School of Rock", "Airplane!", "Naked Gun", "Young Frankenstein"],
            "Fotografía Épica": ["Lawrence of Arabia", "Barry Lyndon", "1917", "Dunkirk", "Oppenheimer", "The Revenant", "Hero", "Tree of Life", "Days of Heaven", "Thin Red Line", "Baraka", "Samsara", "Blade Runner", "Skyfall", "Mad Max Fury Road", "The Fall", "Amélie", "La La Land", "Apocalypse Now", "Ran", "Kagemusha", "Dreams", "First Man", "Ad Astra", "Assassination of Jesse James", "No Time to Die", "Sicario", "Prisoners", "Arrival", "Blade Runner 2049", "Neon Demon", "Drive", "Enter the Void", "Climax", "Spring Breakers"],
            "Animación": ["Spirited Away", "Princess Mononoke", "Akira", "Ghost in the Shell", "Spider-Verse", "Perfect Blue", "Paprika", "Grave of the Fireflies", "My Neighbor Totoro", "Howls Moving Castle", "End of Evangelion", "Your Name", "Weathering with You", "Suzume", "Wolf Children", "Girl Who Leapt Time", "Summer Wars", "Redline", "Fantastic Mr Fox", "Isle of Dogs", "Coraline", "Kubo", "Paranorman", "Persepolis", "Waltz with Bashir", "Flee", "Anomalisa", "Triplets of Belleville", "Illusionist", "Iron Giant", "LEGO Movie", "Rango", "Soul", "Inside Out"],
            "Thriller": ["Heat", "Collateral", "The Departed", "Se7en", "Zodiac", "Prisoners", "Sicario", "Nightcrawler", "Drive", "Uncut Gems", "Good Time", "No Country for Old Men", "Oldboy", "Memories of Murder", "Parasite", "Burning", "Handmaiden", "I Saw the Devil", "Chaser", "Yellow Sea", "Infernal Affairs", "Reservoir Dogs", "Snatch", "Lock Stock", "Gentlemen", "Usual Suspects", "LA Confidential", "Chinatown", "French Connection", "Bullitt", "Dirty Harry", "Fargo", "Big Lebowski", "Millers Crossing", "Blood Simple", "Blue Ruin", "Green Room"]
        }
        
        if st.button("🎲 SORPRENDEME LUMEN"):
            with st.spinner("Buscando joya oculta..."):
                time.sleep(0.5)
                movie = random.choice(library[genre])
                st.markdown(f"""
                <div class="movie-card">
                    <h2>🎬 {movie}</h2>
                    <p style="color:#444;">Género: <b>{genre}</b></p>
                    <p><i>"Una elección perfecta para hoy."</i></p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    def creative_assistant(self):
        st.header("🎨 Director Creativo")
        emotion = st.select_slider("¿Qué atmósfera buscas?", options=["Calma", "Nostalgia", "Romance", "Tensión", "Miedo", "Caos"])
        st.info(f"Análisis Técnico para: {emotion}")
        
        if emotion == "Calma":
            st.write("📹 **Lente:** 35mm o 50mm. \n💡 **Luz:** Suave y difusa. \n📐 **Soporte:** Trípode fijo.")
        elif emotion == "Nostalgia":
            st.write("📹 **Lente:** Vintage/Anamórfico. \n💡 **Luz:** Golden Hour (Cálida). \n🌫️ **Filtro:** ProMist 1/4.")
        elif emotion == "Tensión":
            st.write("📹 **Lente:** 85mm+ (Compresión). \n💡 **Luz:** Clave baja (Sombras duras). \n📐 **Ángulo:** Cerrados.")
        elif emotion == "Miedo":
            st.write("📹 **Lente:** Gran Angular distorsionado. \n💡 **Luz:** Cenital o desde abajo. \n📐 **Ángulo:** Picado.")
        elif emotion == "Caos":
            st.write("📹 **Cámara:** En mano (Shaky cam). \n⚙️ **Obturador:** 45 grados (Staccato). \n✂️ **Edición:** Cortes rápidos.")
        else:
            st.write("Busca poca profundidad de campo (f/1.8) para aislar a los personajes y colores pastel.")

    def data_calculator(self):
        st.header("💾 Calculadora de Data")
        c1, c2 = st.columns(2)
        res = c1.selectbox("Resolución", ["1080p", "4K", "6K", "8K"])
        fps = c2.number_input("FPS", value=24)
        mins = st.slider("Minutos de grabación", 1, 300, 10)
        
        bitrates = {"1080p": 185, "4K": 750, "6K": 1800, "8K": 2600}
        gb = ((bitrates[res] * (fps/24) * 60 * mins) / 8) / 1024
        
        st.success(f"Espacio Estimado (ProRes HQ): {gb:.2f} GB")

    def lens_analyzer(self):
        st.header("🔭 Analizador de Lentes")
        mm = st.slider("Distancia Focal (mm)", 8, 200, 50)
        st.subheader(f"Lente: {mm}mm")
        if mm < 35: st.write("📷 **GRAN ANGULAR:** Expande el espacio. Ideal para paisajes o distorsión.")
        elif mm < 55: st.write("👁️ **NORMAL:** Visión humana natural. Ideal documental y diálogo.")
        else: st.write("🔭 **TELEOBJETIVO:** Comprime el fondo. Ideal retratos y acción lejana.")

    def scheduler(self):
        st.header("⏱️ Plan de Rodaje")
        c1, c2 = st.columns(2)
        pags = c1.number_input("Páginas del Guion", value=90)
        ritmo = c2.number_input("Páginas por Día", value=4.0)
        if ritmo > 0:
            dias = pags / ritmo
            st.metric("Días estimados", f"{dias:.1f}", delta=f"Aprox {dias/5:.1f} Semanas")

# EJECUCIÓN
if __name__ == "__main__":
    app = LumenApp()
    app.main()

