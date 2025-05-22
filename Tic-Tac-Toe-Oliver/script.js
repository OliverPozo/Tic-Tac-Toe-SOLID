const api = "http://localhost:8000";

async function getState() {
  const [tab, player, winner, finished] = await Promise.all([
    fetch(api + "/tablero").then(r => r.json()),
    fetch(api + "/jugador").then(r => r.json()),
    fetch(api + "/ganador").then(r => r.json()),
    fetch(api + "/terminado").then(r => r.json()),
  ]);

  return {
    board: tab,
    player: player.jugador,
    winner: winner.ganador,
    finished: finished.terminado
  };
}

async function render() {
  const { board, player, winner, finished } = await getState();
  const table = document.getElementById("board");
  const status = document.getElementById("status");

  table.innerHTML = "";
  for (let i = 0; i < 3; i++) {
    const row = document.createElement("tr");
    for (let j = 0; j < 3; j++) {
      const cell = document.createElement("td");
      cell.textContent = board[i][j] || "";
      cell.onclick = () => makeMove(i, j);
      row.appendChild(cell);
    }
    table.appendChild(row);
  }

  if (finished) {
    status.textContent = winner === "Empate" ? "Draw!" : `Winner: ${winner}`;
  } else {
    status.textContent = `Turn: ${player}`;
  }
}

async function makeMove(row, col) {
  const finished = await fetch(api + "/terminado").then(r => r.json());
  if (finished.terminado) return;

  await fetch(api + "/mover", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ fila: row, columna: col })
  });

  render();
}

async function restart() {
  await fetch(api + "/reiniciar", { method: "POST" });
  render();
}

render();
