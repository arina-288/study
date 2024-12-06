# Справочник API
<div id="swagger-ui"></div>
<script>
  window.onload = function() {
    const ui = SwaggerUIBundle({
      url: "/study/study/swagger/openapi.yaml",
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
