<script>
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import { link, push } from "svelte-spa-router"
    import { is_login, username, email } from "../lib/store"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    // export let params = {}
</script>

<!-- 
로그인 한 사용자의 프로필 화면을 만들어 보자. 
이 화면에는 사용자에 대한 기본정보와 작성한 질문, 답변, 댓글 등을 확인할 수 있도록 
하면 좋을 것이다. 
-->
<div class="container my-3">
    <h2 class="border-bottom py-2">프로필</h2>
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-body">
                    <p class="card-text">사용자 이름: {$username}</p>
                    <p class="card-text">이메일: {$email}</p>
                </div>
            </div>
        </div>
        <div class="col-12">
            <h3 class="border-bottom py-2">질문</h3>
            <div class="card">
                <div class="card-body">
                    <p class="card-text">질문이 없습니다.</p>
                </div>
            </div>
        </div>
        <div class="col-12">
            <h3 class="border-bottom py-2">답변</h3>
            <div class="card">
                <div class="card-body">
                    <p class="card-text">답변이 없습니다.</p>
                </div>
            </div>
        </div>
        <div class="col-12">
            <h3 class="border-bottom py-2">댓글</h3>
            <div class="card">
                <div class="card-body">
                    <p class="card-text">댓글이 없습니다.</p>
                </div>
            </div>
        </div>
    </div>
</div>