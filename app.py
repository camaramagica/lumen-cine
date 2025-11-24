import streamlit as st
import random
import time
from PIL import Image
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Lumen AI",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- ESTILOS VISUALES (CSS GOLD & PRIVACY) ---
st.markdown("""
    <style>
    /* 1. FONDO DEGRADADO DORADO/ANARANJADO */
    .stApp {
        background: linear-gradient(135deg, #fce38a 0%, #f38181 100%);
        background-attachment: fixed;
    }

    /* 2. OCULTAR MENÚS DE STREAMLIT (PRIVACIDAD) */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 3. ESTILO DE BOTONES (PRO) */
    .stButton>button {
        background-color: #2D2D2D; /* Botón oscuro para contraste */
        color: #Fce38a; /* Texto dorado */
        border-radius: 10px;
        border: 2px solid #f38181;
        font-weight: bold;
        width: 100%;
        height: 3.5em;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #f38181;
        color: white;
        border-color: #2D2D2D;
    }

    /* 4. TIPOGRAFÍA */
    h1, h2, h3 {
        color: #2D2D2D !important;
        font-family: 'Helvetica', sans-serif;
    }
    .stMarkdown p {
        color: #1a1a1a;
        font-weight: 500;
    }
    
    /* 5. TARJETAS DE PELÍCULAS */
    .movie-card {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #f38181;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CLASE PRINCIPAL ---
class LumenApp:
    def __init__(self):
        # Inicializar estado de navegación
        if 'page' not in st.session_state:
            st.session_state.page = "Home"

    def navigate_to(self, page):
        st.session_state.page = page

    def render_sidebar(self):
        with st.sidebar:
            st.header("🎛️ Menú Lumen")
            
            # Botones de navegación personalizados
            if st.button("🏠 INICIO"): self.navigate_to("Home")
            st.markdown("---")
            if st.button("🍿 Recomendador"): self.navigate_to("Recommender")
            if st.button("🎨 Inspiración Visual"): self.navigate_to("Creative")
            if st.button("💾 Calculadora Data"): self.navigate_to("Data")
            if st.button("🔭 Lentes"): self.navigate_to("Lens")
            if st.button("⏱️ Rodaje"): self.navigate_to("Scheduler")
            
            st.markdown("---")
            st.caption("Lumen v5.0 Gold Edition")
            st.caption("Sistema Privado")

    def main(self):
        self.render_sidebar()

        # LÓGICA DE NAVEGACIÓN
        page = st.session_state.page

        if page == "Home":
            self.home_page()
        elif page == "Recommender":
            self.movie_recommender()
        elif page == "Creative":
            self.creative_assistant()
        elif page == "Data":
            self.data_calculator()
        elif page == "Lens":
            self.lens_analyzer()
        elif page == "Scheduler":
            self.scheduler()

    # --- PÁGINA PRINCIPAL (HOME) ---
    def home_page(self):
        # Intentar cargar el logo
        try:
            # Busca el archivo lumen.jpg en el directorio
            st.image("lumen.png", width=300) 
        except:
            st.warning("⚠️ No encuentro 'lumen.png'. Asegúrate de subir la foto a GitHub.")
            st.title("🤖 Lumen")

        st.title("Bienvenido, Director.")
        st.markdown("""
        ### Soy Lumen, tu asistente de producción impulsado por IA.
        
        Estoy diseñado para asistirte en cada etapa de tu proceso creativo:
        
        * **Bloqueo creativo?** Pídeme una película.
        * **¿Dudas técnicas?** Calculo el espacio en disco y lentes.
        * **¿Pre-producción?** Organizo tu plan de rodaje.
        
        👈 **Usa el menú de la izquierda para comenzar.**
        """)
        
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("🚀 INICIAR SISTEMA"):
                self.navigate_to("Recommender")

    # --- MÓDULOS ---
    
    def movie_recommender(self):
        st.header("🍿 Lumen Recomienda")
        st.markdown("Base de datos desbloqueada. 500+ Títulos.")
        
        genre = st.selectbox("Género:", ["Ciencia Ficción", "Terror", "Drama", "Comedia", "Fotografía Épica", "Animación", "Thriller"])
        
        # (LISTAS ABREVIADAS PARA EL EJEMPLO - EN TU CÓDIGO FINAL MANTÉN LAS LISTAS LARGAS)
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
            with st.spinner("Consultando archivos..."):
                time.sleep(0.5)
                movie = random.choice(library[genre])
                st.markdown(f"""
                <div class="movie-card">
                    <h2>🎬 {movie}</h2>
                    <p>Género: {genre}</p>
                    <p><i>"Una elección perfecta para hoy."</i></p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    def creative_assistant(self):
        st.header("🎨 Director Creativo")
        emotion = st.select_slider("Intensidad Emocional", options=["Calma", "Nostalgia", "Romance", "Tensión", "Miedo", "Caos"])
        
        st.info(f"Análisis para: {emotion}")
        
        if emotion == "Calma":
            st.write("Lente: 35mm o 50mm. Luz suave y difusa. Trípode fijo.")
        elif emotion == "Nostalgia":
            st.write("Lente: Vintage/Anamórfico. Luz: Golden Hour. Filtros de difusión.")
        elif emotion == "Tensión":
            st.write("Lente: 85mm+ (Compresión). Luz: Clave baja. Ángulos cerrados.")
        elif emotion == "Miedo":
            st.write("Lente: Gran Angular distorsionado. Luz: Sombras duras. Ángulo: Picado.")
        elif emotion == "Caos":
            st.write("Cámara en mano (Shaky cam). Obturador a 45 grados. Cortes rápidos.")
        else:
            st.write("Busca poca profundidad de campo (f/1.8) para aislar a los personajes.")

    def data_calculator(self):
        st.header("💾 Calculadora")
        c1, c2 = st.columns(2)
        res = c1.selectbox("Resolución", ["1080p", "4K", "6K", "8K"])
        fps = c2.number_input("FPS", value=24)
        mins = st.slider("Minutos", 1, 300, 10)
        
        bitrates = {"1080p": 185, "4K": 750, "6K": 1800, "8K": 2600}
        gb = ((bitrates[res] * (fps/24) * 60 * mins) / 8) / 1024
        
        st.success(f"Espacio Estimado: {gb:.2f} GB")

    def lens_analyzer(self):
        st.header("🔭 Óptica")
        mm = st.slider("Milímetros (mm)", 8, 200, 50)
        st.subheader(f"{mm}mm")
        if mm < 35: st.write("GRAN ANGULAR: Expande el espacio.")
        elif mm < 55: st.write("NORMAL: Visión humana.")
        else: st.write("TELEOBJETIVO: Comprime el fondo.")

    def scheduler(self):
        st.header("⏱️ Plan de Rodaje")
        pags = st.number_input("Páginas", value=90)
        ritmo = st.number_input("Páginas/Día", value=4.0)
        if ritmo > 0:
            st.metric("Días estimados", f"{pags/ritmo:.1f}")

# EJECUCIÓN
if __name__ == "__main__":
    app = LumenApp()
    app.main()
