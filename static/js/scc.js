console.log("Hello world");
let cap = document.getElementById('cap').innerText
console.log(cap+".mp3");
console.log(typeof(cap+".mp3"))
let audioElement= new Audio("../../media/audios/"+cap+".mp3");

let masterElement= document.getElementById('masterPlay');
let progressBar= document.getElementById('progressBar');
let vol = document.getElementById("volume");


masterElement.addEventListener('click',()=>{
    if(audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        masterElement.src="/static/icons/pause-svgrepo-com.svg";
        // audioElement.volume = 0.2;
        console.log(audioElement.volume);
    }
    else{
        audioElement.pause();
        masterElement.src="/static/icons/play-button-svgrepo-com.svg";
    }
});

audioElement.addEventListener('timeupdate',()=>{
    let progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    console.log(progress);
    progressBar.value = progress;
});

progressBar.addEventListener('change',()=>{
    audioElement.currentTime = (progressBar.value*audioElement.duration/100);
})

vol.addEventListener('change',()=>{
    audioElement.volume = (vol.value/100);
})