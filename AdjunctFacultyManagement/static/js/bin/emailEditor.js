class EmailEditor {
    init(params) {
        this.value = params.value;
 
        this.input = document.createElement('input');
        this.input.type = 'email';
        this.input.value = this.value;
 
        this.input.addEventListener('input', (event) => {
            this.value = event.target.value;
        });
    }
 
    /* Component Editor Lifecycle methods */
    // gets called once when grid ready to insert the element
    getGui() {
        return this.input;
    }
 
    // the final value to send to the grid, on completion of editing
    getValue() {
        // this simple editor doubles any value entered into the input
        return this.value;
    }
 
    // Gets called once before editing starts, to give editor a chance to
    // cancel the editing before it even starts.
    isCancelBeforeStart() {
        return false;
    }
 
    // Gets called once when editing is finished (eg if Enter is pressed).
    // If you return true, then the result of the edit will be ignored.
    isCancelAfterEnd() {
        // our editor will reject any value greater than 1000
        return false;
    }
 
    // after this component has been created and inserted into the grid
    afterGuiAttached() {
        this.input.focus();
    }
 }