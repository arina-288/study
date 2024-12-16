# Справочник API
<div id="swagger-ui"></div>
<script>
  window.onload = function() {
    const ui = SwaggerUIBundle({
      //url: "/swagger/openapi.yaml",// для локальной сборки
      url: "/study/swagger/openapi.yaml", // для сборки в гите
      dom_id: '#swagger-ui',
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIStandalonePreset
      ],
      layout: "StandaloneLayout"
    })
    window.ui = ui
  }
</script>
