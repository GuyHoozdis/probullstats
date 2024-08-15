"""Define the data models used internally."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt, PositiveInt

if TYPE_CHECKING:
    from datetime import date


class Bull(BaseModel):
    """Data model as defined by the probullstats website."""

    pbid: str
    bull_brand: str
    bull_name: str
    owner: str
    abbi: NonNegativeInt
    pbr: NonNegativeInt
    prca: NonNegativeInt
    historical_rank: PositiveInt
    hist_rank_percentile: NonNegativeFloat
    active_rank: PositiveInt
    mounted: NonNegativeInt
    rode: NonNegativeInt


class Event(BaseModel):
    """Data model as defined by the probullstats website."""

    pbrid: NonNegativeInt
    rid: str
    groupid: str
    rodeo: str
    # state: constr(to_upper=True, min_length=2, max_length=2)
    state: str
    startdate: date
    sanction: str
