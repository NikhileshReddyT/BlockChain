pragma solidity ^0.5.0;

contract Auction
{
    address payable public beneficiary;
    bool private Auction_Terminated;
    address public highestBidder;
    uint public highestBid;

    mapping(address => uint) pendingReturns;

    constructor() public 
    {
        highestBid = 0;
        beneficiary = msg.sender;
        Auction_Terminated = false;
    }

    function bid() public payable
    {
        require(msg.value > highestBid);
        uint old_bid = highestBid;
        address old_bidder = highestBidder;
        highestBid = msg.value;
        highestBidder = msg.sender;
        pendingReturns[old_bidder] = old_bid;
    }

    function withdraw() public returns (bool)
    {
        uint amount = pendingReturns[msg.sender];
        pendingReturns[msg.sender] = 0;
        bool result = msg.sender.send(amount);
        return result;
    }

    function auctionEnd() public
    {
        require(msg.sender == beneficiary);
        require(Auction_Terminated == false);
        Auction_Terminated = true;
        beneficiary.send(highestBid);
    }
}