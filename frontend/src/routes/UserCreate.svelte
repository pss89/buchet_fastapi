<script>
    import { push } from "svelte-spa-router"
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let username = ""
    let password = ""
    let rePassword = ""
    let email = ""

    function post_user(event) {
        event.preventDefault()
        let url = "/api/user/create"
        let params = {
            username: username,
            password: password,
            rePassword: rePassword,
            email: email
        }
        fastapi('post', url, params, 
            (json) => {
                push('/user-login')
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

<div>
    <h5 class="my-3 border-bottom pb-2">회원 가입</h5>
    <Error error={error} />
    <form method="post">
        <div class="mb-3">
            <label for="username">사용자 이름</label>
            <input type="text" class="form-control" id="username" bind:value="{username}">
        </div>
        <div class="mb-3">
            <label for="password">비밀번호</label>
            <input type="password" class="form-control" id="password" bind:value="{password}">
        </div>
        <div class="mb-3">
            <label for="rePassword">비밀번호 확인</label>
            <input type="password" class="form-control" id="rePassword" bind:value="{rePassword}">
        </div>
        <div class="mb-3">
            <label for="email">이메일</label>
            <input type="text" class="form-control" id="email" bind:value="{email}">
        </div>
        <button type="submit" class="btn btn-primary" on:click="{post_user}">생성하기</button>
    </form>
</div>