const SIZE = 256, sampleNum = 3;
let inputCanvas, outContainerImg2Img, outContainertxt2Img, statusMsg, transferBtn, sampleIndex = 0, modelReady = false, isTransfering = false;
const inputImgs = [], outputImgs = [];

// const edges2pikachu = pix2pix('./models/edges2pikachu_AtoB.pict', modelLoaded);

function setup() {
  // Create canvas
  inputCanvas = createCanvas(SIZE, SIZE);
  inputCanvas.class('border-box pencil').parent('canvasContainer');

  // Selcect output div container
  outContainerImg2Img = select('#output_from_image');
  outContainertxt2Img = select('#output_from_text');

  statusMsg = select('#status');

  // Display initial input image
  loadImage('./static/images/input1.png', inputImg => image(inputImg, 0, 0));

  // Display initial output image
  let out_image = createImg('./static/images/result1.png');
  let out_text = createImg('./static/images/result1.png');
  outContainerImg2Img.html('');
  outContainertxt2Img.html('');
  out_image.class('border-box').parent('output_from_image');
  out_text.class('border-box').parent('output_from_text');

  // Load other sample input/output images
  for (let i = 1; i <= sampleNum; i += 1) {
    loadImage(`./static/images/input${i}.png`, inImg => {
      inputImgs.push(inImg);
      let outImg = createImg(`./static/images/result${i}.png`);
      outImg.hide().class('border-box');
      outputImgs.push(outImg);
    });
  }

  // Set stroke to black
  stroke(0);
  pixelDensity(1);
}

function transferimage2image() {
  isTransfering = true;
  var img = document.createElement("img");
  img.src = './static/images/spinner.gif';
  img.height = 256;
  img.width = 256;
  //optionally set a css class on the image
  var class_name = "foo";
  img.setAttribute("class", class_name);
  const element = document.getElementById("output_from_image");
  element.removeChild(element.childNodes[0]);
  element.appendChild(img);
  // element.replaceChild(img, element.childNodes[0]);

  // Select canvas DOM element
  let canvasElement = document.getElementById('defaultCanvas0');

  var dataURL = canvasElement.toDataURL('image/png').split(',')[1];

  fetch("http://localhost:8000/api/image", {

    // Adding method type
    method: "POST",
    body: dataURL, 
  })
    .then(response => response.json())
    .then(res => img.src = res.imageURL);

}
function transfertext2image() {
  isTransfering = true;
  var img = document.createElement("img");
  img.src = './static/images/spinner.gif';
  img.height = 256;
  img.width = 256;
  //optionally set a css class on the image
  var class_name = "foo";
  img.setAttribute("class", class_name);
  const element = document.getElementById("output_from_text");
  element.removeChild(element.childNodes[0]);
  element.appendChild(img);

  // Select canvas DOM element
  let textElement = document.getElementById('intext');

  var userText = textElement.value;
  // alert(userText)

  fetch("http://localhost:8000/api/text", {

    // Adding method type
    method: "POST",
    body: userText, 
  })
    .then(response => response.json())
    .then(res => img.src = res.imageURL);

}

// Draw on the canvas when mouse is pressed
function draw() {
  if (mouseIsPressed) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}
// Clear the canvas
function clearCanvas() {
  background(255);
}

function getRandomOutput() {
  image(inputImgs[sampleIndex], 0, 0);
  outContainerImg2Img.html('');
  outputImgs[sampleIndex].show().parent('output_from_image');
  sampleIndex += 1;
  if (sampleIndex > sampleNum - 1) sampleIndex = 0;
}

function usePencil() {
  stroke(0);
  strokeWeight(1);
  inputCanvas.removeClass('eraser');
  inputCanvas.addClass('pencil');
}

function useEraser() {
  stroke(255);
  strokeWeight(15);
  inputCanvas.removeClass('pencil');
  inputCanvas.addClass('eraser');
}
