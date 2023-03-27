const App = {
    init() {
      Board.newMake();
    },
  }
  
  const Board = {
    nowTurn: 'player_1',
  
    // 새로 만들기
    newMake() {
      let html = '';
  
      for (let i = 0; i < 9; i++) {
        html += `<div class='panel_item' onclick="Board.itemClick(this)"></div>`;
      }
  
      document.querySelector('.panel_list').innerHTML = html;
    },
  
    itemClick($target) {
      if ($target.className != "panel_item") {
        return;
      }
  
      const shape = {player_1: 'O', player_2: 'X'};
      
      $target.innerHTML = `<div>${shape[Board.nowTurn]}</div>`;
      $target.className += ` ${Board.nowTurn}`;
  
      Board.clearChk();
    },
  
    // 클리어 조건 확인
    clearChk() {
      const BoardItem = document.querySelectorAll(`.panel_item`);
  
      const bolArray = new Array(8).fill(true);
  
      // 가로, 세로 일자 체크
      for (let i = 0; i < 3; i++) {
        const keyArr = [
          i, 3+i, 6+i, // 가로
          i*3, i*3+1, i*3+2 // 세로
        ];
  
        for (let j = 0; j < 6; j++) { 
          bolArray[j] = bolArray[j] && Board.itemChk(BoardItem[keyArr[j]]);
        }
      }
  
      // 대각선
      bolArray[6] = Board.itemChk(BoardItem[0]) && Board.itemChk(BoardItem[4]) && Board.itemChk(BoardItem[8]);
      bolArray[7] = Board.itemChk(BoardItem[2]) && Board.itemChk(BoardItem[4]) && Board.itemChk(BoardItem[6]);
  
      const resultBol = bolArray.some(v => v);
  
      // (결과 체크) 승부가 났던가 안났던가.
      if (resultBol || [...BoardItem].every(v => Board.itemChk(v, 'player'))) {
        const $modal = document.querySelector(`.modal`);
        
        $modal.className += ' open';
  
        $modal.innerHTML = `<h2>${resultBol ? `${Board.nowTurn}님이 이겼습니다.` : '무승부'}</h2>`;
  
        setTimeout(() => {
          $modal.className = 'modal';
          Board.newMake();
        }, 2000);
        return;
      }
  
      Board.turnChange();
    },
      
    // 클래스로 체크 여부 판단함
    itemChk: (target, name) => target.className.includes(name || Board.nowTurn),
  
    // 턴 체인지
    turnChange() {
      Board.nowTurn = {player_1: 'player_2'}[Board.nowTurn] || 'player_1';
    },
  }
  
  window.onload = () => {
    App.init();
  }