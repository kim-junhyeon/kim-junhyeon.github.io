// 유튜브 영상 ID만 채우면 사이트 전체에 영상이 들어갑니다.
// 예: https://youtu.be/AbCdEf12345 → 'AbCdEf12345'
const VIDEOS = {
  'memory-ender': '1gkq9mA3te0',
  'echo': '',
};

document.querySelectorAll('.video[data-v]').forEach(el => {
  const id = VIDEOS[el.dataset.v];
  if (!id) { el.remove(); return; } // 영상이 없으면 자리째 숨김
  el.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?rel=0" title="플레이 영상" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
});
