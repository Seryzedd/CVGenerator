$('.alert > .btn-close').on('click', function() {
    $(this).closest('.alert').fadeOut('slow')
})

$('#newBlock').on('click', function() {
    var blockContainers = $('form').find('.block-container')
    var newDiv = document.createElement("div");
    newDiv.classList.add("block-container");

    var blockTitle = document.createElement("h3");

    let child = blockContainers.length + 1;
    blockTitle.textContent = 'Block ' + child;
    blockTitle.setAttribute('class', 'text-secondary');

    createInput("form-control", "block-" + child, 'block-name-' + child, newDiv, 'name ')
    createSelect("form-control", "placement-" + child, 'block-placement-' + child, newDiv, 'Placement ')

    createLineDivContainer('linesContainer-' + child, newDiv, child);
    $("#blocks").append(blockTitle);
    $("#blocks").append(newDiv);
})

function createLineDivContainer(id, parentContainer, blockCounter) {
    const container = document.createElement("div");
    container.setAttribute('id', id)

    createButton('Créer une nouvelle ligne', 'btn btn-outline-dark mt-2', 'line-block-' + blockCounter, container);

    parentContainer.appendChild(container)
}

function createButton(text, className, id, parent) {
    var button = document.createElement("button");
    button.setAttribute('class', className);
    button.setAttribute('id', id);
    button.setAttribute('type', 'button');
    button.textContent = text;

    button.addEventListener("click", (e) => {
      const linescontainer = $('.lineContainer');
      if (!linescontainer) {
        const linescontainer = document.createElement("div");
        linescontainer.setAttribute('class', 'lineContainer');
      }

      var line = newLine();
      linescontainer.appendChild(line);

    });

    parent.appendChild(button);
}
var i = 0;
function newLine() {

    var lineBlock = document.createElement("div");
    lineBlock.setAttribute('class', 'lineContainer')
    i++

    createInputDate('Start At', 'line-' + i, lineBlock, 'StartDateLine-' + i);

    return lineBlock

}

function createInput(className, id, name, parent, labelName) {
    const label = document.createElement("label");
    label.setAttribute('for', id);
    label.textContent  = labelName;

    var newNameInput = document.createElement("input");
    newNameInput.classList.add(className);
    newNameInput.setAttribute("id", id);
    newNameInput.setAttribute('name', name);

    parent.appendChild(label);
    parent.appendChild(newNameInput);
}

function createInputDate(name, id, parentContainer, labelName) {
    const input = document.createElement("input");
    const label = document.createElement("label");

    label.setAttribute('for', id);
    input.setAttribute('type', 'date');
    input.setAttribute('class', 'form-control mt-2');
    input.setAttribute('id', id);

    parentContainer.appendChild(label);
    parentContainer.appendChild(input);
}

function createSelect(className, id, name, parent, labelName) {
    const label = document.createElement("label");
    label.setAttribute('for', id);
    label.textContent  = labelName;

    var newNameInput = document.createElement("select");
    newNameInput.classList.add(className);
    newNameInput.setAttribute("id", id);
    newNameInput.setAttribute('name', name);

    const opt1 = document.createElement("option");
    const opt2 = document.createElement("option");

    opt1.value = "left-side";
    opt1.text = "left";

    opt2.value = "right-side";
    opt2.text = "right";

    newNameInput.appendChild(opt1);
    newNameInput.appendChild(opt2);

    parent.appendChild(label);
    parent.appendChild(newNameInput);
}
