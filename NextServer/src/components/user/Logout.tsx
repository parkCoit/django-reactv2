import React from 'react';

type Props = {
    props: (e : React.FormEvent<HTMLInputElement>) => void
}

export default function Logout({props}: any){
    return (
    <form onSubmit={props}>
        <button type='submit'> ๋ก๊ทธ์์ </button>
    </form>
    )}

