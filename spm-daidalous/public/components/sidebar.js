class Sidebar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <nav class="sidebar sidebar-offcanvas" id="sidebar">
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="../../index.html">
              <i class="mdi mdi-home-outline menu-icon"></i>
              <span class="menu-title">Home</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false" aria-controls="ui-basic">
              <i class="menu-icon mdi mdi-map-marker-outline"></i>
              <span class="menu-title">Locations</span>
              <i class="menu-arrow"></i> 
            </a>
            <div class="collapse" id="ui-basic">
              <ul class="nav flex-column sub-menu">
                <li class="nav-item"> <a class="nav-link" href="../../pages/view/invoice-list.html">Bukit Timah</a></li>
                <li class="nav-item"> <a class="nav-link" href="../../pages/view/invoice-list.html">Clementi</a></li>
                <li class="nav-item"> <a class="nav-link" href="../../pages/view/invoice-list.html">Ubi</a></li>
              </ul>
            </div>
          </li>
          <li class="nav-item nav-category">help</li>
          <li class="nav-item">
            <a class="nav-link" href="http://bootstrapdash.com/demo/star-admin2-free/docs/documentation.html">
              <i class="menu-icon mdi mdi-file-document"></i>
              <span class="menu-title">Documentation</span>
            </a>
            <a class="nav-link" href="http://bootstrapdash.com/demo/star-admin2-free/docs/documentation.html">
              <i class="menu-icon mdi mdi-headset"></i>
              <span class="menu-title">Support</span>
            </a>
          </li>
        </ul>
      </nav>
        `
    }
}

customElements.define('main-sidebar', Sidebar);