function atualizarDataHora() {
      const agora = new Date();
      document.getElementById('dataHora').innerText = agora.toLocaleString();
    }
    setInterval(atualizarDataHora, 1000);

function carregarEventos() {
  fetch('http://localhost:3000/eventos')
  .then(res => res.json())
  .then(data => {
    const eventos = data;
    const container = document.getElementById('eventos');
    container.innerHTML = '';
    eventos.forEach(evento => {
      const div = document.createElement('div');
      div.classList.add('evento');
      div.innerHTML = `
      <h3>${evento.titulo}</h3>
      <p><strong>Horário:</strong> ${evento.horario}</p>
      <p>${evento.descricao}</p>
      <p><em>Palestrante:</em> ${evento.palestrante}</p>
      <hr>
        `;
      container.appendChild(div);
      });
    })
  .catch(err => {
    console.error('Erro ao carregar eventos:', err);
    document.getElementById('eventos').innerHTML = "<p>Não foi possível carregar os eventos.</p>";
  });
}

    carregarEventos();