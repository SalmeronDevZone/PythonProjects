CREATE TABLE preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta VARCHAR(255),
    falso_uno VARCHAR(255),
    falso_dos VARCHAR(255),
    respuesta VARCHAR(255)
);

-- Se debe editar la tabla añadiendo el nivel de dificultad.

-- Facil=f | Normal=n | dificil=d | muy dificil=x


-- PREGUNTAS FÁCILES:


INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿Cuál es la película donde un hombre llamado Edward tiene tijeras en lugar de manos?", "Titanic", "Forrest Gump", "Eduardo Manostijeras"),
("¿Quién interpretó el papel de Harry Potter en las películas de la saga?", "Daniel Radcliffe", "Rupert Grint", "Emma Watson"),
("¿Cuál es el color característico del vestido de Dorothy en la película 'El Mago de Oz'?", "Azul", "Verde", "Rojo"),
("¿En qué película se encuentra el famoso león llamado Simba?", "Toy Story", "Buscando a Nemo", "El Rey León"),
("¿Quién interpretó el papel de Batman en la trilogía dirigida por Christopher Nolan?", "Christian Bale", "Ben Affleck", "Michael Keaton"),
("¿Cuál es la película animada de Pixar sobre un robot solitario en la Tierra?", "Toy Story", "Monsters, Inc.", "Wall-E"),
("¿Quién es el protagonista de la película 'Forrest Gump'?", "Tom Cruise", "Matt Damon", "Tom Hanks"),
("¿En qué película una princesa llamada Ariel se enamora de un príncipe humano?", "Blancanieves", "Cenicienta", "La Sirenita"),
("¿Cuál es la película donde un niño llamado Kevin queda olvidado en casa durante las vacaciones de Navidad?", "Solo en casa", "Cariño, he encogido a los niños", "Solo en casa 2: Perdido en Nueva York"),
("¿Quién interpretó el papel de Jack en la película 'Titanic'?", "Brad Pitt", "Leonardo DiCaprio", "Tom Cruise");



INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿Quién interpreta a Iron Man en el Universo Cinematográfico de Marvel?", "Chris Hemsworth", "Mark Ruffalo", "Robert Downey Jr."),
("¿Cuál es el nombre del personaje principal en la saga 'El Señor de los Anillos'?", "Gandalf", "Legolas", "Frodo Bolsón"),
("¿Quién interpretó a Neo en la trilogía 'Matrix'?", "Keanu Reeves", "Brad Pitt", "Will Smith"),
("¿En qué película un joven mago llamado Harry descubre que es un mago y asiste a Hogwarts?", "El Hobbit", "El Rey León", "Harry Potter y la Piedra Filosofal"),
("¿Cuál es la película de Disney donde dos hermanas, Elsa y Anna, viven en un reino helado?", "La Sirenita", "Mulan", "Frozen: El reino del hielo"),
("¿Quién dirigió la película 'Jurassic Park'?", "Christopher Nolan", "Steven Spielberg", "James Cameron"),
("¿Cuál es la película de Disney sobre un león que se convierte en rey de la sabana?", "Madagascar", "El Rey León 2", "El Rey León"),
("¿Quién interpretó el papel de Hermione Granger en las películas de 'Harry Potter'?", "Emma Watson", "Daniel Radcliffe", "Rupert Grint"),
("¿En qué película un grupo de amigos viaja en el tiempo a través de un coche DeLorean?", "Volver al Futuro", "Doctor Strange", "Regreso al Futuro"),
("¿Cuál es la película donde un pez payaso llamado Nemo se pierde en el océano?", "Buscando a Dory", "Shark Tale", "Buscando a Nemo");


-- PREGUNTAS MODERADAS:


INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿Cuál es la película que ganó el Óscar a la Mejor Película en el año 2020?", "Parásitos", "1917", "Nomadland"),
("¿Quién interpretó el papel de Joker en la película del mismo nombre lanzada en 2019?", "Heath Ledger", "Joaquin Phoenix", "Jared Leto"),
("¿Cuál es el nombre del barco hundido en la película 'Titanic'?", "Queen Mary", "Carpathia", "RMS Titanic"),
("¿Quién es el director de la trilogía 'El Señor de los Anillos'?", "George Lucas", "Steven Spielberg", "Peter Jackson"),
("¿En qué película se encuentra el personaje Luke Skywalker?", "Star Trek", "La guerra de las galaxias", "Star Wars: Episodio IV - Una nueva esperanza"),
("¿Cuál es el nombre del mago más poderoso del universo de Harry Potter?", "Albus Dumbledore", "Severus Snape", "Lord Voldemort"),
("¿Quién es el director de la película 'Pulp Fiction'?", "Quentin Tarantino", "Martin Scorsese", "Steven Spielberg"),
("¿Cuál es la película animada de Pixar sobre un anciano que vuela a Sudamérica en una casa con globos?", "Monstruos University", "Los Increíbles", "Up"),
("¿Quién interpretó el papel de Rey en la nueva trilogía de 'Star Wars'?", "Daisy Ridley", "Adam Driver", "John Boyega"),
("¿En qué película un robot llamado WALL-E encuentra un brote de vida en un futuro distópico?", "Astro Boy", "El Gigante de Hierro", "Wall-E");



INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿En qué película el protagonista se queda atrapado en un bucle temporal reviviendo el mismo día una y otra vez?", "Origen", "Matrix", "El Día de la Marmota"),
("¿Quién interpretó el papel de James Bond en la película 'Skyfall'?", "Daniel Craig", "Pierce Brosnan", "Sean Connery"),
("¿Cuál es el nombre del mago protagonista de la saga de películas 'El Hobbit'?", "Gandalf", "Saruman", "Bilbo Bolsón"),
("¿Quién es el director de la película 'Interstellar'?", "Christopher Nolan", "Denis Villeneuve", "James Cameron"),
("¿En qué película el personaje principal es un hacker que lucha contra una inteligencia artificial?", "Blade Runner", "Terminator", "Matrix"),
("¿Cuál es la película sobre un equipo de ladrones que planea robar un banco durante un juego de béisbol en Los Ángeles?", "Ocean's Eleven", "El Gran Truco", "La Gran Estafa"),
("¿Quién interpretó el papel de Don Vito Corleone en la película 'El Padrino'?", "Al Pacino", "Robert De Niro", "Marlon Brando"),
("¿Cuál es la película basada en la historia real de un hombre que queda atrapado en un aeropuerto durante meses?", "Náufrago", "La Terminal", "Atrápame si puedes"),
("¿Quién es el director de la película 'El Club de la Lucha'?", "David Fincher", "Quentin Tarantino", "Martin Scorsese"),
("¿En qué película el protagonista intenta sobrevivir en la naturaleza de Alaska después de un accidente de avión?", "127 horas", "Into the Wild", "El Renacido"),
("¿Cuál es la película donde un niño de 10 años se convierte en adulto de la noche a la mañana?", "Big", "Los Goonies", "Quisiera ser grande"),
("¿Quién interpretó el papel de Hannibal Lecter en la película 'El Silencio de los Corderos'?", "Anthony Hopkins", "Jodie Foster", "Jack Nicholson"),
("¿Cuál es la película de ciencia ficción sobre un ex convicto que se convierte en piloto de carreras ilegales en un futuro distópico?", "Blade Runner", "Ready Player One", "Rápidos y Furiosos"),
("¿En qué película el personaje principal tiene la habilidad de viajar en el tiempo solo si se encuentra en un armario?", "El Efecto Mariposa", "Donnie Darko", "Chronicle"),
("¿Cuál es la película sobre un grupo de personas que son encerradas en una habitación y tienen que encontrar pistas para escapar?", "Saw", "El Resplandor", "Escape Room");


-- PREGUNTAS DIFICILES:


INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿Cuál es la película donde un equipo de científicos viaja a un planeta extraterrestre en busca de un mineral precioso?", "Avatar", "Prometheus", "Alien: El Octavo Pasajero"),
("¿Quién interpretó el papel de Vito Corleone en la película 'El Padrino II'?", "Marlon Brando", "Al Pacino", "Robert De Niro"),
("¿Cuál es la película donde un niño ve muertos y busca ayuda de un psicólogo infantil?", "Sexto Sentido", "El Orfanato", "Los Otros"),
("¿Quién es el director de la película 'El Resplandor'?", "Alfred Hitchcock", "Stanley Kubrick", "David Fincher"),
("¿Cuál es la película sobre un hombre que queda atrapado en un bucle temporal y se convierte en un experto en piano y artes marciales?", "Source Code", "Looper", "Atrapado en el Tiempo"),
("¿Quién interpretó el papel de Andy Dufresne en la película 'Cadena Perpetua'?", "Morgan Freeman", "Tim Robbins", "Tom Hanks"),
("¿Cuál es la película donde un grupo de asesinos a sueldo es contratado para matar a un hombre con síndrome de Down?", "American Psycho", "The Hunt", "Green Room"),
("¿Quién es el director de la película 'El Gran Hotel Budapest'?", "Quentin Tarantino", "Martin Scorsese", "Wes Anderson"),
("¿Cuál es la película sobre un hombre que descubre que su realidad es una simulación y lucha contra las máquinas que lo controlan?", "Matrix", "Inception", "Dark City"),
("¿En qué película el protagonista es un hombre que vive la misma secuencia de eventos una y otra vez, pero siempre termina muriendo de diferentes maneras?", "Edge of Tomorrow", "Groundhog Day", "Triangle");



-- PREGUNTAS MUY DIFICILES:


INSERT INTO preguntas (pregunta, falso_uno, falso_dos, respuesta) VALUES
("¿Cuál es la película donde un hombre contrata a una empresa para que borre todos los recuerdos de su ex novia de su memoria?", "Eternal Sunshine of the Spotless Mind", "Memento", "Synecdoche, New York"),
("¿Quién interpretó el papel de Travis Bickle en la película 'Taxi Driver'?", "Robert De Niro", "Harvey Keitel", "Al Pacino"),
("¿Cuál es la película sobre un grupo de delincuentes que planea un robo en un banco utilizando máscaras de presidentes de los Estados Unidos?", "Inside Man", "Heat", "Point Break"),
("¿Quién es el director de la película '2001: Una Odisea del Espacio'?", "Stanley Kubrick", "Ridley Scott", "David Lynch"),
("¿Cuál es la película donde un hombre se despierta en una habitación sin recordar cómo llegó allí y debe seguir pistas para escapar?", "Cube", "Saw", "Oldboy");
