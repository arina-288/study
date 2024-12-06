# API Reference

<div id="swagger-ui"></div>
<script>
  window.onload = function() {
    const ui = SwaggerUIBundle({
      url: "{{ config.site_url }}/swagger/openapi.yaml",
      dom_id: '#swagger-ui',
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIStandalonePreset
      ],
      layout: "StandaloneLayout"
    })
    window.ui = ui

    // Удаление ненужных элементов после загрузки Swagger UI
    ui.initOauth({
      clientId: "your-client-id",
      clientSecret: "your-client-secret",
      realm: "your-realms",
      appName: "your-app-name",
      scopeSeparator: " ",
      additionalQueryStringParams: {}
    });

    ui.then(() => {
      const topbar = document.querySelector('.topbar');
      const info = document.querySelector('.info');
      const schemeContainer = document.querySelector('.scheme-container');

      if (topbar) topbar.style.display = 'none';
      if (info) info.style.display = 'none';
      if (schemeContainer) schemeContainer.style.display = 'none';
    });
  }
</script>
