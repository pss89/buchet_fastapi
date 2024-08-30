// 앞에서 질문 목록에 페이징을 적용하였다. 그런데 질문 목록에서 3페이지로 이동하고 3페이지에 있는 게시물 중 한개를 클릭하여 상세 내역을 조회한 후, 
// 브라우저에서 뒤로가기를 하면 기존의 질문 목록인 3페이지로 가는 것이 아니라 첫번째 페이지로 이동한다. 
// 왜냐하면 Home.svelte 파일이 다시 불리워지면서 get_question_list(0) 가 다시 호출되기 때문이다.

// 이러한 현상을 방지하려면 상세 페이지를 호출할때 현재 질문 목록의 페이지 번호를 전달하고 다시 질문 목록으로 돌아올 때도 전달받은 페이지 번호를 다시 넘기는 식으로 개발해야 한다. 
// 하지만 상상해 보라. 얼마나 코드가 복잡해 질지, 한숨이 절로 나온다.

// 이러한 상황의 구세주는 스벨트의 스토어(store)이다. 스토어를 사용하면 변수의 값을 전역적으로 저장할 수 있기 때문에 라우팅 되는 페이지에 상관없이 스토어에 저장된 변수를 사용할 수 있다.

import { writable } from 'svelte/store'

const persist_storage = (key, initValue) => {
  const storedValueStr = localStorage.getItem(key)
  const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)

  store.subscribe((val) => {
    localStorage.setItem(key, JSON.stringify(val));
  })

  return store;
}

// export const page = writable(0)
export const page = persist_storage("page", 0)
export const keyword = persist_storage("keyword", "")
export const access_token = persist_storage("access_token", "")
export const username = persist_storage("username", "")
export const is_login = persist_storage("is_login", false)