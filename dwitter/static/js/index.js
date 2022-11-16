const SIZE = 256, sampleNum = 3;
let inputCanvas, outputContainer, statusMsg, transferBtn, sampleIndex = 0, modelReady = false, isTransfering = false;
const inputImgs = [], outputImgs = [];

// const edges2pikachu = pix2pix('./models/edges2pikachu_AtoB.pict', modelLoaded);

function setup() {
  // Create canvas
  inputCanvas = createCanvas(SIZE, SIZE);
  inputCanvas.class('border-box pencil').parent('canvasContainer');

  // Selcect output div container
  outputContainer = select('#output');
  statusMsg = select('#status');

  // Display initial input image
  loadImage('./static/images/input2.png', inputImg => image(inputImg, 0, 0));

  // let input = createImg('./static/images/input1.png');
  // input.class('border-box').parent('canvasContainer');

  // Display initial output image
  let out = createImg('./static/images/result1.png');
  outputContainer.html('');
  out.class('border-box').parent('output');

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

// Draw on the canvas when mouse is pressed
function draw() {
  if (mouseIsPressed) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}

// function mouseReleased() {
//   if (modelReady && !isTransfering) {
//     transfer()
//   }
// }

function transfer() {
  isTransfering = true;
  var img = document.createElement("img");
  img.src = './static/images/spinner.gif';
  img.height = 256;
  img.width = 256;
  //optionally set a css class on the image
  var class_name = "foo";
  img.setAttribute("class", class_name);
  const element = document.getElementById("output");
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

  // fetch('http://localhost:8000/api/image')
  //   .then(response => response.json())
  //   .then(data => {
  //     if (data.imageURL) {
  //       img.src = data.imageURL;
  //       element.replaceChild(img, element.childNodes[0]);
  //     }
  //   });
  // // Update status message
  // statusMsg.html('Applying Style Transfer...!');

  // // Select canvas DOM element
  // let canvasElement = document.getElementById('defaultCanvas0');
  // // Apply pix2pix transformation
  // edges2pikachu.transfer(canvasElement, result => {
  //   // Clear output container
  //   outputContainer.html('');
  //   // Create an image based result
  //   createImg(result.src).class('border-box').parent('output');
  //   statusMsg.html('Done!');
  //   isTransfering = false;
  // });
}

// A function to be called when the models have loaded
// function modelLoaded() {
//   if (!statusMsg) statusMsg = select('#status');
//   statusMsg.html('Model Loaded!');
//   transferBtn.show();
//   modelReady = true;
// }

// Clear the canvas
function clearCanvas() {
  background(255);
}

function getRandomOutput() {
  image(inputImgs[sampleIndex], 0, 0);
  outputContainer.html('');
  outputImgs[sampleIndex].show().parent('output');
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

// function generate() {
//     var img = document.createElement("img");
//     img.src = './static/images/spinner.gif';
//     img.height = 256;
//     img.width = 256;
//     //optionally set a css class on the image
//     var class_name = "foo";
//     img.setAttribute("class", class_name);
//     const element = document.getElementById("result");
//     element.replaceChild(img, element.childNodes[1]);

//     fetch('http://localhost:8000/api/image')
//         .then(response => response.json())
//         .then(data => {
//             if (data.imageURL) {
//                 img.src = data.imageURL;
//                 element.replaceChild(img, element.childNodes[1]);
//             }
//         });
// }