import { Routes, Route } from 'react-router-dom';
import AdminPage from './pages/AdminPage';
import PedidosPage from './pages/PedidosPage';
import ProdutosPage from './pages/ProdutosPage';
import AdicionarProdutoPage from './pages/AdicionarProdutoPage';
import HomePage from './pages/HomePage';
import CatalogoPage from './pages/CatalogoPage';
import DetalheProdutoPage from './pages/DetalheProdutoPage';
import ProdutoPageCatalogo from './pages/ProdutoPageCatalogo';
import CheckoutPage from './pages/CheckoutPage';
import AdminProtectedRoute from './components/AdminProtectedRoute'; 
import TokenEntryPage from './pages/TokenEntryPage';
import Carrinho from './components/Carrinho';
import DetalhePedidoPage from './pages/DetalhePedidoPage';


function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <div className="flex-grow">
        <Routes>

          <Route path="/inserir-token" element={<TokenEntryPage />} />
          <Route element={<AdminProtectedRoute />}>
            <Route path="/admin" element={<AdminPage />}>
              <Route index element={<PedidosPage />} />
              <Route path="pedidos" element={<PedidosPage />} />
              <Route path="produtos" element={<ProdutosPage />} />
              <Route path="adicionarproduto" element={<AdicionarProdutoPage />} />
              <Route path="produto/:produtoId" element={<DetalheProdutoPage />} />
              <Route path="pedido/:pedidoId" element={<DetalhePedidoPage />} />
              <Route path="produtos/editar/:produtoId" element={<AdicionarProdutoPage />} />
            </Route>
          </Route>

          <Route path="/" element={<HomePage />} />
          <Route path="/categoria/:categoria" element={<CatalogoPage />} />
          <Route path="/produto/:id" element={<ProdutoPageCatalogo />} />
          <Route path="/produto/:id" element={<ProdutoPageCatalogo />} />
          <Route path="/checkout" element={<CheckoutPage />} />
          <Route path="/carrinho" element={<Carrinho />} />
          <Route path="/produtos/search" element={<CatalogoPage />} />

          <Route path="*" element={
            <div className="min-h-screen flex items-center justify-center">
              <h1 className="text-2xl font-bold">404 - Página Não Encontrada</h1>
            </div>
          } />
        </Routes>
      </div>
    </div>
  );
}

export default App;