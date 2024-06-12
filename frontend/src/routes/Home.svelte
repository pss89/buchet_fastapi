<script>
    import fastapi from "../lib/api"
    import { link } from "svelte-spa-router"
    import { page, is_login } from "../lib/store"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    let question_list = []

    let size = 10
    // let page = 0

    // 게시물의 총건수
    let total = 0
    // 리엑티브 선언 (svelte 에서 상태가 변경될 때 자동으로 업데이트)
    // 전체 페이지 갯수
    $: total_page = Math.ceil(total/size)

    function get_question_list(_page) {
        // fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
        //     response.json().then((json) => {
        //         question_list = json
        //     })
        // })
        let params = {
            page: _page,
            size: size,
        }

        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            // page = _page
            $page = _page
            total = json.total
        });
        // fastapi('get', '/api/question/list', {}, (json) => {
        //     // question_list = json
        //     question_list = json.question_list
        // })
    }

    // get_question_list()
    // get_question_list(0)
    $: get_question_list($page)
</script>

<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="text-center table-dark">
            <th>번호</th>
            <th style="width:50%">제목</th>
            <th>글쓴이</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr class="text-center">
            <!-- <td>{i+1}</td> -->
            <td>{ total - ($page * size) - i}</td>
            <td class="text-start">
                <a use:link href="/detail/{question.id}">{question.subject}</a>
                {#if question.answers.length > 0}
                <span class="text-danger small mx-2">{question.answers.length}</span>
                {/if}
            </td>
            <!-- <td>{question.create_date}</td> -->
            <td>{ question.user ? question.user.username : "" }</td>
            <td>
                {moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}
            </td>
        </tr>
        {/each}
        </tbody>
    </table>
    <!-- 페이징 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <!-- 이전 페이지값 없으면 비활성화 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list($page-1)}">이전</button>
        </li>

        <!-- 페이지번호-->
        {#each Array(total_page) as _, loop_page}
        <!-- 페이지 제한 -->
        {#if loop_page >= $page-5 && loop_page <= $page+5}
        <!-- 현재 페이지와 가틍면 활성화 -->
        <li class="page-item {loop_page === $page && 'active'}">
            <button on:click="{() => get_question_list(loop_page)}" class="page-link">{loop_page + 1}</button>
        </li>
        {/if}
        {/each}

        <!-- 다음 페이지 -->
        <!-- 다음페이지값 없으면 비활성화 -->
        <li class="page-item {page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list($page+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징 끝 -->
    <a use:link href="/question-create" class="btn btn-primary {$is_login ? '' : 'disabled'}">질문 등록하기</a>
</div>