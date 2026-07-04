# function that returns the html template as a string

def html_temp():
    html_template = """
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🎂 Game Master del Crucipuzzle per Lucry ✨</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f0f2f5;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                h1 { color: #333; text-align: center; margin-bottom: 30px; }
                
                .memory-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                    gap: 15px;
                    max-width: 800px;
                    width: 100%;
                }

                .card {
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    padding: 10px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    min-height: 180px;
                    cursor: pointer;
                    transition: transform 0.2s, background-color 0.3s;
                }
                .card:hover { transform: scale(1.02); }
                
                .card.locked { background-color: #3498db; color: white; }
                .card.locked .card-content { display: none; }
                .card.locked .card-number { font-size: 2.5rem; font-weight: bold; }

                .card.active { border: 3px solid #e67e22; background-color: #fff; cursor: default; }
                .card.active .card-number { display: none; }
                .card.active .card-content { display: flex; flex-direction: column; width: 100%; }

                .card.solved { border: 3px solid #2ecc71; background-color: #e8f8f5; cursor: default; }
                .card.solved .card-number { display: none; }
                .card.solved .card-content { display: flex; flex-direction: column; width: 100%; }
                .card.solved input, .card.solved button { display: none; }
                .card.solved .secret-word { display: block !important; color: #27ae60; font-weight: bold; text-align: center; margin-top: 5px; }

                img { width: 100%; max-height: 110px; object-fit: cover; border-radius: 8px; }
                input { width: 90%; padding: 6px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
                button { background-color: #e67e22; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
                button:hover { background-color: #d35400; }
                .secret-word { display: none; }
            </style>
        </head>
        <body>

            <h1>Buon compleanno Lucry! 🎉</h1>
            <h2>Noi buddhane ne diciamo di ✨buddhanate✨ eh?</h2>
            
            <div class="memory-grid" id="grid"></div>

            <script>
                let gameData = [];

                // Funzione di pulizia delle stringhe
                function cleanString(str) {
                    if (!str) return '';
                    return str.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
                }

                // Chiamata asincrona per caricare il file JSON esterno
                async function loadGameData() {
                    try {
                        const response = await fetch('data/game_data.json');
                        gameData = await response.json();
                        renderGrid();
                    } catch (error) {
                        console.error("Error loading game data JSON:", error);
                    }
                }

                function renderGrid() {
                    const grid = document.getElementById('grid');
                    grid.innerHTML = '';

                    gameData.forEach(item => {
                        const savedState = localStorage.getItem(`card_${item.id}`) || 'locked';
                        
                        const card = document.createElement('div');
                        card.className = `card ${savedState}`;
                        card.id = `card-${item.id}`;

                        // Utilizzo delle proprietà .image e .solution mappate dal JSON
                        card.innerHTML = `
                            <div class="card-number">${item.id}</div>
                            <div class="card-content">
                                <img src="${item.image}" alt="Indizio ${item.id}">
                                <input type="text" id="input-${item.id}" placeholder="Cosa rappresenta?" autocomplete="off">
                                <button onclick="checkAnswer(${item.id}, event)">Invia</button>
                                <div class="secret-word">${item.solution}</div>
                            </div>
                        `;

                        card.addEventListener('click', () => {
                            if (card.classList.contains('locked')) {
                                document.querySelectorAll('.card.active').forEach(c => {
                                    c.className = 'card locked';
                                });
                                card.className = 'card active';
                            }
                        });

                        grid.appendChild(card);
                    });
                }

                function checkAnswer(id, event) {
                    event.stopPropagation();
                    const inputVal = document.getElementById(`input-${id}`).value;
                    const targetData = gameData.find(item => item.id === id);

                    // Confronto eseguito usando targetData.solution
                    if (cleanString(inputVal) === cleanString(targetData.solution)) {
                        alert("La risposta è giusta! ✨\\n\\nTrovala nel crucipuzzle 😎");
                        localStorage.setItem(`card_${id}`, 'solved');
                        renderGrid();
                    } else {
                        alert("Uhhmm riprova");
                    }
                }

                window.onload = loadGameData;
            </script>
        </body>
        </html>
        """
    
    return html_template