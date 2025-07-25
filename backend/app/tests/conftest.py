"""Arquivo de configuração do pytest para o ambiente Django."""

import io
import pytest
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from faker import Faker
from PIL import Image
from app.models import Carrinho, Cor, Pedido, Produto

@pytest.fixture(autouse=True, scope="session")
def django_test_environment(django_test_environment): # pylint: disable=unused-argument, redefined-outer-name
    """Fixture que ativa o modo de gerenciamento de modelos para testes."""

    for m in [m for m in apps.get_models() if not m._meta.managed]: # pylint: disable=protected-access
        m._meta.managed = True # pylint: disable=protected-access


@pytest.fixture(autouse=True, scope="session")
def faker():
    """Fixture que fornece uma instância do Faker para geração de dados falsos."""

    yield Faker('pt_BR')


@pytest.fixture
def common_client():
    """Fixture que fornece um cliente autenticado para testes comuns."""
    user = User.objects.create_user(
        username="testuser",
        password="12345",
        is_staff=False,
        is_superuser=False
    )

    client = APIClient()
    client.force_authenticate(user=user)
    yield client


@pytest.fixture
def staff_client():
    """Fixture que fornece um cliente autenticado para testes de staff."""

    user = User.objects.create_user(
        username="staffuser",
        password="12345",
        is_staff=True,
        is_superuser=False
    )

    client = APIClient()
    client.force_authenticate(user=user)
    yield client


@pytest.fixture
def img():
    """Fixture que fornece uma imagem de teste em formato JPEG."""

    file = io.BytesIO()
    image = Image.new("RGB", (100, 100), "white")
    image.save(file, "JPEG")
    file.name = "test.jpg"
    file.seek(0)

    yield file


@pytest.fixture
def products(db):
    """Fixture que cria produtos de exemplo para testes."""
    yield [
        Produto.objects.create( # pylint: disable=no-member
            preco=149.90,
            quantidade=10,
            categoria="Camisetas",
            material="Algodão",
            cor_padrao="Preto",
            titulo="Camiseta Básica Preta",
            descricao="Camiseta de algodão confortável, ideal para o dia a dia.",
            altura=2.0,
            comprimento=70.0,
            largura=50.0
        ),
        Produto.objects.create( # pylint: disable=no-member
            preco=349.90,
            quantidade=5,
            categoria="Calçados",
            material="Couro sintético",
            cor_padrao="Branco",
            titulo="Tênis Esportivo Branco",
            descricao="Tênis leve e resistente, ideal para corrida.",
            altura=12.0,
            comprimento=30.0,
            largura=10.0
        ),
        Produto.objects.create( # pylint: disable=no-member
            preco=89.90,
            quantidade=20,
            categoria="Acessórios",
            material="Poliéster",
            cor_padrao="Azul",
            titulo="Boné Azul Marinho",
            descricao="Boné casual com regulagem traseira.",
            altura=10.0,
            comprimento=20.0,
            largura=18.0
        ),
    ]


@pytest.fixture
def colors(db):
    """Fixture que cria cores de exemplo para testes."""
    yield [
        Cor.objects.create( # pylint: disable=no-member
            nome='SlateBlue',
            rgb='#6A5ACD',
        ),
        Cor.objects.create( # pylint: disable=no-member
            nome='DodgerBlue',
            rgb='#1E90FF',
        ),
        Cor.objects.create( # pylint: disable=no-member
            nome='LightGreen',
            rgb='#90EE90',
        ),
    ]


@pytest.fixture
def carts(db):
    """Fixture que cria carrinhos de exemplo para testes."""
    yield [
        Carrinho.objects.create(subtotal=149.90), # pylint: disable=no-member
        Carrinho.objects.create(subtotal=349.90), # pylint: disable=no-member
        Carrinho.objects.create(subtotal=89.90), # pylint: disable=no-member
    ]


@pytest.fixture
def orders(db, carts): # pylint: disable=redefined-outer-name
    """Fixture que cria pedidos de exemplo para testes."""

    yield [
        Pedido.objects.create( # pylint: disable=no-member
            email_usuario="cliente1@example.com",
            codigo_carrinho=carts[0],
            cep="01310-200",
            bairro="Bela Vista",
            complemento="Apto 101",
            estado="SP",
            cidade="São Paulo",
            numero="123",
            quadra="Q1",
            metodo_pagamento="Pix",
            mercadopago_payment_id="mp-001",
            status="approved",
            frete=12.50,
            valor_total=199.90,
            external_reference="REF001"
        ),
        Pedido.objects.create( # pylint: disable=no-member
            email_usuario="cliente2@example.com",
            codigo_carrinho=carts[1],
            cep="30140-000",
            bairro="Savassi",
            complemento="Sala 12",
            estado="MG",
            cidade="Belo Horizonte",
            numero="456",
            quadra="Q3",
            metodo_pagamento="Cartão de crédito",
            mercadopago_payment_id="mp-002",
            status="pending",
            frete=18.90,
            valor_total=329.90,
            external_reference="REF002"
        ),
        Pedido.objects.create( # pylint: disable=no-member
            email_usuario="cliente3@example.com",
            codigo_carrinho=carts[2],
            cep="70070-350",
            bairro="Asa Norte",
            complemento="Bloco B",
            estado="DF",
            cidade="Brasília",
            numero="789",
            quadra="Q5",
            metodo_pagamento="Dinheiro",
            mercadopago_payment_id="mp-003",
            status="rejected",
            frete=0.00,
            valor_total=89.90,
            external_reference="REF003"
        )
    ]
