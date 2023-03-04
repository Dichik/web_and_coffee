import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import { ProtectedRoute } from '../components';

import { ROUTER_KEYS } from '../constants';
import Layout from '../layouts/layout';

import routes from '../routes';

interface Component {
  element: () => JSX.Element;
  path: string;
  protectedRoute: boolean;
  key: string;
}

export const MainRouter = () => (
  <Router>
    <Layout>
      <Routes>
        {routes.map((route: Component) => {
          const { element: Component, path, protectedRoute, key } = route;
          if (protectedRoute) {
            return (
              <Route key={key} element={<ProtectedRoute />}>
                <Route
                  element={<Component />}
                  path={ROUTER_KEYS[path as keyof typeof ROUTER_KEYS]}
                />
              </Route>
            );
          }
          return (
            <Route
              key={key}
              element={<Component />}
              path={ROUTER_KEYS[path as keyof typeof ROUTER_KEYS]}
            />
          );
        })}
      </Routes>
    </Layout>
  </Router>
);
