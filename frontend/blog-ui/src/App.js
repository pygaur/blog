import React from 'react';
import {
    BrowserRouter as Router,
    Route
} from 'react-router-dom';

import IndexPage from './pages/Index';
import AboutPage from './pages/About';
import ArticlePage from './pages/Article';
import ArticlesPage from './pages/Articles';

import NavBar from './NavBar'
import './App.css';

function App() {
  return (
    <Router>
        <div className="App">
        <NavBar />
            <div id='page-body'>
                <Route path='/' component={IndexPage} exact />
                <Route path='/about' component={AboutPage}  />
                <Route path='/article/:slug' component={ArticlePage}  />
                <Route path='/articles' component={ArticlesPage}  />
            </div>
        </div>
    </Router>
  );
}

export default App;
