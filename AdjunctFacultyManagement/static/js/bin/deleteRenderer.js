class DeleteRenderer {
  // gets called once before the renderer is used
  init(params) {
    // create the cell
    this.eGui = document.createElement("a");
    this.eGui.innerHTML = `
        <i class="material-icons" color="error">delete</i>
       `;
    this.eGui.classList = ["delete-row"];
    this.eGui.dataset.rowid = params.value;

    // // add event listener to button

    this.eGui.addEventListener("click", () => {
      modalOpenFunction(params.node.data, params.node.data.employeeID);
    });
  }

  getGui() {
    return this.eGui;
  }

  // gets called whenever the cell refreshes
  refresh() {
    // return true to tell the grid we refreshed successfully
    return true;
  }

  // gets called when the cell is removed from the grid
  destroy() {
    // do cleanup, remove event listener from button
    // if (this.eButton) {
    //     // check that the button element exists as destroy() can be called before getGui()
    //     this.eButton.removeEventListener('click', this.eventListener);
    //}
  }

  getValueToDisplay(params) {
    return params.valueFormatted ? params.valueFormatted : params.value;
  }
}
