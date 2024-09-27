<script setup lang="ts">

import { ref } from 'vue'
import { FFmpeg } from '@ffmpeg/ffmpeg';
import { fetchFile, toBlobURL } from '@ffmpeg/util';

const loaded = ref(false);
const ffmpegRef = new FFmpeg();
const videoRef = ref(null);
const messageRef = ref(null);

const load = async () => {
    console.log("loading ffmpeg-core");
    const baseURL = 'https://unpkg.com/@ffmpeg/core@0.12.6/dist/esm'
    const ffmpeg = ffmpegRef;
    ffmpeg.on('log', ({ message }) => {
        messageRef.value.innerHTML = message;
        console.log(message);
    });
    // toBlobURL is used to bypass CORS issue, urls with the same
    // domain can be used directly.
    await ffmpeg.load({
        coreURL: await toBlobURL(`${baseURL}/ffmpeg-core.js`, 'text/javascript'),
        wasmURL: await toBlobURL(`${baseURL}/ffmpeg-core.wasm`, 'application/wasm'),
    });
    loaded.value = true;
}

const transcode = async () => {
    const ffmpeg = ffmpegRef;
    await ffmpeg.writeFile('input.webm', await fetchFile('https://raw.githubusercontent.com/ffmpegwasm/testdata/master/Big_Buck_Bunny_180_10s.webm'));
    await ffmpeg.exec(['-i', 'input.webm', 'output.mp4']);
    const data = await ffmpeg.readFile('output.mp4');
    videoRef.value.src =
        URL.createObjectURL(new Blob([data.buffer], {type: 'video/mp4'}));
}

</script>

<template>
  <template v-if="loaded">
    <video ref="videoRef" controls></video><br/>
    <button @click="transcode">Transcode webm to mp4</button>
    <p ref="messageRef"></p>
    <p>Open Developer Tools (Ctrl+Shift+I) to View Logs</p>
  </template>
  <button v-else @click="load">Load ffmpeg-core (~31 MB)</button>
</template>
