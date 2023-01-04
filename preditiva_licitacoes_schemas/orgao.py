from typing import Optional

from pydantic import BaseModel


class OrgaoBase(BaseModel):
    cd_estado: Optional[str] = None
    nr_cnpj_orgao: Optional[str] = None
    nm_orgao: Optional[str] = None
    nr_telefone: Optional[str] = None
    ds_email: Optional[str] = None

    nm_endereco: Optional[str] = None
    nm_bairro: Optional[str] = None
    nr_cep: Optional[str] = None


class OrgaoCreate(OrgaoBase):
    pass


class Orgao(OrgaoBase):
    id_orgao: int

    class Config:
        orm_mode = True
