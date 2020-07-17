import React from 'react';

const ArticlePage = ( {match} ) => {
    const slug = match.params.slug;
    return (
        <>
        <h1> Article  </h1>
        <p>{slug}</p>
        </>
    );
}

export default ArticlePage;