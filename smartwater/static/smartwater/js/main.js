$(document).ready(function () {
  // console.log('Saludos desde jquery');
  envio_informacion();
})

function envio_informacion() {
  $('#envio-datos').on("click", function (event) {
    event.preventDefault()

    $.ajax({
      url: 'nivel/save',
      method: 'post',
      contentType: 'application/json',
      data: JSON.stringify({
        id_dispositivo: 'h12827hag5',
        nivel: 78,
        motor: 0,
        fuente: 0
      }),
      success: function (respuesta) {
        console.log(respuesta)
        $(location).attr('href', '/smartwater');
      },
      error: function (error) {
        console.log(error)
      }
    });
  });
}
