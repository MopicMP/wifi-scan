"""Tests for wifi-scan."""

import pytest
from wifi_scan import scan


class TestScan:
    """Test suite for scan."""

    def test_basic(self):
        """Test basic usage."""
        result = scan("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            scan("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = scan(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
