import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const token = localStorage.getItem('access_token');  // Получите токен из localStorage

        // Загрузка постов из API
        axios.get('http://localhost:8000/api/posts/', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
            .then(response => {
                setPosts(response.data);
            })
            .catch(error => {
                console.error('Ошибка при загрузке постов:', error);
            });
    }, []);

    return (
        <div>
            <h1>Главная</h1>
            {posts.length > 0 ? (
                posts.map(post => (
                    <div key={post.id} className="card mb-3">
                        <div className="card-body">
                            <h5 className="card-title">{post.title}</h5>
                            <p className="card-text">{post.content}</p>
                            <p className="card-text">
                                <small className="text-muted">
                                    Автор: {post.author.username} | Дата создания: {new Date(post.created_at).toLocaleDateString()}
                                </small>
                            </p>
                        </div>
                    </div>
                ))
            ) : (
                <p>Постов нет.</p>
            )}
        </div>
    );
};

export default Home;